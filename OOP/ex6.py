class Vector:
    MIN_COORDS = 0
    MAX_COOEDS = 100

    @classmethod
    def validate(cls, arg):  # cls означает, что обращение идёт к атрибутам класса (MIN_COORDS, MAX_COOEDS). Работа с локальными свойствами экземпляра класса не получится, так как нет ссылка на экхемпляр.
        return cls.MIN_COORDS <= arg <= cls.MAX_COOEDS

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and Vector.validate(y):  # Но лучше прописывать на месте имени класса self в методе
            self.x = x
            self.y = y

            print(self.norm2(self.x, self.y))

    def get_coords(self):
        return self.x, self.y

    @staticmethod  # Работает независимо от класса и не обращается к информации внутри класса.
    def norm2(x, y):
        return x*x + y*y


v = Vector(3, 2)

print(Vector.validate(5))
print(Vector.norm2(2, 3))
res = Vector.get_coords(v)
print(res)

# Из этого урока я понял:
#
# -- То что self мы используем в методах, когда собираемся создавать и работать непосредственно с экземлярами класса
# -- @classmethod когда работаем ТОЛЬКО внутри самого класса
# -- А @staticmethod только когда нам нужен независимый метод, который не будет, и не должен обращаться к локальным, и к любым другим атрибутам, и переменным