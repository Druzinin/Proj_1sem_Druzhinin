from random import randint
n = int(input())

a = [randint(0, 9) for _ in range(n)]
print(*filter(lambda x: a.index(x) % 2, a))
