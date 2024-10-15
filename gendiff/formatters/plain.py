def format_value(value):
    
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def handle_added(item, current_key):
    value = item['old_value'] if item['old_value'] != 'null' else None
    return (f"Property '{current_key}' was added "
            f"with value: {format_value(value)}")


def handle_removed(item, current_key):
    return f"Property '{current_key}' was removed"


def handle_unchanged(item, current_key):
    return ''


def handle_updated(item, current_key):

    old_value = item['old_value']
    new_value = item['new_value']

    return (f"Property '{current_key}' was updated. "
            f"From {format_value(old_value)} "
            f"to {format_value(new_value)}")


def handle_nested(item, current_key):
    return ''


HANDLERS = {
        'added': handle_added,
        'removed': handle_removed,
        'updated': handle_updated,
        'unchanged': handle_unchanged,
        'nested': handle_nested
}


def format_changes(data, parent_key=''):
    result = []

    for item in data:
        current_key = (
            f"{parent_key}.{item['key']}" if parent_key else item['key']
        )

        status = item['status']
        if status in HANDLERS:
            change_message = HANDLERS[status](item, current_key)
            if change_message:
                result.append(change_message)
        else:
            raise ValueError(f'Недопустимый тип: {status}')

        if item.get('children'):
            result.extend(format_changes(item['children'], current_key))

    return result


def return_plain_format(data):
    formatted_diff = format_changes(data)
    formatted_data = '\n'.join(formatted_diff)

    return formatted_data
