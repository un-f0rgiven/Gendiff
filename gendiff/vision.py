

def create_diff_node(key, status, value=None):
    return {
        'key': key,
        'status': status,
        'value': value,
        'children': []
    }

def build_diff(file1, file2):
    """Сравниваем два словаря и возвращаем различия."""
    diff = []  # Изменяем на список для хранения узлов
    all_keys = sorted(set(file1.keys()).union(file2.keys()))  # Объединяем все ключи из обоих файлов

    for key in all_keys:
        value1 = file1.get(key)  # Получаем значение из первого файла
        value2 = file2.get(key)  # Получаем значение из второго файла

        if key in file1 and key not in file2:
            # Ключ есть в первом файле, но отсутствует во втором
            diff.append(create_diff_node(key, 'removed', value1))
        elif key not in file1 and key in file2:
            # Ключ отсутствует в первом файле, но есть во втором
            diff.append(create_diff_node(key, 'added', value2))
        elif value1 == value2:
            # Ключи есть в обоих файлах и значения совпадают
            diff.append(create_diff_node(key, 'unchanged', value1))
        else:
            # Ключи есть в обоих файлах, но значения различаются
            if isinstance(value1, dict) and isinstance(value2, dict):
                # Рекурсивно обрабатываем вложенные словари
                child_diff = build_diff(value1, value2)
                node = create_diff_node(key, 'modified')
                node['children'] = child_diff
                diff.append(node)
            else:
                # Регистрация изменений: одно значение как 'removed', другое как 'added'
                diff.append(create_diff_node(key, 'removed', value1))
                diff.append(create_diff_node(key, 'added', value2))

    return diff  # Возвращаем список различий

