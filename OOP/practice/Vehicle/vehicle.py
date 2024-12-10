class Vehicle:
    def __init__(self):
        self.__gas = 0
        self.__speed = 0

    @property
    def gas(self):
        return self.__gas

    @gas.setter
    def gas(self, amount):
        self.__gas += amount

    @property
    def speed(self):
        return self.__speed

    def change_speed(self, new_speed):
        if self.__gas <= 0:
            print('Нет топлива!')
        else:
            self.__speed = new_speed
            # print(f'Скорость установлена на {new_speed}')


class Car(Vehicle):
    def __init__(self, doors):
        super().__init__()
        self.doors = doors

    def change_speed(self, new_speed):
        super().change_speed(new_speed)  # Вызов метода родительского класса
        if self.gas > 0:
            fuel_consumption = new_speed * 20 / self.gas
            print(f'Расход топлива составляет: {fuel_consumption}')

class Bicycle(Vehicle):
    def __init__(self, time, type_bicycle):
        super().__init__()
        self.time = time
        self.type_bicycle = type_bicycle

    def change_speed(self, new_speed):
        if self.time <= 0:
            print('Вы не начали заниматься!')
        else:
            super().change_speed(new_speed)  # Вызов метода родительского класса
            adjusted_speed = new_speed / 2.5
            print(f'Скорость установлена на {adjusted_speed}. Вы занимаетесь уже: {self.time}, поэтому скорость снижена!')


# Создание экземпляров классов
car = Car(4)  # Автомобиль с 4 дверями
bicycle = Bicycle(30, "горный")  # Велосипед, занимаемся 30 минут, горный тип

# Тестирование заправки и изменения скорости для автомобиля
print("Тестирование автомобиля:")
car.gas = 10  # Заправка 10 литров
print(f"Топливо в автомобиле: {car.gas} литров")

car.change_speed(60)  # Установка скорости 60
car.change_speed(80)  # Установка скорости 80

# Попробуем установить скорость без топлива
car.gas = 0  # Убираем топливо
car.change_speed(50)  # Попытка установить скорость 50

# Тестирование заправки и изменения скорости для велосипеда
print("\nТестирование велосипеда:")
bicycle.change_speed(20)  # Установка скорости 20

# Попробуем установить скорость, когда не занимаемся
bicycle.time = 0  # Устанавливаем время занятия в 0
bicycle.change_speed(15)  # Попытка установить скорость 15

# Увеличим время занятия и изменим скорость
bicycle.time = 30  # Устанавливаем время занятия в 30 минут
bicycle.change_speed(25)  # Установка скорости 25
