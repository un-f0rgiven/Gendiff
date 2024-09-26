from vision import build_diff
<<<<<<< HEAD
import json

def format_diff(diff, indent=1):
=======

def format_diff(diff, indent=0):
>>>>>>> d3e7ea6bfccc6dee80c5e2e4b06bc2efcdd0485c
    result = []
    for node in diff:
        key = node['key']
        status = node['status']
        value = node.get('value')
<<<<<<< HEAD
        indentation = '  ' * indent
=======
        indentation = ' ' * indent
>>>>>>> d3e7ea6bfccc6dee80c5e2e4b06bc2efcdd0485c
        
        if status == 'added':
            result.append(f"{indentation}+ {key}: {value}" if not isinstance(value, dict) else f"{indentation}+ {key}: {{")
            if isinstance(value, dict):
                result.extend(format_diff(build_diff({}, value), indent + 2))
                result.append(f"{indentation}}}")
        elif status == 'removed':
            result.append(f"{indentation}- {key}: {value}" if not isinstance(value, dict) else f"{indentation}- {key}: {{")
            if isinstance(value, dict):
<<<<<<< HEAD
                result.extend(build_diff(value, {}), indent + 2)
=======
                result.extend(format_diff(build_diff(value, {}), indent + 2))
>>>>>>> d3e7ea6bfccc6dee80c5e2e4b06bc2efcdd0485c
                result.append(f"{indentation}}}")
        elif status == 'modified':
            result.append(f"{indentation}  {key}: {{")
            result.extend(format_diff(node['children'], indent + 2))
            result.append(f"{indentation}}}")
        else:  # unchanged
            result.append(f"{indentation}  {key}: {value}")

    return result

<<<<<<< HEAD
def load_json_file(file_path):
    """Загружает данные из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Пример использования с файлами
file1_path = 'file1_r.json'
file2_path = 'file2_r.json'

# Подгружаем данные из файлов
data1 = load_json_file(file1_path)
data2 = load_json_file(file2_path)

# Получаем различия и форматируем их
diff = build_diff(data1, data2)
result = format_diff(diff)

print("{")
print("\n".join(result))
print("}")
=======
first_data = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {
            "key": "value",
            "doge": {
                "wow": ""
            }
        }
    },
    "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value"
        }
    },
    "group2": {
        "abc": 12345,
        "deep": {
            "id": 45
        }
    }
}

second_data = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": None,
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5"
        },
        "setting6": {
            "key": "value",
            "ops": "vops",
            "doge": {
                "wow": "so much"
            }
        }
    },
    "group1": {
        "foo": "bar",
        "baz": "bars",
        "nest": "str"
    },
    "group3": {
        "deep": {
            "id": {
                "number": 45
            }
        },
        "fee": 100500
    }
}

# Построение различий
diff = build_diff(first_data, second_data)

# print(diff)

# Пример использования
formatted_diff = format_diff(diff)

print("{")
print("\n".join(formatted_diff))
print("}")
>>>>>>> d3e7ea6bfccc6dee80c5e2e4b06bc2efcdd0485c
