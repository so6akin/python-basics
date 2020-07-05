# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.


def divide(first_div, second_div):
    first_div = float(input('Делимое: '))
    second_div = float(input('Делитель: '))
    try:
        return f'Частное: {first_div / second_div}'
    except ZeroDivisionError:
        return 'Ошибка! На ноль делить нельзя!'


print(divide(0, 0))