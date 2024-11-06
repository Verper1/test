from library import starting_db, insert_book, get_book


starting_db()

title = input('Введите название книги: ')
author = input('Введите автора книги: ')
year = int(input('Введите год издания книги: '))

insert_book(title, author, year)
book = input('Какую книгу вы хотите увидеть?: ')

print(get_book(book))
