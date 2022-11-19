from numpy import linalg
from copy import deepcopy
a = [[1, 0, 5],
     [2, 2, -1],
     [4, 1, 3]]
b = [[5, 10],
     [4, 8]]
print(linalg.inv(a))


def func_det(x):
    dl = len(x)
    if dl == 2:
        return x[0][0] * x[1][1] - x[0][1] * x[1][0]
    else:
        for i in range(dl):
            x[i] += x[i][:2]
        s = 0
        for t in range(dl):
            n, m = 1, 1
            for p in range(dl):
                n *= x[p][t + p]
                m *= x[(dl - 1) - p][t + p]
            s += n - m
        return s


def inverse_matrix(lst):
    det = func_det(lst)
    if not det:
        print('Не существует')
        return
    else:
        print(f'1)\ndet: {det}\n2)')
    ln = len(lst)
    a_ij = [[0] * ln for _ in range(ln)]
    for i in range(ln):
        for j in range(ln):
            m = deepcopy(lst)
            del m[i]
            for n in range(ln-1):
                del m[n][j]
            det_m = func_det(m)
            a_ij[i][j] = det_m * (-1) ** (i+1 + j+1)
    print(*a_ij, sep='\n')
    a_ij_t = [[r[k] for r in a_ij] for k in range(ln)]
    print('3)', *a_ij_t, sep='\n')
    inv_lst = [[0.0] * ln for _ in range(ln)]
    for i in range(ln):
        for j in range(ln):
            inv_lst[i][j] = a_ij_t[i][j] * (1 / det)
    print('4)')
    print(*inv_lst, sep='\n')


inverse_matrix(a)
print()
inverse_matrix(b)

# def minor(A, i, j):
#     M = copy.deepcopy(A)
#     del M[i]
#     for i in range(len(A[0]) - 1):
#         del M[i][j]
#     return M
#
# Нахождение обратной матрицы, и Детерминанта, примеры на Python
#
#
# def determinant(d, lst):  # функция вычисления детерминанты
#     det = 0
#     if d == 1:
#         det = lst[0]
#     if d == 2:
#         det = lst[0] * lst[3] - lst[2] * lst[1]
#     if d == 3:
#         det = lst[0] * lst[4] * lst[8] + lst[1] * lst[5] * lst[6] + lst[2] * lst[3] * lst[7] - lst[6] * lst[
#             4] * lst[2] - lst[7] * lst[5] * lst[0] - lst[8] * lst[3] * lst[1]
#     if d > 3:
#         det = 0
#         i = 0
#         for j in range(d):
#             det += lst[i * d + j] * cofactor(d, lst, i, j)
#     return det
#
#
# def minor(dim, data, i, j):
#     new_matrix = []
#     for k in range(dim * dim):
#         if int(k / dim) != i and k % dim != j:
#             new_matrix.append(data[k])
#     return determinant(dim - 1, new_matrix)
#
#
# def cofactor(dim, data, i, j):  # функция вычисления кофактора
#     return pow(-1, i + j) * minor(dim, data, i, j)
#
#
# def cofactor_matrix(dim, data):  # функция вычисления ко факторной матрицы
#     new_matrix = []
#     for i in range(dim):
#         for j in range(dim):
#             new_matrix.append(cofactor(dim, data, i, j))
#     return new_matrix
#
#
# def transpose_matrix(dim, data):
#     new_matrix = []
#     for i in range(dim):
#         for j in range(dim):
#             new_matrix.append(data[j * dim + i])
#     return new_matrix
#
#
# def ad_joint_matrix(dim, data):
#     return transpose_matrix(dim, cofactor_matrix(dim, data))
#
#
# matrix = [[2, 2, 1, 2, 5], [1, 3, 3, 1, 3], [1, 2, 2, 1, 3], [4, 2, 2, 3, 8], [1, 5, 2, 1, 1]]  # Пример матрицы
# matrix.clear()
# matrix = a.copy()
# data = []  # создаем пустую матрицу
# for i in range(len(matrix)):  # создаем счетчик итераций на основе размера матрицы matrix
#     for j in range(len(matrix)):  # создаем счетчик итераций на основе размера матрицы matrix
#         data = data + [matrix[i][j]]  # переводим квадратную матрицу matrix в плоскую
# dim = len(matrix)  # размер матрицы
# dim2 = dim * dim  # находим квадрат
# det = determinant(dim, data)  # находим детерминант
# print('Детерминант: |A| =: ', det)
#
# print()
# print('Обратная матрица : ')
# print()
# if det:  # если матрица имеет детерминант не равный нулю
#     adj_matrix = ad_joint_matrix(dim, data)  # находим значение строк матрицы
#     for n in range(dim2):  # создаем счетчик итерации
#         cs = int((adj_matrix[n]) / det)  # находим значение ячейки матрицы
#         if cs < 0:  # условие при котором значение меньше нуля
#             pr = "   "  # 3 пробела для форматирования
#         else:  # иначе
#             pr = "    "  # 4 пробела для форматирования
#         g = pr + str(cs) + "    "  # конкатенация пробелов и значения ячейки матрицы
#         print(g)  # выводим значение переменной g
#         if n % dim == dim - 1:  #
#             print('')  # пустая строка
# else:
#     print('Это вырожденная матрица, обратную матрицу найти невозможно')
