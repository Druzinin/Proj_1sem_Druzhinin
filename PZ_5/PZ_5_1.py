from random import randint  # импортирование функции random
n = randint(1000, 9999)
print(n)

a = n // 1000  # разделение числа на отдельные цифры
b = n % 1000 // 100
c = n % 100 // 10
d = n % 10

if a == b or a == c or a == d or b == c or b == d or c == d:  # проверка на одинаковые цифры
    print('Есть одинаковые цифры')
else:
    print('Нет одинаковых цифр')
