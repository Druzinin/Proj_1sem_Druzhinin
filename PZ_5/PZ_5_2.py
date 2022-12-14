# Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K справа цифру D. С помощью этой
# функции вывести результаты добавления к данному числу K цифр D1 и D2.
d1, d2, K = input('Введите D1: '), input('Введите D2: '), input('Введите K: ')  # Ввод данных

while 1:  # Обработка исключений
    try:
        d1, d2, K = int(d1), int(d2), int(K)
        break
    except ValueError:
        print('Неправильный ввод')
        d1, d2, K = input('Введите D1: '), input('Введите D2: '), input('Введите K: ')


def add_right_digit(d, k):  # Объявление функции
    return k * 10 + d


print(add_right_digit(d1, K))  # Вызов и вывод функций
print(add_right_digit(d2, K))
