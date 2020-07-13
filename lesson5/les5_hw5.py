# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('hw5_numbers.txt', 'w', encoding='utf-8') as f:
    print('5 10 15 20 30', end='', file=f)

with open('hw5_numbers.txt') as f:
    num = f.read().split(' ')
    print(f'Сумма чисел: {sum(map(int, num))}')