import json


def format_changes_as_json(data):
    result = []

    for item in data:
        change = {
            'key': item['key'],
            'status': item['status'],
            'old_value': (
                item['old_value'] if item['old_value'] != 'null' else None
            ),
            'new_value': (
                item['new_value'] if item['new_value'] != 'null' else None
            ),
            'children': []
        }

        if item['children']:
            change['children'] = format_changes_as_json(item['children'])

        result.append(change)

    return result


def print_changes_json(data):
    formatted_diff = format_changes_as_json(data)
    return json.dumps(formatted_diff, indent=4)


def convert_to_json(data):
    # Заменяем None на null для корректного формата JSON
    return json.dumps(data, default=lambda x: (None if x is None else x), indent=4)