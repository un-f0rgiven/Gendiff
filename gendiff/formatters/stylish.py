from gendiff.formatters.replacements import replace_values, replacements

def create_indentation(depth, indent_space=4):
    return ' ' * (depth * indent_space - 2)


def format_value(node, depth):
    result = []
    
    if isinstance(node, dict):
        for key, value in node.items():
            value_indentation = create_indentation(depth + 1)

            if isinstance(value, dict):
                result.append(f"{value_indentation}  {key}: {{")
                result.append(format_value(value, depth + 1))
                result.append(f"{create_indentation(depth + 1)}  }}")
            else:
                result.append(f"{value_indentation}  {key}: {value}")

    return result


def format_children(children, depth):
    result = []

    handlers = {
        'added': handle_added,
        'removed': handle_removed,
        'unchanged': handle_unchanged,
        'updated': handle_updated,
        'nested': handle_nested,
    }

    for child in children:
        status = child['status']
        if status in handlers:
            result.append(handlers[status](child, depth))

    return result


def handle_value(child, depth, symbol, value):
    result = []
    
    if isinstance(child[value], dict):
        result.append(f"{create_indentation(depth + 1)}{symbol} {child['key']}: {{")
        result.extend(format_value(child[value], depth + 1))
        result.append(f"{create_indentation(depth + 1)}  }}")
    else:   
        result.append(f"{create_indentation(depth + 1)}{symbol} {child['key']}: {child[value]}")

    
    return result


def handle_added(child, depth, value='old_value', symbol='+'):
    return handle_value(child, depth, symbol, value)


def handle_removed(child, depth, value='old_value', symbol='-'):
    return handle_value(child, depth, symbol, value)


def handle_unchanged(child, depth, value='old_value', symbol=' '):
    return handle_value(child, depth, symbol, value)


def handle_updated(child, depth):
    result = []

    result.append(handle_removed(child, depth, 'old_value', '-'))
    result.append(handle_added(child, depth, 'new_value', '+'))
    return result


def handle_nested(child, depth):
    result = []

    if child['children'] == []:
        if isinstance(child['old_value'], dict) and isinstance(child['new_value'], str):
            result.append(f"{create_indentation(depth + 1)}- {child['key']}: ")
            result.append("{\n")
            result.append(format_value(child['old_value'], depth + 1))
            result.append(f"{create_indentation(depth + 1)}  }}\n")
            result.append(f"{create_indentation(depth + 1)}+ {child['key']}: {child['new_value']}\n")
        elif isinstance(child['new_value'], dict) and isinstance(child['old_value'], str):
            result.append(f"{create_indentation(depth + 1)}- {child['key']}: {child['old_value']}\n")
            result.append(f"{create_indentation(depth + 1)}+ {child['key']}: ")
            result.append("{\n")
            result.append(format_value(child['new_value'], depth + 1))
            result.append(f"{create_indentation(depth + 1)}  }}\n")
        else:
            result.append(f"{create_indentation(depth + 1)}- {child['key']}: {child['old_value']}\n")
            result.append(f"{create_indentation(depth + 1)}+ {child['key']}: {child['new_value']}\n")
    else:
        result.append(f"{create_indentation(depth + 1)}  {child['key']}: {{")
        result.append(format_children(child['children'], depth + 1))
        result.append(f"{create_indentation(depth + 1)}  }}")

    return result


def format_diff(diff, depth=0):
    result = []

    for node in diff:
        if node['status'] == 'added':
            result.append(f"{create_indentation(depth + 1)}+ {node['key']}: {{")
            result.append(format_value(node['old_value'], depth + 1))
            result.append(f"{create_indentation(depth + 1)}  }}")

        elif node['status'] == 'removed':
            result.append(f"{create_indentation(depth + 1)}- {node['key']}: {{")
            result.append(format_value(node['old_value'], depth + 1))
            result.append(f"{create_indentation(depth + 1)}  }}")

        elif node['status'] == 'unchanged': 
            result.append(f"{create_indentation(depth + 1)}  {node['key']}: {{")
            result.append(format_value(node['old_value'], depth + 1))
            result.append(f"{create_indentation(depth)} }}")

        elif node['status'] == 'nested':
            result.append(f"{create_indentation(depth + 1)}  {node['key']}: {{")
            result.append(format_children(node['children'], depth + 1))
            result.append(f"{create_indentation(depth + 1)}  }}")

    return result

def format_data(data):
    if isinstance(data, list):
        result = []
        for item in data:
            result.append(format_data(item))
        return '\n'.join(result)
    elif isinstance(data, str):
        return data 
    else:
        return str(data)


def return_stylish_format(data):
    formatted_diff = format_diff(data)
    formatted_data = format_data(formatted_diff)
    output = replace_values(formatted_data, replacements=replacements)
    
    return f'{{\n{output}\n}}'