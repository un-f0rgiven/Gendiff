import pytest
import os
from gendiff.gendiff import generate_diff


@pytest.mark.parametrize(
    "format_name, expected_result_fixture, first_file, second_file",
    [
        ('stylish', 'tests/fixtures/stylish_format_result.txt',
         'tests/fixtures/test_file1_r.yaml',
         'tests/fixtures/test_file2_r.yaml'),
        ('plain', 'tests/fixtures/plain_format_result.txt',
         'tests/fixtures/test_file1_r.yaml',
         'tests/fixtures/test_file2_r.yaml'),
        ('json', 'tests/fixtures/json_format_result.txt',
         'tests/fixtures/test_file1_r.yaml',
         'tests/fixtures/test_file2_r.yaml'),
        ('stylish', 'tests/fixtures/stylish_format_result.txt',
         'tests/fixtures/test_file1_r.json',
         'tests/fixtures/test_file2_r.json'),
        ('plain', 'tests/fixtures/plain_format_result.txt',
         'tests/fixtures/test_file1_r.json',
         'tests/fixtures/test_file2_r.json'),
        ('json', 'tests/fixtures/json_format_result.txt',
         'tests/fixtures/test_file1_r.json',
         'tests/fixtures/test_file2_r.json')
    ]
)
def test_generate_diff(format_name,
                       expected_result_fixture,
                       first_file,
                       second_file):
    with open(os.path.join(expected_result_fixture), 'r') as f:
        expected_result = f.read().strip()
    result = generate_diff(first_file, second_file, format_name)
    assert result == expected_result
    assert type(result) is str
