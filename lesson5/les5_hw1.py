# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('hw1_user_inputs.txt', 'w', encoding='utf-8') as f:
    line = input('Введите текст для записи в файл ("пробел" - для окончания ввода): \n')
    while line:
        f.writelines(f'{line}\n')
        line = input('Введите текст: \n')
        if not line:
            break

with open('hw1_user_inputs.txt') as f:
    print(f'В файле {f.name} содержатся следующие данные:\n{f.read()}')
