# Дан список A размера N. Найти минимальный элемент из его элементов с четными номерами: А2, А4, А6, …
from random import randint  # Импортирование модуля randint

n = input('Введите N: ')  # Ввод данных
lst = []
k = 0

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Неправильный ввод')
        n = input('Введите N: ')

a = [randint(0, 9) for _ in range(n)]  # Генерация списка
print('Исходный список:', a)

for i in a:  # Добавление элементов с четными индексами
    if k % 2 == 0:
        lst.append(i)
    k += 1

print(min(lst))
