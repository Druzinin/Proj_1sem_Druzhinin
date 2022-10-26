from random import randint


def rand_digit():
    n = randint(1000, 9999)
    print(n)

    a = n // 1000
    b = n % 1000 // 100
    c = n % 100 // 10
    d = n % 10
    if a == b or a == c or a == d or b == c or b == d or c == d:
        print('Есть повторяющиеся цифры')
    else:
        print('Нет повторяющихся цифр')
