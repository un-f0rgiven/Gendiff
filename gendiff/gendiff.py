import argparse
import os
from gendiff.parser import parse_json_file, parse_yaml_file
from gendiff.stylish import format_diff
from gendiff.vision import build_diff
from gendiff.plain import print_changes
from gendiff.json import print_changes_json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_file_data(file_path):
    ext = os.path.splitext(file_path)[1]
    if ext == '.json':
        return parse_json_file(file_path)
    else:
        return parse_yaml_file(file_path)


def format_diff_lines(all_keys, first_data, second_data):
    diff_lines = []
    for key in all_keys:
        first_value = first_data.get(key)
        second_value = second_data.get(key)
        formatted_first_value = format_value(first_value)
        formatted_second_value = format_value(second_value)

        if key not in first_data:
            diff_lines.append(f"+ {key}: {formatted_second_value}")
        elif key not in second_data:
            diff_lines.append(f"- {key}: {formatted_first_value}")
        elif formatted_first_value != formatted_second_value:
            diff_lines.append(f"- {key}: {formatted_first_value}")
            diff_lines.append(f"+ {key}: {formatted_second_value}")
        else:
            diff_lines.append(f" {key}: {formatted_first_value}")

    return diff_lines


def generate_diff(first_file, second_file, format_name='stylish'):
    first_data = get_file_data(first_file)
    second_data = get_file_data(second_file)
    # all_keys = sorted(first_data.keys() | second_data.keys())
    diff = build_diff(first_data, second_data)

    if format_name == 'stylish':
        result = format_diff(diff)  # Используем функцию для стильного формата
    elif format_name == 'plain':
        result = print_changes(diff)
    elif format_name == 'json':
        result = print_changes_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # Позиционные аргументы
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Необязательный аргумент (установим формат по умолчанию на 'stylish')
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output'
    )

    # Парсинг аргументов
    args = parser.parse_args()

    diffs = generate_diff(
        args.first_file, args.second_file, format_name=args.format
    )

    # Формируем и выводим результат
    print(diffs)


if __name__ == '__main__':
    main()
