class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print("__getattr__: " + item)
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)
        print('__delattr__')


pt1 = Point(1, 2)
print(pt1.a)  # (__getattr__)
print(pt1.MAX_COORD)
pt1.a = 10
print(pt1.a)
del pt1.a  # (__delattr__)
print(pt1.a)
print(pt1.__dict__)
# a = pt1.x
# print(a)  # ValueError: Private attribute (__getattribute__)
# pt1.z = 10  # AttributeError: недопустимое имя атрибута (__setattr__)


# __setattr__(self, key, value)__ – автоматически вызывается при изменении свойства key класса;
# __getattribute__(self, item) – автоматически вызывается при получении свойства класса с именем item;
# __getattr__(self, item) – автоматически вызывается при получении несуществующего свойства item класса;
# __delattr__(self, item) – автоматически вызывается при удалении свойства item (не важно: существует оно или нет).