# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

s = input('Введите строку из нескольких слов, разделенных пробелами: ')
word = list(s.split())
for ind, el in enumerate(word, 1):
    if len(el) <= 10:
        print(f'{ind} {el}')
    else:
        print(f'{ind} {el[0:10]}')
