def filter_by_state(operations: list, state: str = 'EXECUTED') -> list:
    result = []  # пустой список для результатов

    for operation in operations:  # перебираем словари в списке
        if operation['state'] == state:  # проверяем условие
            result.append(operation)  # добавляем подходящий словарь

    return result

