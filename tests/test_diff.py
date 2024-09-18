import pytest
from tests.conftest import config_file1, config_file2, config_file_yaml1, config_file_yaml2  # Фикстуры
from gendiff.gendiff import generate_diff  # Импортируйте свою функцию

def test_generate_diff(config_file1, config_file2):
    expected_diff = "{\n" \
                    "- follow: false\n" \
                    "  host: hexlet.io\n" \
                    "- proxy: 123.234.53.22\n" \
                    "- timeout: 50\n" \
                    "+ timeout: 20\n" \
                    "+ verbose: true\n" \
                    "}"
    
    # Записываем временные файлы для запуска функции
    first_file_path = 'tests/fixtures/test_file1.json'
    second_file_path = 'tests/fixtures/test_file2.json'
    
    # Получаем результат функции
    result = generate_diff(first_file_path, second_file_path)
    
    assert result == expected_diff


def test_generate_diff_yaml(config_file_yaml1, config_file_yaml2):
    expected_diff = "{\n" \
                    "- follow: false\n" \
                    "  host: hexlet.io\n" \
                    "- proxy: 123.234.53.22\n" \
                    "- timeout: 50\n" \
                    "+ timeout: 20\n" \
                    "+ verbose: true\n" \
                    "}"
    
    first_file_path = 'tests/fixtures/test_file1.yaml'
    second_file_path = 'tests/fixtures/test_file2.yaml'
    
    result = generate_diff(first_file_path, second_file_path)
    
    assert result == expected_diff