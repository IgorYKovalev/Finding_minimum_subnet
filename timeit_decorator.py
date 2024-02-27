import time


def timeit(func):
    """
    Декоратор для измерения времени выполнения функции.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время перед выполнением функции
        result = func(*args, **kwargs)  # Вызываем функцию
        end_time = time.time()  # Засекаем время после выполнения функции
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.8f} секунд.")
        return result
    return wrapper
