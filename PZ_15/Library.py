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
    cur.executemany("INSERT INTO authors VALUES (?, ?, ?)", info_authors)
    cur.executemany("INSERT INTO sections VALUES (?)", info_sections)
    cur.executemany("INSERT INTO publishing VALUES (?, ?)", info_publishing)
    cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", info_books)
    cur.executemany("INSERT INTO author_book VALUES (?, ?, ?)", info_author_book)


with sq.connect('Library.sqlite') as con:
    cur = con.cursor()
    print('1)', *cur.execute("SELECT name, year_publishing FROM books ORDER BY year_publishing"), sep='\n')
    print()
    print('2)', *cur.execute("""SELECT name FROM author_book INNER JOIN
    books ON books.id_books = author_book.id_author_book WHERE id_author == 1
    """), sep='\n')
    print()
    # print('3)', *cur.execute("SELECT * FROM books"), sep='\n')
    # print()
    print('4)', *cur.execute("SELECT surname FROM authors ORDER BY surname"), sep='\n')
    print()
    # print('5)', *cur.execute("SELECT * FROM books"), sep='\n')
    # print()

with sq.connect('Library.sqlite') as con:
    cur = con.cursor()
    cur.execute("""UPDATE books SET year_publishing = 2023, name = 'Новая книга' WHERE city = 'Москва'""")
