# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'{self.name} находится в движении.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'{self.name} повернула {direction}.'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км/ч.'


class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed} км/ч.')
        if self.speed > 60:
            print(f'{self.name} превышает максимально допустимую скорость для города.')


class SportCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed} км/ч.')
        if self.speed > 40:
            print(f'{self.name} превышает максимально допустимую скорость для рабочей машины.')


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


volkswagen = TownCar('Volkswagen', 'Коричневый', 80, False)
ferrari = SportCar('Ferrari', 'Красный', 100, False)
toyota = WorkCar('Toyota', 'Черный', 40, False)
skoda = PoliceCar('Skoda', 'Синий', 70, True)

print(volkswagen.go())
print(ferrari.go())
print(toyota.go())
print(skoda.go())

print(volkswagen.turn('налево'))
print(ferrari.turn('направо'))
print(toyota.turn('назад'))
print(skoda.turn('налево'))

volkswagen.show_speed()
print(ferrari.show_speed())
toyota.show_speed()
print(skoda.show_speed())

print(volkswagen.stop())
print(ferrari.stop())
print(toyota.stop())
print(skoda.stop())

print(f'Цвет {ferrari.name} - {ferrari.color}.')
print(f'{toyota.name} - полицейская машина? {toyota.is_police}.')
print(f'{skoda.name} - полицейская машина? {skoda.is_police}.')