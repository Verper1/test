# Создайте класс Triangle, который будет представлять треугольник. Этот класс должен иметь следующие методы и свойства:
# Конструктор (__init__): принимает три параметра - side_a, side_b и side_c (длины сторон треугольника).
# Метод is_valid: проверяет, является ли треугольник допустимым (сумма длин любых двух сторон должна быть больше длины третьей стороны).

# Метод area: возвращает площадь треугольника, используя формулу Герона:
# Полупериметр: p2 = self.side_a + self.side_b + self.side_c / 2
# Площадь: s = sqrt(p2 * (p2 - self.side_a) * (p2 - self.side_b) * (p2 - self.side_c))

# Метод perimeter: возвращает периметр треугольника (сумму всех сторон).
# Метод display: выводит информацию о треугольнике (длины сторон, периметр и площадь).

# Вывод:
# Сторона A: 3
# Сторона B: 4
# Сторона C: 5
# Периметр: 12
# Площадь: 6.0

from math import sqrt
# from loguru import logger


class Triangle:
    def __init__(self):
        self.side_a = int(input('Введите первую сторону треугольника: '))
        self.side_b = int(input('Введите вторую сторону треугольника: '))
        self.side_c = int(input('Введите третью сторону треугольника: '))
        self.s = None
        self.p = None

        if self.is_valid() is False:
            print('Треугольник не существует!')
        else:
            self.area()
            self.perimeter()
            self.display()

    def is_valid(self):
        if self.side_a + self.side_b <= self.side_c or self.side_c + self.side_b <= self.side_a or \
        self.side_c + self.side_a <= self.side_b:
            return False

    def area(self):
        p2 = self.side_a + self.side_b + self.side_c / 2
        self.s = sqrt(p2 * (p2 - self.side_a) * (p2 - self.side_b) * (p2 - self.side_c))
        return self.s

    def perimeter(self):
        self.p = self.side_a + self.side_b + self.side_c
        return self.p

    def display(self):
        print(f'Первая сторона треугольника: {self.side_a}'
              f'\nВторая сторона треугольника: {self.side_b}'
              f'\nТретья сторона треугольника: {self.side_c}'
              f'\nПериметр: {self.s}'
              f'\nПлощадь: {self.p}')


t1 = Triangle()
