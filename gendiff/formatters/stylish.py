from gendiff.formatters.replacements import replace_values, replacements


def create_indentation(depth, indent_space=4):
    return ' ' * (depth * indent_space - 2)


def format_value(node, depth):
# открывающая скобка используется только для форматирования значений типа dict
# По аналогии с предыдущим модулем в этой функции будет правильнее реализовать 
# логику приведения всех возможных типов значений (включая тип dict) нод к строке.
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
        result.append(f"{create_indentation(depth + 1)}"
                      f"{symbol} {child['key']}: {{")
        result.extend(format_value(child[value], depth + 1))
        result.append(f"{create_indentation(depth + 1)}  }}")
    else:
        result.append(f"{create_indentation(depth + 1)}"
                      f"{symbol} {child['key']}: {child[value]}")

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
    indentation = create_indentation(depth + 1)

    if not child['children']:
        if isinstance(child['old_value'], dict):
            result.append(f"{indentation}- {child['key']}: ")
            result.append("{\n")
            result.append(format_value(child['old_value'], depth + 1))
            result.append(f"{indentation}  }}\n")
            result.append(f"{indentation}+ "
                          f"{child['key']}: {child['new_value']}\n")
        elif isinstance(child['new_value'], dict):
            result.append(f"{indentation}- "
                          f"{child['key']}: {child['old_value']}\n")
            result.append(f"{indentation}+ {child['key']}: ")
            result.append("{\n")
            result.append(format_value(child['new_value'], depth + 1))
            result.append(f"{indentation}  }}\n")
        else:
            result.append(f"{indentation}- "
                          f"{child['key']}: {child['old_value']}\n")
            result.append(f"{indentation}+ "
                          f"{child['key']}: {child['new_value']}\n")
    else:
        result.append(f"{indentation}  {child['key']}: {{")
        result.append(format_children(child['children'], depth + 1))
        result.append(f"{indentation}  }}")

    return result


def format_diff(diff, depth=0):
# не описан тип 'updated'
    result = []

    for node in diff:
        status = node['status']
        key = node['key']
        indentation = create_indentation(depth + 1)

        if status in ('added', 'removed'):
        # разделить логику на отдельные ветки 'added' и 'removed'
            result.append(f"{indentation}"
                          f"{'+' if status == 'added' else '-'} {key}: {{")
                        # Открывающая скобка используется только для форматирования значений типа dict.
            result.append(format_value(node['old_value'], depth + 1))
            result.append(f"{indentation}  }}")

        elif status == 'unchanged':
            result.append(f"{indentation}  {key}: {{")
            result.append(format_value(node['old_value'], depth + 1))
            result.append(f"{create_indentation(depth)} }}")

        elif status == 'nested':
            result.append(f"{indentation}  {key}: {{")
            result.append(format_children(node['children'], depth + 1))
            # Так как diff является деревом, то и обработку ноды типа nested нужно выполнять 
            # при помощи рекурсивного вызова format_diff – таким образом количество кода в 
            # этом модуле значительно сократится.
            result.append(f"{indentation}  }}")

    return result
    # По аналогии с plain, в случае, если значение ноды оказалось равно недопустимому значению, 
    # форматтер должен выбросить исключение ValueError.

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
