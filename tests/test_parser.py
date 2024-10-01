import pytest
import os
from gendiff.parser import parse_json_file, parse_yaml_file, get_file_data

@pytest.fixture
def test_file1_json(tmp_path):
    json_data = '{"key": "value"}'
    json_file = tmp_path / "test_file1.json"
    json_file.write_text(json_data)
    return str(json_file)

@pytest.fixture
def test_file1_yaml_(tmp_path):
    yaml_data = "key: value"
    yaml_file = tmp_path / "test_file1.yaml"
    yaml_file.write_text(yaml_data)
    return str(yaml_file)

def test_parse_json_file(test_file1_json):
    # Проверяем парсинг JSON файла с использованием временного файла
    result = parse_json_file(test_file1_json)
    assert result == {"key": "value"}  # Ожидаем, что результат соответствует данным в тестовом файле

def test_parse_yaml_file(test_file1_yaml_):
    # Проверяем парсинг YAML файла с использованием временного файла
    result = parse_yaml_file(test_file1_yaml_)
    assert result == {"key": "value"}  # Ожидаем, что результат соответствует данным в тестовом файле

def test_get_file_data_json(test_file1_json):
    # Проверяем загрузку JSON данных
    result = get_file_data(test_file1_json)
    assert result == {"key": "value"}  # Проверяем, совпадает ли результат с данными из фикстуры

def test_get_file_data_yaml(test_file1_yaml_):
    # Проверяем загрузку YAML данных
    result = get_file_data(test_file1_yaml_)
    assert result == {"key": "value"}  # Проверяем, совпадает ли результат с данными из фикстуры
