# Дано целое число N (>1). Вывести наименьшее из целых чисел K, для которых сумма 1 + 2 + … + K будет больше или
# равна N, и саму эту сумму.
n = input('Введите N: ')

while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Неправильный ввод')
        n = input('Введите N: ')

k = 0
s = 0

while s < n:
    k += 1
    s += k

print(f'k = {k}\ns = {s}')
