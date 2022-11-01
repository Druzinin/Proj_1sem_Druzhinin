# Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.
from random import randint  # Импортирование библиотеки random


def rand_digit():
    n = randint(1000, 9999)
    print(n)

    a = n // 1000
    b = n % 1000 // 100
    c = n % 100 // 10
    d = n % 10
    if a == b or a == c or a == d or b == c or b == d or c == d:
        print('Есть повторяющиеся цифры.')
    else:
        print('Нет повторяющихся цифр.')


rand_digit()
