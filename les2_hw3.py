# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через list
month_list = int(input('Введите номер месяца: '))
seasons_list = ['зиме', 'весне', 'лету', 'осени']
if month_list == 1 or month_list == 12 or month_list == 2:
    print(f'Этот месяц относится к {seasons_list[0]}')
elif month_list == 3 or month_list == 4 or month_list == 5:
    print(f'Этот месяц относится к {seasons_list[1]}')
elif month_list == 6 or month_list == 7 or month_list == 8:
    print(f'Этот месяц относится к {seasons_list[2]}')
elif month_list == 9 or month_list == 10 or month_list == 11:
    print(f'Этот месяц относится к {seasons_list[3]}')
else:
    print('Такого месяца не существует')

# Решение через dict
month_dict = int(input('Введите номер месяца: '))
seasons_dict = {'зиме': (1, 2, 12),
                'весне': (3, 4, 5),
                'лету': (6, 7, 8),
                'осени': (9, 10, 11)}
if 0 < month_dict < 13:
    for key in seasons_dict.keys():
        if month_dict in seasons_dict[key]:
            print(f'Этот месяц относится к {key}')
else:
    print('Такого месяца не существует')
