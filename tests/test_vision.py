from gendiff.vision import create_diff_node, format_value, build_diff


def test_create_diff_node():
    node = create_diff_node('key', 'added', 'old_value', 'new_value')
    assert node == {
        'key': 'key',
        'status': 'added',
        'old_value': 'old_value',
        'new_value': 'new_value',
        'children': []
    }


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value(None) == 'null'
    assert format_value(42) == 42
    assert format_value('test') == 'test'


def test_build_diff(test_file1_r_json, test_file2_r_json):
    expected_output = [
        {
            'key': 'common',
            'status': 'updated',
            'old_value': 'null',
            'new_value': 'null',
            'children': [
                {
                    'key': 'follow',
                    'status': 'added',
                    'old_value': 'false',
                    'new_value': 'null',
                    'children': []},
                {
                    'key': 'setting1',
                    'status': 'unchanged',
                    'old_value': 'Value 1',
                    'new_value': 'null',
                    'children': []},
                {
                    'key': 'setting2',
                    'status': 'removed',
                    'old_value': 200,
                    'new_value': 'null',
                    'children': []},
                {
                    'key': 'setting3',
                    'status': 'updated',
                    'old_value': 'true',
                    'new_value': 'null',
                    'children': []},
                {
                    'key': 'setting4',
                    'status': 'added',
                    'old_value': 'blah blah',
                    'new_value': 'null',
                    'children': []},
                {
                    'key': 'setting5',
                    'status': 'added',
                    'old_value': {
                        'key5': 'value5'},
                    'new_value': 'null',
                    'children': []},
                {
                    'key': 'setting6',
                    'status': 'updated',
                    'old_value': 'null',
                    'new_value': 'null',
                    'children': [
                        {
                            'key': 'doge',
                            'status': 'updated',
                            'old_value': 'null',
                            'new_value': 'null',
                            'children': [
                                {
                                    'key': 'wow',
                                    'status': 'updated',
                                    'old_value': '',
                                    'new_value': 'so much',
                                    'children': []}
                            ]},
                        {
                            'key': 'key',
                            'status': 'unchanged',
                            'old_value': 'value',
                            'new_value': 'null',
                            'children': []},
                        {
                            'key': 'ops',
                            'status': 'added',
                            'old_value': 'vops',
                            'new_value': 'null',
                            'children': []}
                    ]}
            ]},
        {
            'key': 'group1',
            'status': 'updated',
            'old_value': 'null',
            'new_value': 'null',
            'children': [
                {
                    'key': 'baz',
                    'status': 'updated',
                    'old_value': 'bas',
                    'new_value': 'bars',
                    'children': []},
                {
                    'key': 'foo',
                    'status': 'unchanged',
                    'old_value': 'bar',
                    'new_value': 'null',
                    'children': []},
                {
                    'key': 'nest',
                    'status': 'updated',
                    'old_value': {
                        'key': 'value'},
                    'new_value': 'str',
                    'children': []}
            ]},
        {
            'key': 'group2',
            'status': 'removed',
            'old_value': {
                'abc': 12345,
                'deep': {
                    'id': 45}},
            'new_value': 'null',
            'children': []},
        {
            'key': 'group3',
            'status': 'added',
            'old_value': {
                'deep': {
                    'id': {
                        'number': 45}},
                    'fee': 100500},
            'new_value': 'null',
            'children': []}
    ]

    assert build_diff(test_file1_r_json, test_file2_r_json) == expected_output
