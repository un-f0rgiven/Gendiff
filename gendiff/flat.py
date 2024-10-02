def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def format_diff_lines(first_data, second_data):
    diff_lines = []
    all_keys = sorted(first_data.keys() | second_data.keys())

    for key in all_keys:
        first_value = first_data.get(key)
        second_value = second_data.get(key)
        formatted_first_value = format_value(first_value)
        formatted_second_value = format_value(second_value)

        if key not in first_data:
            diff_lines.append(f"  + {key}: {formatted_second_value}")
        elif key not in second_data:
            diff_lines.append(f"  - {key}: {formatted_first_value}")
        elif formatted_first_value != formatted_second_value:
            diff_lines.append(f"  - {key}: {formatted_first_value}")
            diff_lines.append(f"  + {key}: {formatted_second_value}")
        else:
            diff_lines.append(f"    {key}: {formatted_first_value}")

    return diff_lines


def print_diff_lines(first_data, second_data):
    formatted_changes = format_diff_lines(first_data, second_data)
    if formatted_changes:
        results = "\n".join(formatted_changes)
        return f"{{\n{results}\n}}"
    return "{}"
