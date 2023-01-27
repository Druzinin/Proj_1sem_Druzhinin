from random import randint
n, m = map(int, input('Введите размер матрицы (два целых числа через пробел): ').split())
matrix = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]
print('Исходная матрица: ', *matrix, sep='\n')

array = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] > 0 and matrix[i][j] % 3 == 0:
            array.append(matrix[i][j])

print('\n', 'Среднее арифметическое чисел: ', sum(array) / len(array))
