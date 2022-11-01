# Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K справа цифру D. С помощью этой
# функции вывести результаты добавления к данному числу K цифр D1 и D2.
def add_right_digit(d, k):  # Обьявление функции
    return k * 10 + d


d1, d2, K = input('Input D1: '), input('Input D2: '), input('Input K: ')

while 1:  # Обработка исключений
    try:
        d1, d2, K = int(d1), int(d2), int(K)
        break
    except ValueError:
        print('Wrong input')
        d1, d2, K = input('Input D1: '), input('Input D2: '), input('Input K: ')

print(add_right_digit(d1, K))  # Вызов функции
print(add_right_digit(d2, K))
