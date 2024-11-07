from library2 import *
# from loguru import logger


def adding_book():
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
            break
        elif confirm == 2:
            pass
        else:
            print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
            continue


def changing_book():
    while True:
        all_books()
        try:
            book_id = int(input('\nКакую книгу вы хотите изменить?(выберете книгу по id или выйдите на цифру \'0\'): '))
            book_title = ''
        except ValueError:
            print('\nОшибка! Неправльный id!')
            continue
        books = get_books()

        if book_id == 0:
            break
        elif book_id > books[-1][0] or book_id < books[0][0]:
            print('\nОшибка! Неправильный id!')
            continue

        for book in books:
            if book_id == book[0]:
                book_title = book[1]
                break

        try:
            confirm = int(input(f'Вы хотите изменить книгу под названием {book_title}?(1 - да, 2 - нет): '))

            if confirm > 2 or confirm < 1:
                print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
                continue
            elif confirm == 1:
                while True:
                    new_title = input('\nВведите название книги (от 3 символов): ')
                    new_author = input('Введите автора книги (от 2 символов): ')
                    try:
                        new_year = int(input('Введите год издания книги: '))
                    except ValueError:
                        print('\nОшибка! Введите год числом!')
                        continue

                    if new_title == '' or new_author == '' or new_year == '' or len(new_title) < 3 or len(new_author) < 2:
                        print('\nОшибка! Все поля должны быть заполнены и заполнены верно!')
                        continue

                    confirm_changing = int(input(f'\nВсё ли верно?: название - {new_title}, автор - {new_author}, год - {new_year}. Если всё верно, то введите 1, если что-то неверно, то введите 2: '))

                    if confirm_changing == 1:
                        change_book(new_title, new_author, new_year, book_id)
                        break
                    elif confirm_changing == 2:
                        pass
                    else:
                        print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
                        continue
                break
            else:
                continue
        except ValueError:
            print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
            continue


def deleting_book():
    while True:
        all_books()
        try:
            book_id = int(input('\nКакую книгу вы хотите удалить?(выберете книгу по id или выйдите на цифру \'0\'): '))
        except ValueError:
            print('\nОшибка! Неправильный id!')
            continue
        books = get_books()

        if book_id == 0:
            break
        elif book_id > books[-1][0] or book_id < books[0][0]:
            print('\nОшибка! Неправильный id!')
            continue

        for book in books:
            if book_id == book[0]:
                book_id = book[1]

        try:
            confirm = int(input(f'Вы хотите удалить книгу под названием {book_id}?(1 - да, 2 - нет): '))

            if confirm > 2 or confirm < 1:
                print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
                continue
            elif confirm == 1:
                delete_book(book_id)
                break
            else:
                continue
        except ValueError:
            print("\nОшибка! Введите одну цифру от 1 до 2 включительно.")
            continue


def all_books():
    books = get_books()
    print('\nСписок книг: ')

    if len(books) != 0:
        for book in books:
            print(f'| id: {book[0]} | Название: {book[1]} | Автор: {book[2]} | Год издания: {book[3]} |')
    else:
        print('У вас нет сохранённых книг в библиотеке.')

def main():
    create_db()

    while True:
        try:
            all_books()
            answer = int(input('\nЧто вы хотите сделать? (1 - добавить книгу, 2 - редактировать книгу, 3 - удалить книгу, 4 - просмотреть все книги, 5 - выйти из программы): '))

            if answer == 1:
                adding_book()
            elif answer == 2:
                changing_book()
            elif answer == 3:
                deleting_book()
            elif answer == 4:
                all_books()
            elif answer == 5:
                print('\nБуду ждать Вашего возвращения! До свидания.')
                break
            else:
                print("\nОшибка! Введите одну цифру от 1 до 5 включительно.")
                continue
        except ValueError:
            print("\nОшибка! Введите одну цифру от 1 до 5 включительно.")
            continue
