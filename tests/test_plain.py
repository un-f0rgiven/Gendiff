from gendiff.plain import format_value, format_changes, print_changes


def test_format_value():
    assert format_value({"key": "value"}) == "[complex value]"
    assert format_value(None) == "null"
    assert format_value('false') == "false"
    assert format_value('true') == "true"
    assert format_value("Hello") == "'Hello'"
    assert format_value(42) == "42"
    assert format_value(3.14) == "3.14"


def test_format_changes():
    data_added = [{'key': 'property1', 'status': 'added', 'old_value': None}]
    assert format_changes(data_added) == [
        "Property 'property1' was added with value: null"
    ]

    data_removed = [{'key': 'property1', 'status': 'removed'}]
    assert format_changes(data_removed) == ["Property 'property1' was removed"]

    data_updated = [{
        'key': 'property1',
        'status': 'updated',
        'old_value': 'old_value',
        'new_value': 'new_value'}]
    assert format_changes(data_updated) == [
        "Property 'property1' was updated. From 'old_value' to 'new_value'"
    ]

    data_unchanged = [{'key': 'property1', 'status': 'unchanged'}]

    assert format_changes(data_unchanged) == []

    # Nested properties
    nested_data = [{
        'key': 'property1',
        'status': 'added',
        'old_value': None,
        'children': [
            {
                'key': 'sub_property1',
                'status': 'updated',
                'old_value': 'old',
                'new_value': 'new'}
        ]
    }]
    assert format_changes(nested_data) == [
        "Property 'property1' was added with value: null",
        "Property 'property1.sub_property1' was updated. From 'old' to 'new'"
    ]


def test_print_changes():
    data = [
        {'key': 'property1', 'status': 'added', 'old_value': None},
        {'key': 'property2', 'status': 'removed'},
        {
            'key': 'property3',
            'status': 'updated',
            'old_value': 'old_value',
            'new_value': 'new_value'}
    ]
    expected_output = (
        "Property 'property1' was added with value: null\n"
        "Property 'property2' was removed\n"
        "Property 'property3' was updated. From 'old_value' to 'new_value'"
    )

    assert print_changes(data) == expected_output
    assert print_changes([]) == ""
