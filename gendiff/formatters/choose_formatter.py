from gendiff.formatters.stylish import return_stylish_format
from gendiff.formatters.plain import return_plain_format
from gendiff.formatters.json import return_json_format


def choose_formatter(format_name, diff):
    if format_name == 'stylish':
        result = return_stylish_format(diff)
    elif format_name == 'plain':
        result = return_plain_format(diff)
    elif format_name == 'json':
        result = return_json_format(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")

    return result
