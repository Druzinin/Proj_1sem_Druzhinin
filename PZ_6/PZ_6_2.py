# Дан целочисленный список А размера N. Переписать в новый целочисленный список B все четные числа из исходного
# списка (в том же порядке) и вывести размер полученного список В и его содержимое.
from random import randint
n = input('Input N: ')

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Wrong input')
        n = input('Input N: ')

a = [randint(0, 9) for _ in range(n)]

b = list(filter(lambda x: x % 2 == 0, a))
print('Размер списка:', len(b))
print('Список B -', b)
