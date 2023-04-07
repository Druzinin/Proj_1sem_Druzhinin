import sqlite3 as sq
from data import *

with sq.connect('Library.sqlite') as con:
    con.execute("PRAGMA foreign_keys = ON;")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS author_book;")
    cur.execute("DROP TABLE IF EXISTS authors;")
    cur.execute("DROP TABLE IF EXISTS books;")
    cur.execute("DROP TABLE IF EXISTS sections;")
    cur.execute("DROP TABLE IF EXISTS publishing;")

    cur.execute("""CREATE TABLE IF NOT EXISTS authors (
    id_author INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS books (
    id_books INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    year_publishing INTEGER,
    storage TEXT,
    id_section INTEGER
    REFERENCES sections ON DELETE CASCADE ON UPDATE CASCADE,
    id_publish INTEGER
    REFERENCES publishing ON DELETE CASCADE ON UPDATE CASCADE
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sections (
    id_section INTEGER PRIMARY KEY AUTOINCREMENT,
    section TEXT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS publishing (
    id_publish INTEGER PRIMARY KEY AUTOINCREMENT,
    publish TEXT,
    city TEXT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS author_book (
    id_author_book INTEGER PRIMARY KEY AUTOINCREMENT,
    id_book INTEGER
    REFERENCES books ON DELETE CASCADE ON UPDATE CASCADE,
    id_author INTEGER
    REFERENCES authors ON DELETE CASCADE ON UPDATE CASCADE
    );""")

with sq.connect('Library.sqlite') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO authors (surname, name) VALUES (?, ?);", info_authors)
    cur.executemany("INSERT INTO sections (section) VALUES (?)", info_sections)
    cur.executemany("INSERT INTO publishing (publish, city) VALUES (?, ?)", info_publishing)
    cur.executemany("INSERT INTO author_book (id_book, id_author) VALUES (?, ?)", info_author_book)
    cur.executemany("INSERT INTO books (name, year_publishing, storage, id_section, id_publish)"
                    "VALUES (?, ?, ?, ?, ?)", info_books)

# SELECTS
# with sq.connect('Library.sqlite') as con:
#     cur = con.cursor()
#
#     print('\n1.')
#     for row in cur.execute("SELECT name, year_publishing FROM books ORDER BY year_publishing"):
#         print(*row)
#     print('\n2.')
#
#     for row in cur.execute("""SELECT books.name FROM books JOIN author_book ON books.id_books = author_book.id_book
#         JOIN authors ON author_book.id_author = authors.id_author WHERE authors.surname = ? AND authors.name = ?""",
#                            ('Иванов', 'Петр')):
#         print(*row)
#     print('\n3.')
#
#     for row in cur.execute("""SELECT name FROM books JOIN sections ON books.id_section = sections.id_section
#     WHERE sections.section = ?""", ('Drama',)):
#         print(*row)
#     print('\n4.')
#
#     for row in cur.execute("""SELECT name FROM books JOIN publishing ON books.id_publish = publishing.id_publish
#     WHERE publishing.publish = ?""", ('Elsevier',)):
#         print(*row)
#     print('\n5.')
#
#     for row in cur.execute("SELECT surname, name FROM authors ORDER BY surname, name"):
#         print(*row)
#     print('\n6.')
#
#     for row in cur.execute("SELECT name, year_publishing FROM books ORDER BY name, year_publishing"):
#         print(*row)
#     print('\n7.')
#
#     for row in cur.execute("""SELECT books.name, year_publishing FROM books JOIN
#     author_book ON books.id_books = author_book.id_book JOIN authors ON author_book.id_author = authors.id_author
#     WHERE authors.surname = ? AND authors.name = ? ORDER BY year_publishing""", ('Иванов', 'Петр')):
#         print(*row)
#     print('\n8.')
#
#     for row in cur.execute("SELECT name FROM books WHERE year_publishing = ?", (1842,)):
#         print(*row)
#     print('\n9.')
#
#     for row in cur.execute("""SELECT authors.surname, authors.name FROM authors JOIN
#     author_book ON authors.id_author = author_book.id_author JOIN
#     books ON author_book.id_book = books.id_books JOIN
#     publishing ON books.id_publish = publishing.id_publish WHERE publishing.publish = ?""", ('Elsevier',)):
#         print(*row)
#     print('\n10.')
#
#     for row in cur.execute("SELECT name FROM books WHERE name LIKE ?", ('%and%',)):
#         print(*row)


# UPDATES
# with sq.connect('Library.sqlite') as con:
#     cur = con.cursor()
#
#     cur.execute("""UPDATE books SET year_publishing = 2022 WHERE id_books IN (SELECT id_books FROM author_book JOIN
#     authors ON author_book.id_author = authors.id_author WHERE surname = 'Иванов')""")
#
#     cur.execute("UPDATE books SET name = 'Новая книга', year_publishing = 2023 WHERE storage = 'Москва'")
#
#     cur.execute("""UPDATE books SET name = 'Новое название', id_section = (SELECT id_section FROM sections
#     WHERE section = 'Фантастика') WHERE id_books IN (SELECT id_books FROM author_book JOIN
#     authors ON author_book.id_author = authors.id_author WHERE name = 'Александр' AND surname = 'Петров')""")
#
#     cur.execute("UPDATE books SET name = 'Старое название' WHERE year_publishing BETWEEN 2010 AND 2015")
#
#     cur.execute("""UPDATE books SET storage = 'Библиотека №2' WHERE id_books IN (SELECT id_books FROM author_book
#     WHERE id_author = 7)""")
#
#     cur.execute("""UPDATE publishing SET city = (SELECT city FROM books
#     WHERE books.id_publish = publishing.id_publish)""")
#
#     cur.execute("""UPDATE author_book SET id_author = (SELECT id_author FROM authors
#     WHERE authors.id_author = author_book.id_author)""")
#
#     cur.execute("""UPDATE books SET id_section = (SELECT id_section FROM sections
#     WHERE sections.section = books.id_section)""")
#
#     cur.execute("""UPDATE books SET year_publishing = 2022
#                 WHERE id_books IN (SELECT id_book FROM author_book WHERE year_publishing = 2021)""")
#
#     cur.execute("""UPDATE books SET storage = 'Книжный шкаф 1'
#                 WHERE id_publish IN (SELECT id_publish FROM publishing WHERE publish = 'Издательство А')""")
#
#     cur.execute("""UPDATE authors SET surname = 'Новая фамилия'
#                 WHERE id_author IN (SELECT id_author FROM author_book WHERE id_author = 1)""")
#
#     cur.execute("""UPDATE books SET year_publishing = 2022
#                 WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city = 'Москва')""")
#
#     cur.execute("""UPDATE books SET storage = 'Книжный шкаф 1' WHERE id_books IN (SELECT id_book FROM author_book
#     WHERE id_author IN (SELECT id_author FROM authors WHERE surname = 'Иванов'))""")
#
#     cur.execute("""UPDATE books SET year_publishing = 2023 WHERE id_books IN (SELECT id_book FROM author_book
#     WHERE id_author IN (SELECT id_author FROM authors WHERE name = 'Анна'))""")
#
#     cur.execute("""UPDATE books SET id_section = (SELECT id_section FROM sections WHERE section = 'Классика')
#                 WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city = 'Санкт-Петербург')""")
#
#     cur.execute("""UPDATE books SET year_publishing = 2024 WHERE id_books IN (SELECT id_book FROM author_book
#                 WHERE id_author IN (SELECT id_author FROM authors WHERE surname = 'Петров'))""")
#
#
# # DELETES
# with sq.connect('Library.sqlite') as con:
#     cur = con.cursor()
#
#     # 1. Удалить все записи из таблицы Книги, у которых Раздел = 'Фантастика':
#     cur.execute("DELETE FROM books WHERE id_section = (SELECT id_section FROM sections WHERE section = 'Фантастика')")
#
#     # 2. Удалить все записи из таблицы Книги, у которых ГодИздания меньше 2000:
#     cur.execute("DELETE FROM books WHERE year_publishing < 2000")
#
#     # 3. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 1:
#     cur.execute("DELETE FROM author_book WHERE id_author = 1")
#
#     # 4. Удалить все записи из таблицы Авторы, у которых Фамилия начинается с буквы "А":
#     cur.execute("DELETE FROM authors WHERE surname LIKE 'А%'")
#
#     # 5. Удалить все записи из таблицы Издательства, у которых Город равен "Москва":
#     cur.execute("DELETE FROM publishing WHERE city = 'Москва'")
#
#     # 6. Удалить все записи из таблицы АвторКниги, у которых КодКниги равен 10:
#     cur.execute("DELETE FROM author_book WHERE id_book = 10")
#
#     # 7. Удалить все записи из таблицы Книги, у которых МестоХранения равно "Склад":
#     cur.execute("DELETE FROM books WHERE storage = 'Склад'")
#
#     # 8. Удалить все записи из таблицы Разделы, у которых Раздел равен "Детективы":
#     cur.execute("DELETE FROM sections WHERE section = 'Детективы'")
#
#     # 9. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 2:
#     cur.execute("DELETE FROM author_book WHERE id_author = 2")
#
#     # 10. Удалить все записи из таблицы Издательства, у которых Издательство равно "O'Reilly Media":
#     cur.execute("DELETE FROM publishing WHERE publish = 'O''Reilly Media'")
#
#     # 11. Удалить все записи из таблицы Книги, у которых Название содержит слово "Война":
#     cur.execute("DELETE FROM books WHERE name LIKE '%Война%'")
#
#     # 12. Удалить все книги, которые были изданы до 2000 года включительно и хранятся в "Библиотека №1".
#     cur.execute("DELETE FROM books WHERE year_publishing <= 2000 AND storage = 'Библиотека №1'")
#
#     # 13. Удалить всех авторов, у которых нет книг в таблице Книги.
#     cur.execute("DELETE FROM authors WHERE id_author NOT IN (SELECT DISTINCT id_author FROM author_book)")
#
#     # 14. Удалить все книги, изданные в городе "Москва", из таблицы "Книги".
#     cur.execute("DELETE FROM books WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city = 'Москва')")
#
#     # 15. Удалить всех авторов, чьи фамилии начинаются на букву "А" из таблицы "authors" и соответствующие записи из
#     # таблицы "author_book".
#     cur.execute("DELETE FROM authors WHERE surname LIKE 'А%' AND id_author IN (SELECT id_author FROM author_book)")
#     cur.execute("DELETE FROM author_book WHERE id_author IN (SELECT id_author FROM authors WHERE surname LIKE 'А%')")
#
#     # 16. Удалить все записи из таблицы "author_book", связанные с книгами, изданными в городе "Москва".
#     cur.execute("""DELETE FROM author_book WHERE id_book IN (SELECT id_books FROM books
#     WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city = 'Москва'))""")
#
#     # 17. Удалить все книги из таблицы "books", которые были написаны авторами с фамилиями, начинающимися на букву "П"
#     cur.execute("""DELETE FROM books WHERE id_books IN (SELECT id_book FROM author_book
#     WHERE id_author IN (SELECT id_author FROM authors WHERE surname LIKE 'П%'))""")
#
#     # 18. Удалить все книги из таблицы "books", которые были изданы в городах с названиями, начинающимися на букву "Н"
#     cur.execute("DELETE FROM books WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city LIKE 'Н%')")
#
#     # 19. Удалить все записи из таблицы "author_book", связанные с книгами, изданными в городах, название которых
#     # начинается на букву
#     cur.execute("""DELETE FROM author_book WHERE id_book IN ( SELECT id_books FROM books JOIN
#     publishing ON books.id_publish = publishing.id_publish WHERE publishing.city LIKE 'Н%')""")
