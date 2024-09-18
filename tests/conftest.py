import pytest
import json
import os

@pytest.fixture
def config_file1():
    """Загружает конфигурацию из test_file1.json."""
    config_file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'test_file1.json')
    with open(config_file_path, 'r') as f:
        data = json.load(f)
    return data

@pytest.fixture
def config_file2():
    """Загружает конфигурацию из test_file2.json."""
    config_file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'test_file2.json')
    with open(config_file_path, 'r') as f:
        data = json.load(f)
    return data