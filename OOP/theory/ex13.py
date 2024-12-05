# class Geom:
#     pass
#
#
# class Line:
#     pass
#
#
# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
#
# g = Geom()
# l = Line()
# print(issubclass(Geom, Line))  # Geom не наследуется от Line, поэтому в консоли будет >>> False
# # print(issubclass(l, Line))  # Будет ошибка, так как в issubclass() нужно вводить только классы
# print(isinstance(l, object))  # Объект l является наследуемым от класса object, поэтому в консоли будет выведено >>> True
# print(isinstance(int, object))  # Класс int (и другие классы типа str, list, tuple и т.д.) является наследуемым от класса object, поэтому в консоли будет выведено >>> True
#
# v = Vector([1, 2, 3])
# print(v)  # Вывод будет таким >>> 1 2 3. Если закомментировать def __str__(self), то выведет это >>> [1, 2, 3]

# ----------------------------------------------------------------------------------------------------------------------

class Geom:
    name = 'Geom'

    # def draw(self):
    #     print('Рисование примитива')  # Переопределение, если есть метод и в родительском, и в дочернем классе. Расширение, если метод есть только в дочернем классе
    def __init__(self, x1, x2, y1, y2):
        print(f'Инициализатор для {self.__class__}')
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линий')


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2)  # Делегирование. super(). вызывает инициализатор родительского класса в дочернем классе
        print('Инициализатор Rect')
        self.fill = fill

    def draw(self):
        print('Рисование прямоугольника')


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
# print(l.__dict__)
