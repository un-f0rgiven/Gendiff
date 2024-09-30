

def create_indentation(depth, indent_space=4):
    """Создает строку отступов в зависимости от уровня вложенности."""
    return ' ' * (depth * indent_space - 2)

def format_value(node, depth):
    result = ""
    if isinstance(node, dict):
        for key, value in node.items():
            value_indentation = create_indentation(depth + 1)

            if isinstance(value, dict):
                result += f"{value_indentation}  {key}: {{\n"
                result += format_value(value, depth + 1)
                result += f"{create_indentation(depth + 1)}  }}\n"
            else:
                result += f"{value_indentation}  {key}: {value}\n"

    return result

def format_children(children, depth):
    """Форматирует детей узла и возвращает строку с результатом."""
    result = ""

    for child in children:
        if child['status'] == 'added':
            result += f"{create_indentation(depth + 1)}+ {child['key']}: "
            if isinstance(child['value'], dict):
                result += "{\n"
                result += format_value(child['value'], depth + 1)
                result += f"{create_indentation(depth + 1)}  }}\n"
            else:
                result += f"{child['value']}\n"
                
        elif child['status'] == 'removed':
            result += f"{create_indentation(depth + 1)}- {child['key']}: "
            if isinstance(child['value'], dict):
                result += "{\n"
                result += format_value(child['value'], depth + 1)
                result += f"{create_indentation(depth + 1)}  }}\n"
            else:
                result += f"{child['value']}\n"
                
        elif child['status'] == 'unchanged':
            result += f"{create_indentation(depth + 1)}  {child['key']}: "
            if isinstance(child['value'], dict):
                result += "{\n"
                result += format_value(child['value'], depth + 1)
                result += f"{create_indentation(depth)}}}\n"
            else:
                result += f"{child['value']}\n"
                
        elif child['status'] == 'modified':
            result += f"{create_indentation(depth + 1)}  {child['key']}: {{\n"
            result += format_children(child['children'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

    return result

def format_diff(diff, depth=0):
    result = ""

    for node in diff:
        if node['status'] == 'added':
            result += f"{create_indentation(depth + 1)}+ {node['key']}: {{\n"
            result += format_value(node['value'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

        elif node['status'] == 'removed':
            result += f"{create_indentation(depth + 1)}- {node['key']}: {{\n"
            result += format_value(node['value'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

        elif node['status'] == 'unchanged':
            result += f"{create_indentation(depth + 1)}  {node['key']}: {{\n"
            result += format_value(node['value'], depth + 1)
            result += f"{create_indentation(depth)}}}\n"

        elif node['status'] == 'modified':
            result += f"{create_indentation(depth + 1)}  {node['key']}: {{\n"
            result += format_children(node['children'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

    return result
