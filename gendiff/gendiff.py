import argparse
import json


def parse_json_file(file_path):
    """Парсит JSON файл и возвращает словарь."""
    with open(file_path, 'r') as file:
        return json.load(file)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(first_file, second_file):
    """Функция для сравнения двух JSON файлов и вывода различий."""
    first_data = parse_json_file(first_file)
    second_data = parse_json_file(second_file)

    # Объединяем ключи из обоих файлов и сортируем их в алфавитном порядке
    all_keys = sorted(first_data.keys() | second_data.keys())

    diff_lines = []

    for key in all_keys:
        first_value = first_data.get(key)
        second_value = second_data.get(key)

        # Применяем форматирование для значений
        formatted_first_value = format_value(first_value)
        formatted_second_value = format_value(second_value)

        # Если значение отсутствует в первом файле
        if key not in first_data:
            diff_lines.append(f"+ {key}: {formatted_second_value}")
        # Если значение отсутствует во втором файле
        elif key not in second_data:
            diff_lines.append(f"- {key}: {formatted_first_value}")
        # Если значения различаются
        elif formatted_first_value != formatted_second_value:
            diff_lines.append(f"- {key}: {formatted_first_value}")
            diff_lines.append(f"+ {key}: {formatted_second_value}")
        # Если значения совпадают
        else:
            diff_lines.append(f"  {key}: {formatted_first_value}")

    # Собираем результат в фигурные скобки
    result = "{\n" + "\n".join(diff_lines) + "\n}"
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # Позиционные аргументы
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Необязательный аргумент
    parser.add_argument('-f', '--format',
                        default='plain', help='set format of output')

    # Парсинг аргументов
    args = parser.parse_args()

    diffs = generate_diff(args.first_file, args.second_file)

    # Формируем и выводим результат
    print(diffs)


if __name__ == '__main__':
    main()
