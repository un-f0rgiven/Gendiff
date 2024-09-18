import pytest

def test_config_file1_values(config_file1):
    assert config_file1["host"] == "hexlet.io"
    assert config_file1["timeout"] == 50
    assert config_file1["proxy"] == "123.234.53.22"
    assert config_file1["follow"] is False

def test_config_file2_values(config_file2):
    assert config_file2["host"] == "hexlet.io"
    assert config_file2["timeout"] == 20
    assert config_file2["verbose"] is True

def test_combined_config(config_file1, config_file2):
    expected_combined_config = {
        "host": "hexlet.io",
        "timeout": 20,  # поскольку "timeout" из config_file2 должен переопределить значение из config_file1
        "proxy": "123.234.53.22",
        "follow": False,
        "verbose": True
    }

    # Объединение двух конфигураций
    combined_config = {**config_file1, **config_file2}
    assert combined_config == expected_combined_config