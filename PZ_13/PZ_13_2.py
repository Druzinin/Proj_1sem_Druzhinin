# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.

from random import randint  # Импортирование модуля
n, m = map(int, input('Введите размер матрицы (два целых числа через пробел): ').split())  # Ввод данных
N = int(input(f'Введите номер строки (<= {n}): '))
matrix = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]  # Генерация матрицы
print('Исходная матрица: ', *matrix, sep='\n')

for i in range(n):  # Циклы для перебора элементов матрицы
    for j in range(m):
        if i == N - 1:
            matrix[i][j] += 3  # Увеличение элементов в строке N на 3

print('\nИзмененная матрица: ')  # Вывод результата
print(*matrix, sep='\n')
