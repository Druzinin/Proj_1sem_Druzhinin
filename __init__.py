def add_left_digit(d, k):  # Объявление функции
    k = int(str(d) + str(k))
    return k


K = input('Введите целое число K: ')  # Ввод данных
D1 = input('Введите целое число D1, в диапазоне 1-9: ')
D2 = input('Введите целое число D2, в диапазоне 1-9: ')

while True:  # Обработчик исключений
    try:
        K, D1, D2 = int(K), int(D1), int(D2)
        break
    except ValueError:
        K, D1, D2 = input("Введите число K без лишних символов: "), input(
            "Введите число D1 без лишних символов: "), input("Введите число D2 без лишних символов: ")

print(add_left_digit(D1, K))  # Вывод первого результата
print(add_left_digit(D2, K))  # Вывод второго результата
