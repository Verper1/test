# from accessify import private
#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = self.__y = 0
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#
#     @private
#     @classmethod
#     def check_value(cls, x):
#         return type(x) in (int, float)
#
#     def set_coord(self, x, y):
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError('ValueError')
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# pt = Point(1, 2)
# pt.set_coord(10, 20)
# print(pt.get_coord())
# # print(pt.__x)  # вызовет ошибку
# print(dir(pt))
# print(pt._Point__x)  # Так делать можно, но крайне не рекомендуется. Является обходом защиты доступа _... __...
# pt.check_value(5)  # Point.check_value() is inaccessible due to its protection level
#
# # _x = это неявная защита. __х = явная защита, которая не позволяет обратиться к атрибуту класса из вне.
#
# ---------------------------------------------------------------------------------------------------------------------
# class Example:
#     def __init__(self):
#         self.public_attr = "Я публичный атрибут"
#         self._protected_attr = "Я защищенный атрибут"
#         self.__private_attr = "Я приватный атрибут"
#
#     @property
#     def private_attr(self):
#         return self.__private_attr
#
#     @private_attr.setter
#     def private_attr(self, value):
#         self.__private_attr = value
#
# # Пример использования
# obj = Example()
# print(obj.public_attr)           # Доступен
# print(obj._protected_attr)       # Доступен, но не рекомендуется
# # print(obj.__private_attr)      # Ошибка: AttributeError
# print(obj.private_attr)          # Доступ через свойство
# obj.private_attr = "Новое значение"
# print(obj.private_attr)          # Измененное значение
#
# ---------------------------------------------------------------------------------------------------------------------

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Внесено {amount}. Новый баланс: {self.__balance}")
        else:
            print("Невозможно внести отрицательную сумму.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято {amount}. Новый баланс: {self.__balance}")
        else:
            print("Недостаточно средств или неверная сумма.")

# Пример использования
account = BankAccount("123456789", 1000)
print(account.account_number)
print(account.balance)
account.deposit(500)
account.withdraw(200)