class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):  # Можно воспользоваться __len__ для нахождения истинности высказывания, но лучше использовать для таких целей __bool__
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y  # Всегда должен возвращать только True/False


p = Point(1, 0)
# print(bool(p))  # Обычно так не пишется, а пишется так, как ниже
if p:
    print("Объект р даёт True")
else:
    print("Объект р даёт False")