import sqlite3 as sq
# from datetime import date
from data import *

with sq.connect('Library.sqlite') as con:
    con.execute("PRAGMA foreign_keys = ON;")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS authors;")
    cur.execute("DROP TABLE IF EXISTS books;")
    cur.execute("DROP TABLE IF EXISTS sections;")
    cur.execute("DROP TABLE IF EXISTS publishing;")
    cur.execute("DROP TABLE IF EXISTS author_book;")

    cur.execute("""CREATE TABLE IF NOT EXISTS authors (
    id_author INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT NOT NULL,
    name TEXT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS books (
    id_books INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    year_publishing TEXT,
    storage TEXT,
    id_section TEXT
    REFERENCES sections ON DELETE CASCADE ON UPDATE CASCADE,
    id_publishing TEXT
    REFERENCES publishing ON DELETE CASCADE ON UPDATE CASCADE
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS sections (
    id_section INTEGER PRIMARY KEY AUTOINCREMENT
    );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS publishing (
    id_publishing INTEGER PRIMARY KEY AUTOINCREMENT,
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
    con.execute("PRAGMA foreign_keys = ON;")
    cur = con.cursor()
    cur.execute("INSERT INTO authors VALUES (?, ?, ?)", info_authors)
    cur.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", info_books)
    cur.execute("INSERT INTO sections VALUES (?)", info_sections)
    cur.execute("INSERT INTO publishing VALUES (?, ?)", info_publishing)
    cur.execute("INSERT INTO author_book VALUES (?, ?, ?)", info_author_book)


with sq.connect('Library.sqlite') as con:
    cur = con.cursor()
    cur.execute("SELECT name FROM books ORDER BY year_publishing")
    cur.execute("""SELECT name FROM books INNER JOIN
    author_book ON books.id_books = id_book INNER JOIN
    id_author ON authors.id_author = id_author_book
    """)
