from gendiff.parser import get_file_data
from gendiff.diff import build_diff
from gendiff.formatters.choose_formatter import choose_formatter


def generate_diff(first_file, second_file, format_name='stylish'):
    first_data = get_file_data(first_file)
    second_data = get_file_data(second_file)

    diff = build_diff(first_data, second_data)

    result = choose_formatter(format_name, diff)

    return result
