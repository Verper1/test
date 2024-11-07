import sqlite3


def create_db():
    connection = sqlite3.connect('library2.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def add_book(title: str, author: str, year: int):
    connection = sqlite3.connect('library2.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books2 (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    print(f"\nКнига с названием - '{title}', автором - '{author}' и годом издания - '{year}' успешно добавлена.")

    connection.commit()
    connection.close()


def get_books():
    connection = sqlite3.connect('library2.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books2')
    books = cursor.fetchall()

    connection.close()
    return books


def change_book(new_title: str, new_author: str, new_year: int, book_id: int):
    connection = sqlite3.connect('library2.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books2 SET title = ?, author = ?, year = ? WHERE id = ?', (new_title, new_author, new_year, book_id))
    print(f"\nКнига с ID {book_id} успешно обновлена.")

    connection.commit()
    connection.close()


def delete_book(book_id: int):
    connection = sqlite3.connect('library2.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books2 WHERE id = ?',(book_id,))
    print(f"\nКнига с ID {book_id} успешно удалена.")

    connection.commit()
    connection.close()
