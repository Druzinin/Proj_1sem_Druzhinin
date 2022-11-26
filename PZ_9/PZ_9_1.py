d = dict(keyboard='клавиатура', mouse='мышь', display='монитор', printer='принтер', high='', )
s = input('Введите слово на английском: ')
print(d[s] if s in d else 'Нет такого слова в словаре')
