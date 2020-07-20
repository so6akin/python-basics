# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title
        self.square = []

    @abstractmethod
    def get_square(self):
        pass

    def get_full_square(self):
        res = 0
        for el in self.square:
            res += el
        return f'Общий расход ткани: {res}'

class Coat(Clothes):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size
        self.square.append(round(self.size / 6.5 + 0.5, 2))

    @property
    def get_square(self):
        return f'Расход ткани на пальто: {round(self.size / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height
        self.square.append(round(self.height * 2 + 0.3, 2))

    @property
    def get_square(self):
        return f'Расход ткани на костюм: {round(self.height * 2 + 0.3, 2)}'


coat = Coat('Пальто', 4)
suit = Suit('Костюм', 2)
print(coat.get_square)
print(suit.get_square)



