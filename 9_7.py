def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Проверка, является ли результат простым числом
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result1 = sum_three(2, 3, 6)
print(result1)
result2 = sum_three(21, 12, 36)
print(result2)