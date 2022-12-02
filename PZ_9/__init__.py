# 1
# from random import randint
# n, m = 5, 5
# matrix2 = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix2, sep='\n')
# matrix1 = [[0] * (m - 2) for i in range(n - 2)]
#
# for i in range(1, n - 1):
#     for j in range(1, m - 1):
#         matrix1[i-1][j-1] = matrix2[i][j]
#
# print()
# print(*matrix1, sep='\n')


# 2
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] < 0:
#             matrix[i][j] **= 2
#
# print()
# print(*matrix, sep='\n')


# 3
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# min_number, max_number = matrix[0][0], matrix[0][0]
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] < min_number:
#             min_number = matrix[i][j]
#         if matrix[i][j] > max_number:
#             max_number = matrix[i][j]
#
# print(min_number, max_number)


# 5
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if i == j:
#             matrix[i][j] **= 2
#
# print()
# print(*matrix, sep='\n')


# 6
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > 0 and matrix[i][j] % 2 == 0:
#             array.append(matrix[i][j])
#
# print()
# print(array)
# print(sum(array), sum(array) / len(array))


# 7
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if i != j:
#             matrix[i][j] **= 2
#
# print()
# print(*matrix, sep='\n')


# 8
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 1) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
#
# def f(lst):
#     for i in range(n):
#         for j in range(m):
#             if lst[i][j] > 0:
#                 return True
#     return False
#
#
# print(f(matrix))


# 9
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if j == 1:
#             matrix[i][j] **= 2
#
# print()
# print(*matrix, sep='\n')


# 10
# from random import randint
# n, m = 5, 5
# matrix = []
#
# for i in range(n):
#     matrix.append([0] * m)
#     for j in range(m):
#         r = randint(0, 9)
#         matrix[i][j] = 0 if r % 2 else r
#         if r % 2:
#             print(r)
#
# print(*matrix, sep='\n')


# 11
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if j == 0:
#             matrix[i][j] **= 3
#
# print()
# print(*matrix, sep='\n')


# 12
# from random import randint
# n, m = 5, 5
# matrix = []
#
# for i in range(n):
#     matrix.append([0] * m)
#     for j in range(m):
#         r = randint(0, 15)
#         matrix[i][j] = 0 if r > 10 else r
#         if r > 10:
#             print(r)
#
# print(*matrix, sep='\n')


# 13
# from random import randint
# n, m = 5, 5
# N = 4
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if i == N - 1:
#             matrix[i][j] += 3
#
# print()
# print(*matrix, sep='\n')


# 14
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if j == m - 1:
#             matrix[i][j] = -1
#
# print()
# print(*matrix, sep='\n')


# 15
# from random import randint
# n, m = 5, 5
# N = 4
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if j == N - 1:
#             matrix[i][j] *= 2
#
# print()
# print(*matrix, sep='\n')


# 16
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if i == m - 1:
#             matrix[i][j] = 0
#
# print()
# print(*matrix, sep='\n')


# 17
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print()
# array = [randint(0, 9) for _ in range(n)]
# print(array)
#
# for i in range(n):
#     for j in range(m):
#         if j == 1:
#             matrix[i][j] = array[i]
#
# print()
# print(*matrix, sep='\n')


# 18
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > 0 and matrix[i][j] % 3 == 0:
#             array.append(matrix[i][j])
#
# print()
# print(array)
# print(sum(array) / len(array))


# 19
# from random import randint
# n, m = 5, 3
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print()
# array = [randint(0, 9) for _ in range(m)]
# print(array)
#
# for i in range(n):
#     for j in range(m):
#         if i == 2:
#             matrix[i][j] = array[j]
#
# print()
# print(*matrix, sep='\n')


# 20
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > 0:
#             array.append(matrix[i][j])
#
# print()
# print(array)
# print(sum(array) / len(array))


# 21
# from random import randint
# n, m = 5, 5
# N = 4
# matrix = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     for j in range(m):
#         if i == N - 1:
#             array.append(matrix[i][j])
#
# print()
# print(sum(array))
# s = 1
# for k in array:
#     s *= k
# print(s)


# 22
# from random import randint
# n, m = 5, 5
# matrix = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     for j in range(m):
#         if j > m / 2:
#             array.append(matrix[i][j])
#
# print()
# print(sum(array))


# 23
# from random import randint
# n, m = 5, 5
# N = 4
# matrix = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     for j in range(m):
#         if j == N - 1:
#             array.append(matrix[i][j])
#
# print()
# print(sum(array))
# s = 1
# for k in array:
#     s *= k
# print(s)


# 24
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] < 0:
#             array.append(matrix[i][j])
#
# print()
# print(array)
# print(len(array))


# 25
# from random import randint
# n, m = 5, 5
# matrix = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     if i % 2:
#         continue
#     array.append([0] * m)
#     for j in range(m):
#         array[-1][j] = matrix[i][j]
#
# print()
# for k in array:
#     print(sum(k) / len(k))


# 26
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# max_number = -100
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > max_number:
#             if matrix[i][j] > 0 and matrix[i][j] % 4 == 0:
#                 max_number = matrix[i][j]
#
# print(max_number)


# 27
from random import randint
n, m = 5, 5
matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
print(*matrix, sep='\n')
array = []

for i in range(n):
    s = 0
    for j in range(m):
        if j % 2:
            s += matrix[i][j]
        else:
            continue
    array.append(s)

for i in range(n):
    for j in range(m):
        if i == 1:
            matrix[i][j] = array[j]

print(f'\n{array}\n')
print(*matrix, sep='\n')


# 28
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# min_number = matrix[0][-2]
#
# for i in range(n):
#     for j in range(m):
#         if j == m - 2:
#             if matrix[i][j] < min_number:
#                 min_number = matrix[i][j]
#
# print(min_number)


# # 29
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     s = 0
#     for j in range(m):
#         if j % 2:
#             s += matrix[i][j]
#         else:
#             continue
#     array.append(s)
#
# for i in range(n):
#     for j in range(m):
#         if i == 1:
#             matrix[i][j] = array[j]
#
# print(f'\n{array}\n')
# print(*matrix, sep='\n')


# 30
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# min_number = matrix[-2][0]
# for i in range(n):
#     for j in range(m):
#         if i == n - 2:
#             if matrix[i][j] < min_number:
#                 min_number = matrix[i][j]
#
# print(min_number)


# 31
