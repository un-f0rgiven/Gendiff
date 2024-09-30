import json


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



def load_json_file(file_path):
    """Загружает данные из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# # Пример использования с файлами
# file1_path = 'file1_r.json'
# file2_path = 'file2_r.json'

# # Подгружаем данные из файлов
# data1 = load_json_file(file1_path)
# data2 = load_json_file(file2_path)

# # Получаем различия и форматируем их
# diff = build_diff(data1, data2)

# print(diff)


# где file1_r.json: { "common": { "setting1": "Value 1", "setting2": 200, "setting3": true, "setting6": { "key": "value", "doge": { "wow": "" } } }, "group1": { "baz": "bas", "foo": "bar", "nest": { "key": "value" } }, "group2": { "abc": 12345, "deep": { "id": 45 } } } file2_r.json: { "common": { "follow": false, "setting1": "Value 1", "setting3": null, "setting4": "blah blah", "setting5": { "key5": "value5" }, "setting6": { "key": "value", "ops": "vops", "doge": { "wow": "so much" } } }, "group1": { "foo": "bar", "baz": "bars", "nest": "str" }, "group3": { "deep": { "id": { "number": 45 } }, "fee": 100500 } }
