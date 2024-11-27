def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов

    for func in functions:
        # Вызываем каждую функцию и сохраняем результат в словарь
        results[func.__name__] = func(int_list)

    return results  # Возвращаем словарь с результатами


# Примеры использования функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))