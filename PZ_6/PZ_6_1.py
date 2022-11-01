# Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами: A2, A4, A6 …
from random import randint  # Импортирование библиотеки random
n = input('Введите N: ')
lst = []
k = 0

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Неправильный ввод')
        n = input('Введите N: ')

a = [randint(0, 9) for _ in range(n)]

for i in a:  # Добавление элементов с четными индексами
    if k % 2 == 0:
        lst.append(i)
    k += 1

print('Исходный список:', a)
print(min(lst))
