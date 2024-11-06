from library2 import *
# from loguru import logger


def answer_1():
    while True:
        title = input('\nВведите название книги (от 3 символов): ')
        author = input('Введите автора книги (от 2 символов): ')
        try:
            year = int(input('Введите год издания книги: '))
        except ValueError:
            print('\nОшибка! Введите год числом!')
            continue

        if title == '' or author == '' or year == '' or len(title) < 3 or len(author) < 2:
            print('\nОшибка! Все поля должны быть заполнены и заполнены верно!')
            continue

        confirm = int(input(
            f'\nВсё ли верно?: название - {title}, автор - {author}, год - {year}. Если всё верно, то введите 1, если что-то неверно, то введите 2: '))

        if confirm == 1:
            add_book(title, author, year)
            print('\nКнига была добавлена!')
            break
        elif confirm == 2:
            pass
        else:
            print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
            continue


def answer_3():
    while True:
        answer_4()
        try:
            book_id = int(input('\nКакую книгу вы хотите удалить?(выберете книгу по id или выйдите на цифру \'0\'): '))
        except ValueError:
            print('\nОшибка! Неправльный id!')
            continue
        books = get_books()

        if book_id == 0:
            break
        elif book_id > books[-1][0] or book_id < books[0][0]:
            print('\nОшибка! Неправльный id!')
            continue

        for book in books:
            if book_id == book[0]:
                book_id = book[1]
                pass

        try:
            confirm = int(input(f'Вы хотите удалить книгу под названием {book_id}?(1 - да, 2 - нет): '))

            if confirm > 2 or confirm < 1:
                print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
                continue
            elif confirm == 1:
                delete_book(book_id)
                print('Книга была удалена')
                break
            else:
                continue
        except ValueError:
            print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
            continue


def answer_4():
    books = get_books()
    print('\nСписок книг: ')
    for book in books:
        print(book[0], book[1], book[2], book[3])


if __name__ == "__main__":
    create_db()

    while True:
        try:
            answer = int(input('\nЧто вы хотите сделать? (1 - добавить книгу, 2 - редактировать книгу, 3 - удалить книгу, 4 - просмотреть все книги, 5 - выйти из программы): '))

            if answer == 1:
                answer_1()
            elif answer == 2:
                pass
            elif answer == 3:
                answer_3()
            elif answer == 4:
                answer_4()
            elif answer == 5:
                print('\nБуду ждать Вашего возвращения! До свидания.')
                break
            else:
                print("\nОшибка! Введите одну цифру от 1 до 5 включительно.")
                continue
        except ValueError:
            print("\nОшибка! Введите одну цифру от 1 до 5 включительно.")
            continue