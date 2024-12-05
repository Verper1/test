class Number:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return self.value % 2 == 0


def main():
    try:
        num = int(input("Введите число: "))
        number = Number(num)

        if number.is_even():
            print(f"{num} - четное число.")
        else:
            print(f"{num} - нечетное число.")
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")


if __name__ == '__main__':
    main()
