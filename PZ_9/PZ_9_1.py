d = dict(keyboard='клавиатура', mouse='мышь', display='монитор', printer='принтер', low='низкий',
         high='высокий', cheap='дешевый', expensive='дорогой', quality='качество', quiet='тихий')
s = input('Введите слово на английском: ').lower()
print(d[s] if s in d else 'Нет такого слова в словаре')
