import argparse
import os
from gendiff.parser import parse_json_file, parse_yaml_file


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
            diff_lines.append(f"  {key}: {formatted_first_value}")

    return diff_lines


def generate_diff(first_file, second_file):
    first_data = get_file_data(first_file)
    second_data = get_file_data(second_file)

    all_keys = sorted(first_data.keys() | second_data.keys())
    diff_lines = format_diff_lines(all_keys, first_data, second_data)

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
