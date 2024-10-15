def create_diff_node(
        key,
        status,
        old_value=None,
        new_value=None,
        children=None
):
    # Определяет функцию для создания узла разницы с указанными параметрами:
    # key - ключ, status - статус изменения, old_value - старое значение,
    # new_value - новое значение, children - дочерние узлы (по умолчанию None).

    if children is None:
        # Если параметр children не был передан (значение None),
        # присваиваем ему пустой список.
        children = []

    return {
        # Возвращает словарь,
        # представляющий узел разницы с указанными значениями.
        'key': key,              # Ключ элемента.

        'status': status,        # Статус изменения.
        'old_value': old_value,  # Старое значение.
        'new_value': new_value,  # Новое значение.
        'children': children      # Дочерние узлы, если они есть.
    }


def build_diff(file1, file2):
    # Определяет функцию для построения разницы между двумя файлами.

    diff = []  # Инициализирует список для хранения узлов разницы.

    # Создает множество всех ключей из обоих файлов и сортирует его.
    all_keys = sorted(set(file1.keys()).union(file2.keys()))

    # Проходим по каждому ключу из объединенного списка ключей.
    for key in all_keys:
        # Получаем значения по текущему ключу из обоих файлов.
        value1 = file1.get(key)  # Значение из первого файла.
        value2 = file2.get(key)  # Значение из второго файла.

        # Проверка на наличие ключа только в первом файле (удаленный элемент).
        if key in file1 and key not in file2:
            diff.append(create_diff_node(key, 'removed', value1))

        # Проверка на наличие ключа только во втором файле (новый элемент).
        elif key not in file1 and key in file2:
            diff.append(create_diff_node(key, 'added', value2))

        # Проверка на равенство значений (неизмененный элемент).
        elif value1 == value2:
            diff.append(create_diff_node(key, 'unchanged', value1))

        # Проверка на то, что значения являются словарями (вложенные различия).
        elif isinstance(value1, dict) and isinstance(value2, dict):
            child_diff = build_diff(value1, value2)
            # Рекурсивно вызываем build_diff для вложенных словарей.
            diff.append(create_diff_node(key, 'nested', children=child_diff))
            # Добавляем узел с дочерними элементами.

        # Обработка случая, когда значение изменилось.
        else:
            diff.append(create_diff_node(key, 'updated', value1, value2))

    return diff  # Возвращает список узлов разницы.
