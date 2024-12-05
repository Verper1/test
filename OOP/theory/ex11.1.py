class UserAccount:
    def __init__(self):
        self.username = 'Mary'
        self.email = '1111@example.com'
        self.__password = '1234'
        self.old_password = ''

    def set_password(self, password):
        self.old_password = self.__password
        self.__password = password
        return self.__password, self.old_password


    def check_password(self):
        if self.old_password == self.__password:
            return True
        else:
            return False


# Создаём объект класса UserAccount под названием user
user = UserAccount()
print(user.__dict__)

# Изменяем пароль self.__password и сохраняем старый self.old_password
user.set_password('5678')
print(user.__dict__)

# Проверка нового пароля на соответствие старому
print(user.check_password())

# Изменяем пароль self.new_password и сохраняем старый self.old_password
user.set_password('9012')
print(user.__dict__)

# Проверка нового пароля на соответствие старому
print(user.check_password())

# Изменяем пароль self.new_password и сохраняем старый self.old_password
user.set_password('9012')
print(user.__dict__)

# Проверка нового пароля на соответствие старому
print(user.check_password())
