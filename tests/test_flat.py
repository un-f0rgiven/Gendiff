import pytest
from gendiff.flat import format_diff_lines, print_diff_lines

def test_format_diff_lines(test_file1_json, test_file2_json):
    expected_output = [
        "  - follow: false",
        "    host: hexlet.io",
        "  - proxy: 123.234.53.22",
        "  - timeout: 50",
        "  + timeout: 20",
        "  + verbose: true"
    ]

    result = format_diff_lines(test_file1_json, test_file2_json)
    assert result == expected_output
    assert isinstance(result, list)  # Проверка типа данных результата (должен быть список)

def test_print_diff_lines(test_file1_json, test_file2_json):
    expected_output = "{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"

    result = print_diff_lines(test_file1_json, test_file2_json)
    assert result == expected_output
    assert isinstance(result, str)  # Проверка типа данных результата (должна быть строка)