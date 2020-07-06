# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_sum():
    sum = 0
    exit = False
    while not exit:
        number = input("Введите числа, разделенные пробелом (для выхода нажмите 'Q'): ").split()
        res = 0
        for i in range(len(number)):
            if number[i].upper() == 'Q':
                exit = True
                break
            else:
                res += int(number[i])
        sum += res
        print(f'Текущая сумма равна {sum}')
    print(f'Общая сумма равна {sum}')


my_sum()
