# Дан целочисленный список А размера N. Переписать в новый целочисленный список B все четные числа из исходного
# списка (в том же порядке) и вывести размер полученного список В и его содержимое.
from random import randint  # Импортирование модуля random

n = input('Введите N: ')  # Ввод данных
B = []

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Неправильный ввод')
        n = input('Введите N: ')

A = [randint(0, 9) for _ in range(n)]  # Генерация списка
print('Исходный список:', A)

for i in A:
    if i % 2 == 0:
        B.append(i)  # Добавление четных чисел в список B

print('Размер списка B:', len(B))  # Вывод результата
print('Список B -', B)
