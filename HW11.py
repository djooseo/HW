"""
Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
Наповніть класи атрибутами та методами на свій розсуд.

Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель". Виведіть на екран значення атрибутів обʼєктів
"""


class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def introduce_yourself(self):
        message = f'Hi, I\'m a {self.brand}, my model is {self.model} and I was released in {self.year}.'
        return message


class Car(Transport):
    pass


class Aircraft(Transport):
    pass


class Ship(Transport):
    pass


my_car = Car('Porsche', '911 GT3 RS', 2016)
my_aircraft = Aircraft('Lockheed Martin', 'SR-71 "Blackbird"', 1966)
my_ship = Ship('Newport News Shipbuilding', 'USS Gerald R. Ford', 2017)

print(my_car.introduce_yourself())
print(my_aircraft.introduce_yourself())
print(my_ship.introduce_yourself())
