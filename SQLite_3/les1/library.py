# connect_db(db_name='library.db'): Функция для создания соединения с базой данных.
#
# create_books_table(): Функция для создания таблицы books, если она не существует. Таблица должна содержать следующие столбцы:
#
# id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
# title (TEXT, NOT NULL)
# author (TEXT, NOT NULL)
# year (INTEGER, NOT NULL)
# add_book(title, author, year): Функция для добавления новой книги в таблицу. Она должна принимать параметры title, author и year.
#
# get_all_books(): Функция для получения всех книг из таблицы.
#
# delete_book(book_id): Функция для удаления книги по её id.

import sqlite3


def starting_db():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()
    return cursor, connection


def insert_book(title: str, author: str, year: int):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    connection.commit()
    connection.close()


def get_book(title):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book = cursor.fetchone()
    connection.close()
    return book
