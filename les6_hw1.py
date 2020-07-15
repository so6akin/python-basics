# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self):
        с = 1
        for el in cycle(self.__color):
            if с > 6:
                break
            if el in 'red':
                print(el)
                sleep(7)
            elif el in 'yellow':
                print(el)
                sleep(2)
            else:
                print(el)
                sleep(4)
            с += 1


t = TrafficLight()
t.running()
