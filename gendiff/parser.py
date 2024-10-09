import yaml
import json
import os


def parse_json(data):
    return json.loads(data)


def parse_yaml(data):
    return yaml.safe_load(data)


def parse_file_content(file_extension, content):
    if file_extension == '.json':
        return parse_json(content)
    elif file_extension == '.yaml' or file_extension == '.yml':
        return parse_yaml(content)
    else:
        raise ValueError(f"Неподдерживаемое расширение файла: {file_extension}")


def get_file_data(file_path):
    ext = os.path.splitext(file_path)[1]
    with open(file_path, 'r') as file:
        content = file.read()
    return parse_file_content(ext, content)
