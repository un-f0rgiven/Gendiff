def create_symbol_indentation(depth, indent_space=4, symbol=2):
    return ' ' * (depth * indent_space - symbol)


def create_indentation(depth, indent_space=4):
    return ' ' * (depth * indent_space)


def formatted_value(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def format_value(node, depth=0):
    result = []

    if not isinstance(node, dict):
        return formatted_value(node)

    for key, value in node.items():
        indentation = create_indentation(depth + 1)

        if isinstance(value, dict):
            result.append(f"{indentation}{key}: {{")
            result.append(format_value(value, depth + 1))
            result.append(f"{indentation}}}")
        else:
            result.append(f"{indentation}{key}: {formatted_value(value)}")

    return '\n'.join(result)


def add_value(result, symbol_indentation, key, value, prefix, depth):
    if isinstance(value, dict):
        result.append(f"{symbol_indentation}{prefix} {key}: {{")
        result.append(format_value(value, depth + 1))
        result.append(f"{create_indentation(depth + 1)}}}")
    else:
        result.append(
            f"{symbol_indentation}{prefix} {key}: {formatted_value(value)}"
        )


def handle_node(node, depth, result, symbol_indentation):
    status = node['status']
    key = node['key']
    children = node.get('children', None)
    old_value = node.get('old_value', None)
    new_value = node.get('new_value', None)

    if status == 'added':
        add_value(result, symbol_indentation, key, old_value, '+', depth)
    elif status == 'removed':
        add_value(result, symbol_indentation, key, old_value, '-', depth)
    elif status == 'unchanged':
        add_value(result, symbol_indentation, key, old_value, ' ', depth)
    elif status == 'updated':
        add_value(result, symbol_indentation, key, old_value, '-', depth)
        add_value(result, symbol_indentation, key, new_value, '+', depth)
    elif status == 'nested':
        result.append(f"{symbol_indentation}  {key}: {{")
        result.append(format_diff(children, depth + 1))
        result.append(f"{create_indentation(depth + 1)}}}")
    else:
        raise ValueError(f'Недопустимый тип: {status}')


def format_diff(diff, depth=0):
    result = []

    for node in diff:
        symbol_indentation = create_symbol_indentation(depth + 1)
        handle_node(node, depth, result, symbol_indentation)

    return '\n'.join(result)


def return_stylish_format(data):
    formatted_data = format_diff(data)

    return f'{{\n{formatted_data}\n}}'
