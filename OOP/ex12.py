# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# cat = Cat('Boris')
#
# # cat  # Если этот код ввести в консоль, то эта строка выведет инфо через метод __repr__
# print(cat)  # А эта строка выведет инфо через метод __str__
# ----------------------------------------------------------------------------------------------------------------------

class Point:
    def __init__(self, *args):
        self.__coords = args


    def __len__(self):
        return len(self.__coords)


    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(1, -2, -6)
print(len(p))
print(abs(p))
