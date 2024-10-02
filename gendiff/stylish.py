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

    # Создаем сопоставление статусов и обработчиков.
    handlers = {
        'added': handle_added,
        'removed': handle_removed,
        'unchanged': handle_unchanged,
        'updated': handle_updated,
    }

    for child in children:
        status = child['status']
        if status in handlers:
            result += handlers[status](child, depth)

    return result


def handle_added(child, depth):
    result = f"{create_indentation(depth + 1)}+ {child['key']}: "
    if isinstance(child['old_value'], dict):
        result += "{\n"
        result += format_value(child['old_value'], depth + 1)
        result += f"{create_indentation(depth + 1)}  }}\n"
    else:
        result += f"{child['old_value']}\n"
    return result


def handle_removed(child, depth):
    result = f"{create_indentation(depth + 1)}- {child['key']}: "
    if isinstance(child['old_value'], dict):
        result += "{\n"
        result += format_value(child['old_value'], depth + 1)
        result += f"{create_indentation(depth + 1)}  }}\n"
    else:
        result += f"{child['old_value']}\n"
    return result


def handle_unchanged(child, depth):
    result = f"{create_indentation(depth + 1)}  {child['key']}: "
    if isinstance(child['old_value'], dict):
        result += "{\n"
        result += format_value(child['old_value'], depth + 1)
        result += f"{create_indentation(depth)}}}\n"
    else:
        result += f"{child['old_value']}\n"
    return result


def handle_updated(child, depth):
    result = ""
    if child['children'] == []:
        if isinstance(
            child['old_value'], dict
        ) and isinstance(
            child['new_value'], str
        ):
            result += (f"{create_indentation(depth + 1)}- "
                       f"{child['key']}: ")
            result += "{\n"
            result += format_value(child['old_value'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"
            result += (f"{create_indentation(depth + 1)}+ "
                       f"{child['key']}: {child['new_value']}\n")
        elif isinstance(
            child['new_value'], dict
        ) and isinstance(
            child['old_value'], str
        ):
            result += (f"{create_indentation(depth + 1)}- "
                       f"{child['key']}: {child['old_value']}\n")
            result += (f"{create_indentation(depth + 1)}+ "
                       f"{child['key']}: ")
            result += "{\n"
            result += format_value(child['new_value'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

        elif isinstance(
            child['old_value'], str
        ) and isinstance(
            child['new_value'], str
        ):
            result += (f"{create_indentation(depth + 1)}- "
                       f"{child['key']}: {child['old_value']}\n")
            result += (f"{create_indentation(depth + 1)}+ "
                       f"{child['key']}: {child['new_value']}\n")
    else:
        result += (f"{create_indentation(depth + 1)}  "
                   f"{child['key']}: {{\n")
        result += format_children(child['children'], depth + 1)
        result += f"{create_indentation(depth + 1)}  }}\n"
    return result


def format_diff(diff, depth=0):
    result = ""

    for node in diff:
        if node['status'] == 'added':
            result += f"{create_indentation(depth + 1)}+ {node['key']}: {{\n"
            result += format_value(node['old_value'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

        elif node['status'] == 'removed':
            result += f"{create_indentation(depth + 1)}- {node['key']}: {{\n"
            result += format_value(node['old_value'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

        elif node['status'] == 'unchanged':
            result += f"{create_indentation(depth + 1)}  {node['key']}: {{\n"
            result += format_value(node['old_value'], depth + 1)
            result += f"{create_indentation(depth)}}}\n"

        elif node['status'] == 'updated':
            result += f"{create_indentation(depth + 1)}  {node['key']}: {{\n"
            result += format_children(node['children'], depth + 1)
            result += f"{create_indentation(depth + 1)}  }}\n"

    return f"{{\n{result}}}"
