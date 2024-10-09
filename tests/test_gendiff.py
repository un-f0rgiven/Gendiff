import pytest
from gendiff.gendiff import generate_diff


@pytest.mark.parametrize(
    "format_name, expected_result_fixture, first_file, second_file",
    [
        ('stylish', 'stylish_format_result',
         'tests/fixtures/test_file1_r.yaml',
         'tests/fixtures/test_file2_r.yaml'),
        ('plain', 'plain_format_result',
         'tests/fixtures/test_file1_r.yaml',
         'tests/fixtures/test_file2_r.yaml'),
        ('json', 'json_format_result',
         'tests/fixtures/test_file1_r.yaml',
         'tests/fixtures/test_file2_r.yaml'),
        ('stylish', 'stylish_format_result',
         'tests/fixtures/test_file1_r.json',
         'tests/fixtures/test_file2_r.json'),
        ('plain', 'plain_format_result',
         'tests/fixtures/test_file1_r.json',
         'tests/fixtures/test_file2_r.json'),
        ('json', 'json_format_result',
         'tests/fixtures/test_file1_r.json',
         'tests/fixtures/test_file2_r.json')
    ]
)
def test_generate_diff_yaml(format_name,
                            expected_result_fixture,
                            first_file,
                            second_file,
                            request):
    expected_result = request.getfixturevalue(expected_result_fixture)
    result = generate_diff(first_file, second_file, format_name)
    assert result == expected_result
    assert type(result) is str
