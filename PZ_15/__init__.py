# with sq.connect('ЗАРПЛАТА.sqlite') as con:
#     cur = con.cursor()
#     print(1, *cur.execute("SELECT имя, фамилия, должность FROM анкета;"))
#     print(2, *cur.execute("SELECT имя, фамилия, базовая_ставка FROM анкета;"))
#     print(3, *cur.execute("SELECT имя, фамилия FROM анкета WHERE отдел = 'IT';"))
#     print(4, *cur.execute("SELECT имя, фамилия FROM анкета WHERE дата_найма > '2022-01-01';"))
#     print(5, *cur.execute("SELECT * FROM Больничные_листы WHERE id_сотрудника = 42;"))
#     print(6, *cur.execute("SELECT * FROM Больничные_листы WHERE оплачен = 'YES';"))
#     print(7, *filter(lambda x: date(*map(int, x[2].split('-'))) <
#                                date(date.today().year, date.today().month, 1) <
#                                date(*map(int, x[3].split('-'))),
#                      cur.execute("""SELECT имя, фамилия, дата_начала, дата_окончания FROM анкета INNER JOIN
#         Больничные_листы ON анкета.id_a = Больничные_листы.id_сотрудника;""")))
#     print(8, sum(r) / len(r) if (r := sum(cur.execute("SELECT базовая_ставка FROM анкета;"), ())) else 0.0)
#     print(9, *cur.execute("SELECT имя, фамилия FROM анкета WHERE базовая_ставка > 100000;"))
#     print(10, *map(lambda x: (x[0], x[1], (date(*map(int, x[3].split('-'))) - date(*map(int, x[2].split('-')))).days),
#                    cur.execute("""SELECT имя, фамилия, дата_начала, дата_окончания FROM анкета INNER JOIN
#         Больничные_листы ON анкета.id_a = Больничные_листы.id_сотрудника;""")))
#     print(11, *filter(lambda i: 0 < (date.today() - date(*map(int, i[3].split('-')))).days < 30,
#                       cur.execute("""SELECT имя, фамилия, Больничные_листы.* FROM анкета INNER JOIN
#         Больничные_листы ON анкета.id_a = Больничные_листы.id_сотрудника;""")))
#     print(12, *cur.execute("SELECT * FROM ;"))
#     print(13, sorted(cur.execute("""SELECT имя, фамилия, Больничные_листы.* FROM анкета INNER JOIN
#         Больничные_листы ON анкета.id_a = Больничные_листы.id_сотрудника;"""), key=lambda x: x[3])[1])
#     print(14, sorted(cur.execute("""SELECT имя, фамилия, Больничные_листы.* FROM анкета INNER JOIN
#         Больничные_листы ON анкета.id_a = Больничные_листы.id_сотрудника;"""), key=lambda x: x[3])[0])
#     print(15, *cur.execute("SELECT * FROM ;"))
