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

    # Создаем сопоставление статусов и обработчиков.
    handlers = {
        'added': handle_added,
        'removed': handle_removed,
        'updated': handle_updated,
        'unchanged': lambda item, current_key: None,  # Игнорируем unchanged
    }

    for item in data:
        current_key = (
            f"{parent_key}.{item['key']}" if parent_key else item['key']
        )

        status = item['status']
        if status in handlers:
            change_message = handlers[status](item, current_key)
            # Добавляем только если change_message не равно None
            if change_message:
                result.append(change_message)

        # Если есть вложенные свойства, рекурсивно обрабатываем их
        if item.get('children'):
            result.extend(format_changes(item['children'], current_key))

    return result


def handle_added(item, current_key):
    value = item['old_value'] if item['old_value'] != 'null' else None
    return (f"Property '{current_key}' was added "
            f"with value: {format_value(value)}")


def handle_removed(item, current_key):
    return f"Property '{current_key}' was removed"


def handle_updated(item, current_key):
    old_value = item['old_value'] if item['old_value'] != 'null' else None
    new_value = item['new_value'] if item['new_value'] != 'null' else None

    if old_value != new_value:  # Проверяем, что значения отличаются
        return (f"Property '{current_key}' was updated. "
                f"From {format_value(old_value)} "
                f"to {format_value(new_value)}")
    return None  # Если нет изменений, возвращаем None


def print_changes(data):
    formatted_changes = format_changes(data)
    if formatted_changes:
        results = "\n".join(formatted_changes)  # Создаем результирующую строку
        return results  # Возвращаем результаты для использования
    return ""  # Возвращаем пустую строку, если нет изменений
