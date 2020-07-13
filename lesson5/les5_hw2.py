# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('hw2_count.txt', 'w') as f:
    print('один', file=f)
    print('два слова', file=f)
    print('три слова три', file=f)

with open('hw2_count.txt') as f:
    content = f.readlines()
    print(f'Количество строк: {len(content)}')
    print(f'Количество слов построчно:')
    for words in content:
        print(f'{len(words.split())}')
