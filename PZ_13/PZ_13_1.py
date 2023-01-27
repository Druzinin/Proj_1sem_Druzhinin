# В матрице найти среднее арифметическое положительных элементов, кратных 3.

from random import randint  # Импортирование модуля
n, m = map(int, input('Введите размер матрицы (два целых числа через пробел): ').split())  # Ввод данных
matrix = [[randint(-10, 10) for _ in range(m)] for _ in range(n)]  # Генерация матрицы
print('Исходная матрица: ', *matrix, sep='\n')

array = []
for i in range(n):  # Циклы для перебора элементов матрицы
    for j in range(m):
        if matrix[i][j] > 0 and matrix[i][j] % 3 == 0:
            array.append(matrix[i][j])  # Добавление в массив элементов, соответствующих условию

print(f'\nСписок: {array}\nСреднее арифметическое элементов: {sum(array) / len(array)}' if array else
      '\nНет подходящих элементов')  # Вывод результата
