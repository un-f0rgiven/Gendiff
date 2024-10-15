def create_diff_node(key, status, old_value=None, new_value=None):
# Будет правильнее сделать либо так, чтобы create_diff_node позволял 
# задать значение children (то есть сделать так, чтобы при помощи этой 
# функции можно было создать любой тип ноды), либо избавиться от этой 
# функции и создавать ноды непосредственно в build_diff
    return {
        'key': key,
        'status': status,
        'old_value': old_value,
        'new_value': new_value,
        'children': []
    }


def build_diff(file1, file2):
    diff = []
    all_keys = sorted(set(file1.keys()).union(file2.keys()))

    for key in all_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key in file1 and key not in file2:
            diff.append(create_diff_node(key, 'removed', value1))
        elif key not in file1 and key in file2:
            diff.append(create_diff_node(key, 'added', value2))
        elif value1 == value2:
            diff.append(create_diff_node(key, 'unchanged', value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            child_diff = build_diff(value1, value2)
            node = create_diff_node(key, 'nested')
            node['children'] = child_diff
            # либо создавать 'children' тут
            diff.append(node)
        else:
            diff.append(create_diff_node(key, 'updated', value1, value2))

    return diff
