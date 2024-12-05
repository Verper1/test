# Напишите программу, которая принимает на вход строку и определяет, является ли она палиндромом.
# Палиндром — это слово, фраза, число или другая последовательность символов, которая читается одинаково в обоих направлениях (шалаш).
# Требования:
# Программа должна игнорировать пробелы, знаки препинания и регистр символов.
# Выведите сообщение о том, является ли строка палиндромом или нет.
# Реализуйте функцию, которая будет проверять, является ли строка палиндромом.

# Пример ввода и вывода:
# Ввод: "Нажал кабан на баклажан.1"
# Вывод: "Это палиндром"
# Ввод: "Кабан"
# Вывод: "Это не палиндром"

import re
from loguru import logger


class Palindrome:
    def __init__(self):
        self.reversed_word = None
        self.request = input('Введите слово или предложение: ').lower()
        logger.info(f'{self.request}')

        self.handler()
        self.word_checker()

    def handler(self):
        self.request = ''.join(re.findall(r'[а-яА-Яa-zA-Z]', self.request))
        logger.info(f'{self.request}')
        return self.request

    def word_checker(self):
        if self.request[::-1] == self.request:
            print(f'{self.request} - Это палиндром!')
        else:
            print(f'{self.request} - Это не палиндром!')


word = Palindrome()
