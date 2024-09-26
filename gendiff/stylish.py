from vision import build_diff
import json

def create_indentation(depth, indent_space='    ', special_symbol=' '):
    """Создает строку отступов в зависимости от уровня вложенности."""
    indentation = (indent_space * depth) + (special_symbol + ' ' if depth > 0 else '')
    return indentation

def format_node(node, depth, indent_space):
    """Рекурсивно форматирует узел и его значения с учетом вложенности."""
    result = []
    current_indentation = create_indentation(depth, indent_space)

    if isinstance(node, dict):
        for key, value in node.items():
            value_indentation = create_indentation(depth + 1, indent_space)

            if isinstance(value, dict):
                result.append(f"{value_indentation}{key}: {{")
                result.extend(format_node(value, depth + 1, indent_space))
                result.append(f"{value_indentation}}}")
            else:
                result.append(f"{value_indentation}{key}: {value}")
    
    return result

def format_diff(diff, depth=0, indent_space='    '):
    """Форматирует изменения, добавляя отступы для всех верхнеуровневых элементов со статусом 'added'."""
    result = []

    for node in diff:
        if depth == 0 and node['status'] == 'added':
            result.append(f"+ {node['key']}: {{")
            result.extend(format_node(node.get('value', {}), depth + 1, indent_space))
            result.append(f"{create_indentation(depth)}}}")

        if 'children' in node and node['children']:
            result.extend(format_diff(node['children'], depth + 1, indent_space))
        elif depth == 0 and node['status'] == 'removed':
            result.append(f"- {node['key']}: {{")
            result.extend(format_node(node.get('value', {}), depth + 1, indent_space))
            result.append(f"{create_indentation(depth)}}}")

        if 'children' in node and node['children']:
            result.extend(format_diff(node['children'], depth + 1, indent_space))

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
formatted_result = format_diff(diff)

# print(diff)
print('\n'.join(formatted_result))

# print("{")
# print("\n".join(result))
# print("}")