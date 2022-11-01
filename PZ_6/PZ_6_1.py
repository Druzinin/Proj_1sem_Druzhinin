# Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами: А2, А4, А6, …
from random import randint
n = input('Введите N: ')
lst = []
k = 0

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Wrong input')
        n = input('Введите N: ')

a = [randint(0, 9) for _ in range(n)]

for i in a:
    if k % 2:
        lst.append(i)
    k += 1

print(*a)
print(*lst)
