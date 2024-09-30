def format_value(value):
    """Форматирует значение для вывода, добавляя кавычки для строк."""
    if isinstance(value, dict):
        return "[complex value]"
    elif value is None:
        return "null"
    elif value == 'false':  # Проверяем булевые значения
        return "false"  # false или true без кавычек
    elif value == 'true':  # Проверяем булевые значения
        return "true"  # false или true без кавычек
    elif isinstance(value, str):  # Проверяем строки
        return f"'{value}'"  # Оборачиваем строки в кавычки
    else:
        return str(value)  # Для других типов просто конвертируем в строку


def format_changes(data, parent_key=''):
    result = []

    for item in data:
        # Создаем путь к текущему свойству
        current_key = (
            f"{parent_key}.{item['key']}"
            if parent_key else item['key']
        )

        # Обрабатываем изменение статуса, исключая верхние уровни
        if item['status'] == 'added':
            value = item['old_value'] if item['old_value'] != 'null' else None
            result.append(
                f"Property '{current_key}' was added "
                f"with value: {format_value(value)}"
            )
        elif item['status'] == 'removed':
            result.append(f"Property '{current_key}' was removed")
        elif item['status'] == 'updated':
            old_value = (
                item['old_value'] if item['old_value'] != 'null' else None
            )
            new_value = (
                item['new_value'] if item['new_value'] != 'null' else None
            )
            if old_value != new_value:  # Проверяем, что значения отличаются
                if parent_key:  # Только если это не верхний уровень
                    result.append(
                        f"Property '{current_key}' was updated. "
                        f"From {format_value(old_value)} "
                        f"to {format_value(new_value)}"
                    )
        elif item['status'] == 'unchanged':
            continue  # Ничего не делаем для неизмененных свойств

        # Если есть вложенные свойства, рекурсивно обрабатываем их
        if item['children']:
            result.extend(format_changes(item['children'], current_key))

    return result


def print_changes(data):
    changes = format_changes(data)
    return '\n'.join(changes)
