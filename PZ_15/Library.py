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
    id_book INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    year_publish INTEGER,
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
    cur.executemany("INSERT INTO books (name, year_publish, storage, id_section, id_publish) VALUES (?, ?, ?, ?, ?)",
                    info_books)


# SELECTS
# with sq.connect('Library.sqlite') as con:
#     cur = con.cursor()
#
#     print('\n1.')
#     for row in cur.execute("SELECT name, year_publish FROM books ORDER BY year_publish"):
#         print(*row)
#     print('\n2.')
#
#     for row in cur.execute("""SELECT books.name FROM books JOIN author_book ON books.id_book = author_book.id_book
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
#     for row in cur.execute("SELECT name, year_publish FROM books ORDER BY name, year_publish"):
#         print(*row)
#     print('\n7.')
#
#     for row in cur.execute("""SELECT books.name, year_publish FROM books JOIN
#     author_book ON books.id_book = author_book.id_book JOIN authors ON author_book.id_author = authors.id_author
#     WHERE authors.surname = ? AND authors.name = ? ORDER BY year_publish""", ('Иванов', 'Петр')):
#         print(*row)
#     print('\n8.')
#
#     for row in cur.execute("SELECT name FROM books WHERE year_publish = ?", (1842,)):
#         print(*row)
#     print('\n9.')
#
#     for row in cur.execute("""SELECT authors.surname, authors.name FROM authors JOIN
#     author_book ON authors.id_author = author_book.id_author JOIN
#     books ON author_book.id_book = books.id_book JOIN
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
#     # 1. Обновить год издания всех книг, написанных автором с фамилией "Иванов", установив год издания равным 2022:
#     cur.execute("""UPDATE books SET year_publish = 2022 WHERE id_book IN (SELECT id_book FROM author_book JOIN
#     authors ON author_book.id_author = authors.id_author WHERE surname = 'Иванов')""")
#     print(*cur.execute("SELECT year_publish FROM books"))
#
#     # 2. Обновить название и год издания книги, хранящейся в городе "Москва", установив
#     # название "Новая книга" и год издания равным 2023:
#     cur.execute("UPDATE books SET name = 'Новая книга', year_publish = 2023 WHERE storage = 'Москва'")
#     print(*cur.execute("SELECT name, year_publish FROM books"))
#
#     # 3. Обновить название и раздел всех книг, написанных автором с именем "Александр" и фамилией "Петров", установив
#     # название "Новое название" и раздел "Фантастика":
#     cur.execute("""UPDATE books SET name = 'Новое название', id_section = (SELECT id_section FROM sections
#     WHERE section = 'Фантастика') WHERE id_book IN (SELECT id_book FROM author_book JOIN
#     authors ON author_book.id_author = authors.id_author WHERE name = 'Александр' AND surname = 'Петров')""")
#     print(*cur.execute("SELECT name, id_section FROM books"))
#
#     # 4. Обновить название всех книг, которые были опубликованы в годы с 2010 по 2015 включительно, установив
#     # название "Старое название":
#     cur.execute("UPDATE books SET name = 'Старое название' WHERE year_publish BETWEEN 2010 AND 2015")
#     print(*cur.execute("SELECT name, year_publish FROM books"))
#
#     # 5. Обновить место хранения всех книг, написанных автором с кодом 7, установив место хранения "Библиотека №2":
#     cur.execute("""UPDATE books SET storage = 'Библиотека №2' WHERE id_book IN (SELECT id_book FROM author_book
#     WHERE id_author = 7)""")
#     print(*cur.execute("SELECT storage FROM books"))
#
#     # 6. Обновление города из таблицы Издательства по коду города в таблице Книги:
#     cur.execute("""UPDATE publishing SET city = (SELECT city FROM publishing WHERE id_publish = 1)""")
#     print(*cur.execute("""SELECT city FROM publishing"""))
#
#     # 7. Обновление кода автора в таблице АвторКниги по коду автора в таблице Авторы:
#     cur.execute("""UPDATE author_book SET id_author = (SELECT id_author FROM authors
#     WHERE authors.id_author = author_book.id_author)""")
#     print(*cur.execute("""SELECT author_book.id_author FROM author_book JOIN
#     authors ON author_book.id_author = authors.id_author WHERE authors.id_author = author_book.id_author"""))
#
#     # 8. Обновление названия раздела в таблице Книги по названию раздела в таблице Разделы:
#     cur.execute("""UPDATE books SET id_section = (SELECT id_section FROM sections
#     WHERE sections.section = books.id_section)""")
#
#     # 9. Обновление года издания в таблице books по году издания в таблице author_book:
#     cur.execute("""UPDATE books SET year_publish = 2022
#                 WHERE id_book IN (SELECT id_book FROM author_book WHERE year_publish = 2021)""")
#
#     # 10. Обновление места хранения в таблице books по названию издательства в таблице publishing:
#     cur.execute("""UPDATE books SET storage = 'Книжный шкаф 1'
#                 WHERE id_publish IN (SELECT id_publish FROM publishing WHERE publish = 'Издательство А')""")
#
#     # 11. Обновление фамилии автора в таблице authors по коду автора в таблице author_book:
#     cur.execute("""UPDATE authors SET surname = 'Новая фамилия'
#                 WHERE id_author IN (SELECT id_author FROM author_book WHERE id_author = 1)""")
#
#     # 12. Обновить год издания всех книг, изданных в городе "Москва", на 2022 год.
#     cur.execute("""UPDATE books SET year_publish = 2022
#                 WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city = 'Москва')""")
#
#     # 13. Обновить место хранения всех книг, написанных автором с фамилией "Иванов", на "Книжный шкаф 1".
#     cur.execute("""UPDATE books SET storage = 'Книжный шкаф 1' WHERE id_book IN (SELECT id_book FROM author_book
#     WHERE id_author IN (SELECT id_author FROM authors WHERE surname = 'Иванов'))""")

#     # 14. Обновить год издания всех книг, написанных автором с именем "Анна", на 2023 год.
#     cur.execute("""UPDATE books SET year_publish = 2023 WHERE id_book IN (SELECT id_book FROM author_book
#     WHERE id_author IN (SELECT id_author FROM authors WHERE name = 'Анна'))""")
#
#     # 15. Обновить название раздела всех книг, изданных в городе "Санкт-Петербург", на "Классика".
#     cur.execute("""UPDATE books SET id_section = (SELECT id_section FROM sections WHERE section = 'Классика')
#                 WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city = 'Санкт-Петербург')""")
#
#     # 16. Обновить год издания всех книг, написанных автором с фамилией "Петров", на 2024 год.
#     cur.execute("""UPDATE books SET year_publish = 2024 WHERE id_book IN (SELECT id_book FROM author_book
#                 WHERE id_author IN (SELECT id_author FROM authors WHERE surname = 'Петров'))""")


# DELETES
# with sq.connect('Library.sqlite') as con:
#     cur = con.cursor()
#
#     # 1. Удалить все записи из таблицы Книги, у которых Раздел = 'Фантастика':
#     cur.execute("DELETE FROM books WHERE id_section = (SELECT id_section FROM sections WHERE section = 'Фантастика')")
#     print(*cur.execute("SELECT section FROM books JOIN sections ON books.id_section = sections.id_section"))
#
#    # 2. Удалить все записи из таблицы Книги, у которых ГодИздания меньше 2000:
#    cur.execute("DELETE FROM books WHERE year_publish < 2000")
#    print(*cur.execute("SELECT year_publish FROM books"))
#
#    # 3. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 1:
#    cur.execute("DELETE FROM author_book WHERE id_author = 1")
#    print(*cur.execute("SELECT id_author FROM author_book"))
#
#     # 4. Удалить все записи из таблицы Авторы, у которых Фамилия начинается с буквы "А":
#     cur.execute("DELETE FROM authors WHERE surname LIKE 'A%'")
#     print(*cur.execute("SELECT surname FROM authors"))
#
#     # 5. Удалить все записи из таблицы Издательства, у которых Город равен "Москва":
#     cur.execute("DELETE FROM publishing WHERE city = 'Москва'")
#     print(*cur.execute("SELECT city FROM publishing"))
#
#     # 6. Удалить все записи из таблицы АвторКниги, у которых КодКниги равен 10:
#     cur.execute("DELETE FROM author_book WHERE id_book = 10")
#     print(*cur.execute("SELECT id_book FROM author_book"))
#
#     # 7. Удалить все записи из таблицы Книги, у которых МестоХранения равно "Склад":
#     cur.execute("DELETE FROM books WHERE storage = 'Склад'")
#     print(*cur.execute("SELECT storage FROM books"))
#
#     # 8. Удалить все записи из таблицы Разделы, у которых Раздел равен "Детективы":
#     cur.execute("DELETE FROM sections WHERE section = 'Детективы'")
#     print(*cur.execute("SELECT section FROM sections"))
#
#     # 9. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 2:
#     cur.execute("DELETE FROM author_book WHERE id_author = 2")
#     print(*cur.execute("SELECT id_author FROM author_book"))
#
#     # 10. Удалить все записи из таблицы Издательства, у которых Издательство равно "O'Reilly Media":
#     cur.execute("DELETE FROM publishing WHERE publish = 'O''Reilly Media'")
#     print(*cur.execute("SELECT publish FROM publishing"))
#
#    # 11. Удалить все записи из таблицы Книги, у которых Название содержит слово "Война":
#    cur.execute("DELETE FROM books WHERE name LIKE '%War%'")
#    print(*cur.execute("SELECT name FROM books"))
#
#    # 12. Удалить все книги, которые были изданы до 2000 года включительно и хранятся в "Библиотека №1".
#    cur.execute("DELETE FROM books WHERE year_publish <= 2000 AND storage = 'Библиотека №1'")
#    print(*cur.execute("SELECT year_publish, storage FROM books"))
#
#    # 13. Удалить всех авторов, у которых нет книг в таблице Книги.
#    cur.execute("DELETE FROM authors WHERE id_author NOT IN (SELECT DISTINCT id_author FROM author_book)")
#    print(*cur.execute("SELECT id_author FROM authors"))
#
#    # 14. Удалить все книги, изданные в городе "Москва", из таблицы "Книги".
#    cur.execute("DELETE FROM books WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city = 'Москва')")
#    print(*cur.execute("SELECT city FROM books JOIN publishing ON books.id_publish = publishing.id_publish"))
#
#    # 15. Удалить всех авторов, чьи фамилии начинаются на букву "А" из таблицы "authors" и соответствующие записи из
#    # таблицы "author_book".
#     cur.execute("DELETE FROM authors WHERE surname LIKE 'A%'")
#     print(*cur.execute("SELECT surname FROM authors"))
#
#    # 16. Удалить все записи из таблицы "author_book", связанные с книгами, изданными в городе "Москва".
#    cur.execute("""DELETE FROM author_book WHERE id_book IN (SELECT id_book FROM books JOIN
#    publishing ON books.id_publish = publishing.id_publish WHERE city = 'Москва')""")
#    print(*cur.execute("""SELECT city FROM author_book JOIN books ON author_book.id_book = books.id_book JOIN
#    publishing ON books.id_publish = publishing.id_publish"""))
#
#    # 17. Удалить все книги из таблицы "books", которые были написаны авторами с фамилиями, начинающимися на букву "П"
#    cur.execute("""DELETE FROM books WHERE id_book IN (SELECT id_book FROM author_book JOIN
#    authors ON author_book.id_author = authors.id_author WHERE surname LIKE 'П%')""")
#    print(*cur.execute("""SELECT surname FROM author_book JOIN books ON author_book.id_book = books.id_book JOIN
#    authors ON author_book.id_author = authors.id_author"""))
#
#    # 18. Удалить все книги из таблицы "books", которые были изданы в городах с названиями, начинающимися на букву "Н"
#     cur.execute("DELETE FROM books WHERE id_publish IN (SELECT id_publish FROM publishing WHERE city LIKE 'Н%')")
#     print(*cur.execute("SELECT city FROM books JOIN publishing ON books.id_publish = publishing.id_publish"))
#
#    # 19. Удалить все записи из таблицы "author_book", связанные с книгами, изданными в городах, название которых
#    # начинается на букву "Н"
#     cur.execute("""DELETE FROM author_book WHERE id_book IN (SELECT id_book FROM books JOIN
#     publishing ON books.id_publish = publishing.id_publish WHERE city LIKE 'Н%')""")
#     print(*cur.execute("""SELECT city FROM author_book JOIN books ON author_book.id_book = books.id_book JOIN
#     publishing ON books.id_publish = publishing.id_publish"""))
