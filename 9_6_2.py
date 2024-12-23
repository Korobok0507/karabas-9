def all_variants(text):
    length = len(text)
    # Перебираем длину подпоследовательностей от 1 до length
    for sub_length in range(1, length + 1):
        # Перебираем начальные индексы для каждой длины подпоследовательности
        for start in range(length - sub_length + 1):
            yield text[start:start + sub_length]  # Возвращаем подпоследовательность

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)