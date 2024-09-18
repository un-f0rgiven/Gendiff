import yaml
import json


def parse_json_file(file_path):
    """Парсит JSON файл и возвращает словарь."""
    with open(file_path, 'r') as file:
        return json.load(file)


def parse_yaml_file(file_path):
    """Парсит YAML файл и возвращает словарь."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
