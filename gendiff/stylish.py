def format_value(value):
    if isinstance(value, dict):
        return format_dict(value)
    if isinstance(value, list):
        return format_list(value)
    if value is None:
        return 'null'
    return str(value).lower() if isinstance(value, bool) else str(value)

def format_dict(data):
    lines = []
    for key, item in sorted(data.items()):
        lines.append(f"{key}: {format_value(item)}")
    return "{\n" + "\n".join(lines) + "\n}"

def format_list(data):
    return "[\n" + ",\n".join(f"  {format_value(item)}" for item in data) + "\n]"

def format_diff(diff, indent=0):
    result = []
    indent_space = ' ' * indent

    for key, change in sorted(diff.items()):
        status = change['status']

        if status == 'added':
            result.append(f"{indent_space}+ {key}: {format_value(change['value'])}")
        elif status == 'removed':
            result.append(f"{indent_space}- {key}: {format_value(change['value'])}")
        elif status == 'modified':
            old_value, new_value = change['value'] if change['value'] else (None, None)
            if old_value is not None:
                result.append(f"{indent_space}- {key}: {format_value(old_value)}")
            if new_value is not None:
                result.append(f"{indent_space}+ {key}: {format_value(new_value)}")
        elif status == 'unchanged':
            result.append(f"{indent_space}  {key}: {format_value(change['value'])}")

        # Если есть дочерние элементы, форматируем их
        if change.get('children'):
            child_diff = {child['key']: child for child in change['children']}
            child_result = format_diff(child_diff, indent + 2)
            result.append(child_result)

    return "\n".join(result)

def format_full_diff(diff):
    formatted_diff = format_diff(diff)
    return "{\n" + formatted_diff + "\n}"