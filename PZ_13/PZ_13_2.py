from random import randint
n, m = map(int, input('Введите размер матрицы (два целых числа через пробел): ').split())
N = int(input('Введите номер строки: '))
matrix = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]
print('Исходная матрица: ', *matrix, sep='\n')

for i in range(n):
    for j in range(m):
        if i == N - 1:
            matrix[i][j] += 3

print('Измененная матрица: ')
print(*matrix, sep='\n')
