def filter_by_state(operations: list, state: str = 'EXECUTED') -> list:
    """Функция filter_by_state принимает список словарей.
Функция возвращает новый список словарей, содержащий только те словари,
у которых ключ state соответствует указанному значению"""

    result = []  # пустой список для результатов

    for operation in operations:  # перебираем словари в списке
        if operation['state'] == state:  # проверяем условие
            result.append(operation)  # добавляем подходящий словарь

    return result

