from vision import build_diff
import json

def format_diff(diff, indent=1):
    result = []
    for node in diff:
        key = node['key']
        status = node['status']
        value = node.get('value')
        indentation = '  ' * indent
        
        if status == 'added':
            result.append(f"{indentation}+ {key}: {value}" if not isinstance(value, dict) else f"{indentation}+ {key}: {{")
            if isinstance(value, dict):
                result.extend(format_diff(build_diff({}, value), indent + 2))
                result.append(f"{indentation}}}")
        elif status == 'removed':
            result.append(f"{indentation}- {key}: {value}" if not isinstance(value, dict) else f"{indentation}- {key}: {{")
            if isinstance(value, dict):
                result.extend(format_diff(build_diff(value, {}), indent + 2))
                result.append(f"{indentation}}}")
        elif status == 'modified':
            result.append(f"{indentation}  {key}: {{")
            result.extend(format_diff(node['children'], indent + 2))
            result.append(f"{indentation}}}")
        else:  # unchanged
            result.append(f"{indentation}  {key}: {value}")

    return result

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
