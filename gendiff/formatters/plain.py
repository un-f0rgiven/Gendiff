from gendiff.formatters.replacements import replace_values, replacements


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_changes(data, parent_key=''):
    result = []

    handlers = {
        'added': handle_added,
        'removed': handle_removed,
        'updated': handle_updated,
        'unchanged': handle_unchanged
    }

    for item in data:
        current_key = (
            f"{parent_key}.{item['key']}" if parent_key else item['key']
        )

        status = item['status']
        if status in handlers:
            change_message = handlers[status](item, current_key)
            if change_message:
                result.append(change_message)

        if item.get('children'):
            result.extend(format_changes(item['children'], current_key))

    return result


def handle_added(item, current_key):
    value = item['old_value'] if item['old_value'] != 'null' else None
    return (f"Property '{current_key}' was added "
            f"with value: {format_value(value)}")


def handle_removed(item, current_key):
    return f"Property '{current_key}' was removed"


def handle_unchanged(item, current_key):
    return ''


def handle_updated(item, current_key):
    old_value = item['old_value'] if item['old_value'] != 'null' else None
    new_value = item['new_value'] if item['new_value'] != 'null' else None

    if old_value != new_value:
        return (f"Property '{current_key}' was updated. "
                f"From {format_value(old_value)} "
                f"to {format_value(new_value)}")
    return ''  # Возвращаем пустую строку


def return_plain_format(data):
    formatted_diff = format_changes(data)
    formatted_data = '\n'.join(formatted_diff)
    output = replace_values(formatted_data, replacements=replacements)

    return output
