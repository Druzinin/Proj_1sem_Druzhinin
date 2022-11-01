d1, d2, K = input('Введите D1: '), input('Введите D2: '), input('Введите K: ')

while 1:  # Обработка исключений
    try:
        d1, d2, K = int(d1), int(d2), int(K)
        break
    except ValueError:
        print('Wrong input')
        d1, d2, K = input('Введите D1: '), input('Введите D2: '), input('Введите K: ')


def add_right_digit(d, k):
    return k * 10 + d


print(add_right_digit(d1, K))
print(add_right_digit(d2, K))
