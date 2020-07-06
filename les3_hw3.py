# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    minimum = min(arg1, arg2, arg3)
    if arg1 == minimum:
        return arg2 + arg3
    elif arg2 == minimum:
        return arg1 + arg3
    else:
        return arg1 + arg2


print(my_func(1, 2, 3))