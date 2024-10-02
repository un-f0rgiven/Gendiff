from gendiff.stylish import format_diff
from gendiff.vision import build_diff


def test_format_diff_with_json(test_file1_r_json, test_file2_r_json):
    # Создаем разницу между двумя конфигурациями
    diff = build_diff(test_file1_r_json, test_file2_r_json)

    # Ожидаемый результат в строковом формате
    expected_result = (
        "{\n"
        "    common: {\n"
        "      + follow: false\n"
        "        setting1: Value 1\n"
        "      - setting2: 200\n"
        "      - setting3: true\n"
        "      + setting3: null\n"
        "      + setting4: blah blah\n"
        "      + setting5: {\n"
        "            key5: value5\n"
        "        }\n"
        "        setting6: {\n"
        "            doge: {\n"
        "              - wow: \n"
        "              + wow: so much\n"
        "            }\n"
        "            key: value\n"
        "          + ops: vops\n"
        "        }\n"
        "    }\n"
        "    group1: {\n"
        "      - baz: bas\n"
        "      + baz: bars\n"
        "        foo: bar\n"
        "      - nest: {\n"
        "            key: value\n"
        "        }\n"
        "      + nest: str\n"
        "    }\n"
        "  - group2: {\n"
        "        abc: 12345\n"
        "        deep: {\n"
        "            id: 45\n"
        "        }\n"
        "    }\n"
        "  + group3: {\n"
        "        deep: {\n"
        "            id: {\n"
        "                number: 45\n"
        "            }\n"
        "        }\n"
        "        fee: 100500\n"
        "    }\n"
        "}"
    )

    # Сравниваем результат функции format_diff с ожидаемым результатом
    assert format_diff(diff) == expected_result


def test_format_diff_with_yaml(test_file1_r_yaml, test_file2_r_yaml):
    # Создаем разницу между двумя конфигурациями
    diff = build_diff(test_file1_r_yaml, test_file2_r_yaml)

    # Ожидаемый результат в строковом формате
    expected_result = (
        "{\n"
        "    common: {\n"
        "      + follow: false\n"
        "        setting1: Value 1\n"
        "      - setting2: 200\n"
        "      - setting3: true\n"
        "      + setting3: null\n"
        "      + setting4: blah blah\n"
        "      + setting5: {\n"
        "            key5: value5\n"
        "        }\n"
        "        setting6: {\n"
        "            doge: {\n"
        "              - wow: \n"
        "              + wow: so much\n"
        "            }\n"
        "            key: value\n"
        "          + ops: vops\n"
        "        }\n"
        "    }\n"
        "    group1: {\n"
        "      - baz: bas\n"
        "      + baz: bars\n"
        "        foo: bar\n"
        "      - nest: {\n"
        "            key: value\n"
        "        }\n"
        "      + nest: str\n"
        "    }\n"
        "  - group2: {\n"
        "        abc: 12345\n"
        "        deep: {\n"
        "            id: 45\n"
        "        }\n"
        "    }\n"
        "  + group3: {\n"
        "        deep: {\n"
        "            id: {\n"
        "                number: 45\n"
        "            }\n"
        "        }\n"
        "        fee: 100500\n"
        "    }\n"
        "}"
    )

    # Сравниваем результат функции format_diff с ожидаемым результатом
    assert format_diff(diff) == expected_result
