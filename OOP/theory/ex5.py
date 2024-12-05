# class Ex5:
#     def __init__(self, value):
#         self.value = value
#
#     def cube(self):
#         return self.value ** 3
#
#
# def main():
#     num = int(input("Введите число, которое хотите возвести в куб: "))
#     answer = Ex5(num).cube()
#     print(f'Куб числа {num} равен {answer}')
#
#
# if __name__ == '__main__':
#     main()
#
# ---------------------------------------------------------------------------------------------------------------------

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные с БД'

    def write(self, data):
        print(f'Запись в БД {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2), '\n')
db.connect()
db2.connect()
