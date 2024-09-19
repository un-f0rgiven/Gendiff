from vision import build_diff

def format_diff(diff, indent=0):
    result = []
    for node in diff:
        key = node['key']
        status = node['status']
        value = node.get('value')
        indentation = ' ' * indent
        
        if status == 'added':
            result.append(f"{indentation}+ {key}: {value}" if not isinstance(value, dict) else f"{indentation}+ {key}: {{")
            if isinstance(value, dict):
                result.extend(format_diff(build_diff({}, value), indent + 2))
                result.append(f"{indentation}}}")
        elif status == 'removed':
            result.append(f"{indentation}- {key}: {value}" if not isinstance(value, dict) else f"{indentation}- {key}: {{")
            if isinstance(value, dict):
                result.extend(format_diff(build_diff(value, {}), indent + 2))
                result.append(f"{indentation}}}")
        elif status == 'modified':
            result.append(f"{indentation}  {key}: {{")
            result.extend(format_diff(node['children'], indent + 2))
            result.append(f"{indentation}}}")
        else:  # unchanged
            result.append(f"{indentation}  {key}: {value}")

    return result

first_data = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {
            "key": "value",
            "doge": {
                "wow": ""
            }
        }
    },
    "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value"
        }
    },
    "group2": {
        "abc": 12345,
        "deep": {
            "id": 45
        }
    }
}

second_data = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": None,
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5"
        },
        "setting6": {
            "key": "value",
            "ops": "vops",
            "doge": {
                "wow": "so much"
            }
        }
    },
    "group1": {
        "foo": "bar",
        "baz": "bars",
        "nest": "str"
    },
    "group3": {
        "deep": {
            "id": {
                "number": 45
            }
        },
        "fee": 100500
    }
}

# Построение различий
diff = build_diff(first_data, second_data)

# print(diff)

# Пример использования
formatted_diff = format_diff(diff)

print("{")
print("\n".join(formatted_diff))
print("}")