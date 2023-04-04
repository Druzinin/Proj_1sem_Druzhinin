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
    section TEXT
    REFERENCES sections ON DELETE CASCADE ON UPDATE CASCADE,
    publish TEXT
    REFERENCES publishing ON DELETE CASCADE ON UPDATE CASCADE
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sections (
    section TEXT PRIMARY KEY
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS publishing (
    publish TEXT PRIMARY KEY,
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
    cur.executemany("INSERT INTO books (name, year_publishing, storage, section, publish)"
                    "VALUES (?, ?, ?, ?, ?)", info_books)

with sq.connect('Library.sqlite') as con:
    cur = con.cursor()

    cur.execute("SELECT name, year_publishing FROM books ORDER BY year_publishing")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])

    author_last_name = 'Иванов'
    author_first_name = 'Петр'
    cur.execute("""SELECT books.name FROM books JOIN author_book ON books.id_books = author_book.id_book
        JOIN authors ON author_book.id_author = authors.id_author WHERE authors.surname = ? AND authors.name = ?""",
                (author_last_name, author_first_name))
    rows = cur.fetchall()
    for row in rows:
        print(row[0])

    section = 'Детективы'
    cur.execute("""SELECT name FROM books JOIN main.sections ON books.section = sections.section
    WHERE sections.section = ?""",
                (section,))
    rows = cur.fetchall()
    for row in rows:
        print(row[0])

    publisher = 'Eksmo'
    cur.execute("""SELECT name FROM books JOIN publishing ON books.publish = publishing.publish
    WHERE publishing.publish = ?""",
                (publisher,))
    rows = cur.fetchall()
    for row in rows:
        print(row[0])

    cur.execute("SELECT surname, name FROM authors ORDER BY surname, name")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])

    cur.execute("SELECT name, year_publishing FROM books ORDER BY name, year_publishing")
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])

    author_last_name = 'Иванов'
    author_first_name = 'Петр'
    cur.execute("""SELECT books.name, year_publishing FROM books JOIN
    main.author_book ON books.id_books = author_book.id_book JOIN authors ON author_book.id_author = authors.id_author
    WHERE authors.surname = ? AND authors.name = ? ORDER BY year_publishing""",
                (author_last_name, author_first_name))
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])

    year = 2017
    cur.execute("SELECT name FROM books WHERE year_publishing = ?", (year,))
    rows = cur.fetchall()
    for row in rows:
        print(row[0])

    publisher = 'Eksmo'
    cur.execute("""SELECT DISTINCT authors.surname, authors.name FROM authors JOIN
    main.author_book ON authors.id_author = author_book.id_author JOIN books ON author_book.id_book = books.id_books
    JOIN publishing ON books.publish = publishing.publish WHERE publishing.publish = ?""",
                (publisher,))
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1])

    word = '%метро%'
    cur.execute("SELECT name FROM books WHERE name LIKE ?", (word,))
    rows = cur.fetchall()
    for row in rows:
        print(row[0])


# UPDATE Книги
# SET год_издания = 2022
# WHERE автор IN (
# SELECT id_автора
# FROM Авторы
# WHERE фамилия = 'Иванов'
# );
#
# UPDATE Книги
# SET название = 'Новая книга', год_издания = 2023
# WHERE место_хранения IN (
# SELECT id_места
# FROM МестаХранения
# WHERE город = 'Москва'
# );
#
# UPDATE Книги
# SET название = 'Новое название', раздел = 'Фантастика'
# WHERE автор IN (
# SELECT id_автора
# FROM Авторы
# WHERE имя = 'Александр' AND фамилия = 'Петров'
# );
#
# UPDATE Книги
# SET название = 'Старое название'
# WHERE год_издания BETWEEN 2010 AND 2015;
#
# UPDATE Книги
# SET место_хранения = 'Библиотека №2'
# WHERE автор = 7;
#
# UPDATE Книги
# SET город_издания = (
# SELECT город
# FROM Издательства
# WHERE Издательства.id_города = Книги.id_города
# );
#
# UPDATE АвторКниги
# SET код_автора = (
# SELECT id_автора
# FROM Авторы
# WHERE Авторы.id_автора = АвторКниги.id_автора
# );
#
# UPDATE Книги
# SET раздел = (
# SELECT название
# FROM Разделы
# WHERE Разделы.id_раздела = Книги.id_раздела
# );
#
# UPDATE Книги
# SET год_издания = (
# SELECT год_издания
# FROM АвторКниги
# WHERE АвторКниги.id_книги = Книги.id_книги
# );
#
# UPDATE Книги
# SET место_хранения = (
# SELECT МестаХранения.название
# FROM Издательства
# INNER JOIN МестаХранения ON Издательства.id_места = МестаХранения.id_места
# WHERE Издательства.id_издательства = Книги.id_издательства
# );
#
# UPDATE Авторы
# SET фамилия = (
# SELECT фамилия
# FROM АвторКниги
# WHERE АвторКниги.id_автора = Авторы.id_автора
# )
# WHERE id_автора IN (
# SELECT id_автора
# FROM АвторКниги
# );
#
# UPDATE Книги
# SET год_издания = 2022
# WHERE город_издания = 'Москва';
# UPDATE Книги
# SET МестоХранения = 'Книжный шкаф 1'
# WHERE АвторКниги IN (
#   SELECT Код
#   FROM АвторКниги
#   WHERE АвторКниги.КодАвтора IN (
#     SELECT Код
#     FROM Авторы
#     WHERE Авторы.Фамилия = 'Иванов'
#   )
# );
#
# UPDATE Книги
# SET ГодИздания = 2023
# WHERE АвторКниги IN (
#   SELECT Код
#   FROM АвторКниги
#   WHERE АвторКниги.КодАвтора IN (
#     SELECT Код
#     FROM Авторы
#     WHERE Авторы.Имя = 'Анна'
#   )
# );
#
# UPDATE Книги
# SET Раздел = 'Классика'
# WHERE ГородИздания = 'Санкт-Петербург';
# UPDATE Книги
# SET ГодИздания = 2024
# WHERE АвторКниги IN (
#   SELECT Код
#   FROM АвторКниги
#   WHERE АвторКниги.КодАвтора IN (
#     SELECT Код
#     FROM Авторы
#     WHERE Авторы.Фамилия = 'Петров'
#   )
# );

# 1. UPDATE Library SET year_published = 2022 WHERE author_lastname = 'Иванов';
# 2. UPDATE Library SET title = 'Новая книга', year_published = 2023 WHERE location = 'Москва';
# 3. UPDATE Library SET title = 'Новое название', section = 'Фантастика'
# WHERE author_firstname = 'Александр' AND author_lastname = 'Петров';
# 4. UPDATE Library SET title = 'Старое название' WHERE year_published BETWEEN 2010 AND 2015;
# 5. UPDATE Library SET location = 'Библиотека №2' WHERE author_code = 7;
# 6. UPDATE Книги SET city = (SELECT city FROM Издательства WHERE Издательства.city_code = Книги.city_code);
# 7. UPDATE АвторКниги SET author_code = (SELECT code FROM Авторы WHERE Авторы.author_code = АвторКниги.author_code);
# 8. UPDATE Книги SET section = (SELECT section FROM Разделы WHERE Разделы.section_name = Книги.section);
# 9. UPDATE Книги SET year_published = (SELECT year_published FROM АвторКниги WHERE АвторКниги.book_code = Книги.code);
# 10. UPDATE Книги SET location = (SELECT location FROM Издательства WHERE Издательства.name = Книги.publisher);
# 11. UPDATE Авторы SET author_lastname = (SELECT author_lastname FROM АвторКниги
# WHERE АвторКниги.author_code = Авторы.code);
# 12. UPDATE Library SET year_published = 2022 WHERE location = 'Москва';
# 13. UPDATE Library SET location = 'Книжный шкаф 1' WHERE author_lastname = 'Иванов';
# 14. UPDATE Library SET year_published = 2023 WHERE author_firstname = 'Анна';
# 15. UPDATE Library SET section = 'Классика' WHERE location = 'Санкт-Петербург';
# 16. UPDATE Library SET year_published = 2024 WHERE author_lastname = 'Петров';


# DELETE FROM Книги WHERE Раздел = 'Фантастика';

# DELETE FROM Книги WHERE ГодИздания < 2000;

# DELETE FROM АвторКниги WHERE КодАвтора = 1;

# DELETE FROM Авторы WHERE Фамилия LIKE 'А%';
# -- также нужно удалить связанные записи из таблицы АвторКниги

# DELETE FROM АвторКниги WHERE КодАвтора IN (SELECT КодАвтора FROM Авторы WHERE Фамилия LIKE 'А%');

# DELETE FROM Издательства WHERE Город = 'Москва';

# DELETE FROM АвторКниги WHERE КодКниги = 10;

# DELETE FROM Книги WHERE МестоХранения = 'Склад';

# DELETE FROM Разделы WHERE Раздел = 'Детективы';

# DELETE FROM АвторКниги WHERE КодАвтора = 2;

# DELETE FROM Издательства WHERE Издательство = 'O''Reilly Media';

# DELETE FROM Книги WHERE Название LIKE '%Война%';

# DELETE FROM Книги WHERE ГодИздания <= 2000 AND МестоХранения = 'Библиотека №1';

# DELETE FROM Авторы WHERE КодАвтора NOT IN (SELECT КодАвтора FROM АвторКниги);

# DELETE FROM Книги WHERE КодИздательства IN (SELECT КодИздательства FROM Издательства WHERE Город = 'Москва');

# DELETE FROM Авторы WHERE Фамилия LIKE 'А%';
# -- также нужно удалить связанные записи из таблицы АвторКниги

# DELETE FROM АвторКниги WHERE КодАвтора IN (SELECT КодАвтора FROM Авторы WHERE Фамилия LIKE 'А%');

# DELETE FROM АвторКниги WHERE КодКниги IN (SELECT КодКниги FROM Книги WHERE КодИздательства IN
# (SELECT КодИздательства FROM Издательства WHERE Город = 'Москва'));

# DELETE FROM Книги WHERE Код IN (SELECT КодКниги FROM АвторКниги JOIN
# Авторы ON АвторКниги.КодАвтора = Авторы.КодАвтора WHERE Авторы.Фамилия LIKE 'П%');

# DELETE FROM Книги WHERE КодИздательства IN (SELECT КодИздательства FROM Издательства WHERE Название LIKE 'Н%');

# DELETE FROM АвторКниги WHERE КодКниги IN (SELECT Код FROM Книги WHERE КодИздательства IN
# (SELECT КодИздательства FROM Издательства WHERE Название LIKE 'Н%'));
