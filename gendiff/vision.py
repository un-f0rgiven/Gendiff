

def create_diff_node(key, status, value=None):
    return {
        'key': key,
        'status': status,
        'value': value,
        'children': []
    }

def format_value(value):
    """Приведение значений к нужному формату."""
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    return value

def build_diff(file1, file2):
    """Сравниваем два словаря и возвращаем различия."""
    diff = []
    all_keys = sorted(set(file1.keys()).union(file2.keys()))

    for key in all_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key in file1 and key not in file2:
            diff.append(create_diff_node(key, 'removed', format_value(value1)))
        elif key not in file1 and key in file2:
            diff.append(create_diff_node(key, 'added', format_value(value2)))
        elif value1 == value2:
            diff.append(create_diff_node(key, 'unchanged', format_value(value1)))
        else:
            # Если оба значения являются словарями, рекурсивно обрабатываем их
            if isinstance(value1, dict) and isinstance(value2, dict):
                child_diff = build_diff(value1, value2)
                node = create_diff_node(key, 'modified', None)  # Устанавливаем значение в None
                node['children'] = child_diff
                diff.append(node)
            else:
                # Если значения различаются и хотя бы одно из них не словарь
                diff.append(create_diff_node(key, 'removed', format_value(value1)))
                diff.append(create_diff_node(key, 'added', format_value(value2)))

    return diff
