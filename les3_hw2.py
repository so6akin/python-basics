# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.


def func(name, surname, birth, city, email, telephone):
    name = input('Имя: ')
    surname = input('Фамилия: ')
    birth = input('Год рождения: ')
    city = input('Город проживания: ')
    email = input('Email: ')
    telephone = input('Телефон: ')
    return ' '.join([name, surname, birth, city, email, telephone])


print(func(name='Александр', surname='Собакин', birth='1992', city='Москва', email='sobakin.sun@ya.ru',
           telephone='8-926-789-88-23'))
