import argparse
from gendiff.parser import get_file_data
from gendiff.flat import print_diff_lines
from gendiff.stylish import format_diff
from gendiff.vision import build_diff
from gendiff.plain import print_changes
from gendiff.json import print_changes_json
# from gendiff.test import test_diff


def generate_diff(first_file, second_file, format_name='stylish'):
    first_data = get_file_data(first_file)
    second_data = get_file_data(second_file)

    diff = build_diff(first_data, second_data)

    if format_name == 'stylish':
        result = format_diff(diff)
    # elif format_name == 'test': # тестовый вывод
    #     result = test_diff(diff)
    elif format_name == 'plain':
        result = print_changes(diff)
    elif format_name == 'json':
        result = print_changes_json(diff)
    elif format_name == 'flat':
        result = print_diff_lines(first_data, second_data)
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
