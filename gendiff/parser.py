import yaml
import json
import os


def parse_json_file(file_path):
    """Парсит JSON файл и возвращает словарь."""
    with open(file_path, 'r') as file:
        return json.load(file)


def parse_yaml_file(file_path):
    """Парсит YAML файл и возвращает словарь."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def get_file_data(file_path):
    ext = os.path.splitext(file_path)[1]
    if ext == '.json':
        return parse_json_file(file_path)
    else:
        return parse_yaml_file(file_path)
