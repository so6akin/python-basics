# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(x, y):
    return round(x ** y, 4)


print(my_func(3.5, -2))


def my_func_2(x, y):
    for _ in range(abs(y) - 1):
        x *= x
    return round(1 / x, 4)


print(my_func_2(3.5, -2))

print(f'Pow: {round(pow(3.5, -2), 4)}')