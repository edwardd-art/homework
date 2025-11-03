def filter_by_state(operations: list, state: str = 'EXECUTED') -> list:
    """Функция filter_by_state принимает список словарей.
Функция возвращает новый список словарей, содержащий только те словари,
у которых ключ state соответствует указанному значению"""

    result = []  # пустой список для результатов

    for operation in operations:  # перебираем словари в списке
        if operation['state'] == state:  # проверяем условие
            result.append(operation)  # добавляем подходящий словарь

    return result


def sort_by_date(operations: list, reverse: bool = True) -> list:
    """
    Сортирует список операций по дате operations: список словарей с операциями
    reverse: если True (по умолчанию) - сортировка по убыванию,
    если False - по возрастанию
    Returns: Отсортированный список операций
    """

    return sorted(
        operations,
        key=lambda x: x['date'],
        reverse=reverse
    )
