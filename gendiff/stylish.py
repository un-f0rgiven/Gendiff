from vision import build_diff
import json


def create_indentation(depth, indent_space=4, displacement=2):
    """Создает строку отступов в зависимости от уровня вложенности."""
    indentation = depth * indent_space - displacement
    return ' ' * indentation

def format_value(node, depth): 
    result = ""

    if isinstance(node, dict):
        for key, value in node.items():
            value_indentation = create_indentation(depth + 1)

            if isinstance(value, dict):
                result += f"{value_indentation}{key}: {{\n"
                result += format_value(value, depth + 1)
                result += f"{value_indentation}}}\n"
            else:
                result += f"{value_indentation}{key}: {value}\n"

    return result

def format_children(children, depth):
    """Форматирует детей узла и возвращает строку с результатом."""
    result = ""

    for child in children:
        if child['status'] == 'added':
            result += f"{create_indentation(depth)}+ {child['key']}: "
            if isinstance(child['value'], dict):
                result += "{\n"
                result += format_value(child['value'], depth + 1)
                result += f"{create_indentation(depth)} }}\n"  # Добавил перенос строки здесь
            else:
                result += f"{child['value']}\n"
        elif child['status'] == 'removed':
            result += f"{create_indentation(depth)}- {child['key']}: "
            if isinstance(child['value'], dict):
                result += "{\n"
                result += format_value(child['value'], depth + 1)
                result += f"{create_indentation(depth)} }}\n"  # Добавил перенос строки здесь
            else:
                result += f"{child['value']}\n"
        elif child['status'] == 'unchanged':
            result += f"{create_indentation(depth)}  {child['key']}: "
            if isinstance(child['value'], dict):
                result += "{\n"
                result += format_value(child['value'], depth + 1)
                result += f"{create_indentation(depth)} }}\n"  # Добавил перенос строки здесь
            else:
                result += f"{child['value']}\n"
        elif child['status'] == 'modified':
            result += f"{create_indentation(depth)}  {child['key']}: {{\n"
            result += format_children(child['children'], depth + 1)
            result += f"{create_indentation(depth)} }}\n"  # Добавил перенос строки здесь

    return result

def format_diff(diff, depth=0, indent_space=4, displacement=2):
    result = ""
    
    for node in diff:
        if node['status'] == 'added':
            result += f"{create_indentation(depth)}+ {node['key']}: {{\n"
            result += format_value(node['value'], depth + 1)
            result += f"{create_indentation(depth)}}}\n"
        elif node['status'] == 'removed':
            result += f"{create_indentation(depth)}- {node['key']}: {{\n"
            result += format_value(node['value'], depth + 1)
            result += f"{create_indentation(depth)}}}\n"
        elif node['status'] == 'unchanged':
            result += f"{create_indentation(depth)}  {node['key']}: {{\n"
            result += format_value(node['value'], depth + 1)
            result += f"{create_indentation(depth)}}}\n"
        elif node['status'] == 'modified':
            result += f"{create_indentation(depth)}  {node['key']}: {{\n"
            result += format_children(node['children'], depth + 1)
            result += f"{create_indentation(depth)}}}\n"
    
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

print(f'{{\n{formatted_result}}}')