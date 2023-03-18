# 1
# from random import randint
# n, m = 5, 5
# matrix2 = [[randint(0, 100) for _ in range(m)] for _ in range(n)]
# print(*matrix2, sep='\n')
#
# transpose = list(zip(*matrix2))
# array = {*matrix2[0], *matrix2[-1], *transpose[0], *transpose[-1]}
# matrix1 = [[j for j in i[1:-1] if j not in array] for i in matrix2[1:-1]]
# print(f'\n{array}\n')
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
# array = sum(matrix, [])
# print(min(array), max(array))


# 4
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# print(sum(filter(lambda x: x < 0, sum(matrix[:round(n / 3)], []))))


# 5
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if i == j:
#             matrix[i][j] <<= 1
#
# print()
# print(*matrix, sep='\n')


# 6
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# array = tuple(filter(lambda x: x > 0 and x % 2 == 0, sum(matrix, [])))
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
#             matrix[i][j] *= 2
#
# print()
# print(*matrix, sep='\n')


# 8
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 1) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print(any(filter(lambda x: x > 0, sum(matrix, []))))


# 9
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     matrix[i][1] **= 2
#
# print()
# print(*matrix, sep='\n')


# 10
# print(*[[0 if (r := __import__('random').randint(1, 10)) % 2 else r for _ in range(5)] for _ in range(5)], sep='\n')


# 11
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     matrix[i][0] **= 3
#
# print()
# print(*matrix, sep='\n')


# 12
# print(*[[0 if (r := __import__('random').randint(0, 15)) > 10 else r for _ in range(5)] for _ in range(5)], sep='\n')


# 13
# from random import randint
# n, m = 5, 5
# N = 4
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     matrix[N - 1][i] += 3
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
#     matrix[i][m - 1] = -1
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
#     matrix[i][N - 1] *= 2
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
#     matrix[n - 1][i] = 0
#
# print()
# print(*matrix, sep='\n')


# 17
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print()
#
# array = [randint(0, 9) for _ in range(n)]
# print(array)
#
# for i in range(n):
#     matrix[i][1] = array[i]
#
# print()
# print(*matrix, sep='\n')


# 18
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = tuple(filter(lambda x: x > 0 and x % 3 == 0, sum(matrix, [])))
# print(f'\n{array}\n{sum(array) / len(array)}')


# 19
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print()

# array = [randint(0, 9) for _ in range(m)]
# print(array)
#
# for i in range(n):
#     matrix[2][j] = array[i]
#
# print()
# print(*matrix, sep='\n')


# 20
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# array = tuple(filter(lambda x: x > 0, sum(matrix, [])))
# print(f'\n{array}\n{sum(array) / len(array)}')


# 21
# from random import randint
# from math import prod
# n, m = 5, 5
# N = 4
# matrix = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     array.append(matrix[N - 1][i])
#
# print()
# print(sum(array), prod(array))


# 22
# from random import randint
# n, m = 5, 5
# matrix = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(round(n / 2), n):
#     for j in range(m):
#         array.append(matrix[i][j])
#
# print()
# print(sum(array))


# 23
# from random import randint
# from math import prod
# n, m = 5, 5
# N = 4
# matrix = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = []
#
# for i in range(n):
#     array.append(matrix[i][N - 1])
#
# print()
# print(sum(array), prod(array))


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
# print()
# print(*[sum(i) / len(i) for i in matrix[::2]], sep='\n')


# 26
# from random import randint
# n, m = 5, 5
# matrix = [[randint(-9, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# print(max(filter(lambda x: x > 0 and x % 4 == 0, sum(matrix, []))))


# 27
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print()
# print(*map(sum, tuple(zip(*matrix))[1::2]))


# 28
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print(min(tuple(zip(*matrix))[m - 2]))


# 29
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = tuple(map(sum, zip(*matrix)))
#
# for i in range(n):
#     matrix[1][i] = array[i]
#
# print()
# print(*matrix, sep='\n')


# 30
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print()
# print(min(matrix[n - 2]))


# 31
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# array = tuple(map(sum, matrix))
#
# for i in range(n):
#     matrix[i][2] = array[i]
#
# print()
# print(*matrix, sep='\n')


# 32 -> 22
# 33 хз
# 34
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
# print()
# print(sum(matrix[0] + matrix[1]))


# 35
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] % 3 == 0:
#             matrix[i][j] *= 3
#
# print()
# print(*matrix, sep='\n')


# 36
# from random import randint
# n, m = 5, 5
# matrix = [[randint(0, 9) for _ in range(m)] for _ in range(n)]
# print(*matrix, sep='\n')
#
# array = sum(tuple(zip(*matrix))[-2:], ())
# print(sum(array) / len(array))


# 37 -> 36
# 38 -> 1
# 39 -> 34
# 40 -> 3
# 41 -> 30
# 42 -> 5
# 43 -> 28
# 44 -> 25
# 45 -> 26
# 46 -> 7
# 47 -> 24
# 48 -> 25
# 49 -> 22
# 50 -> 9
# 51 -> 20
# 52 -> 11
# 53 -> 18
# 54 -> 13
# 55 -> 16
# 56 -> 15
# 57 -> 14
# 58 -> 19
# 59 -> 12
# 60 -> 7
# 61 -> 10
# 62 -> 17
# 63 -> 8
# 64 -> 21
# 65 -> 6
# 66 -> 23
