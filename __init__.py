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
