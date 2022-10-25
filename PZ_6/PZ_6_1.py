from random import randint
# n = int(input())
n = 10
# a = [randint(0, 9) for _ in range(n)]

a = []
for _ in range(n):
    a.append(randint(1, 100))

print(a)
# print(*filter(lambda x: a.index(x) % 2, a))
for i in a:
    if a.index(i) % 2:
        print(i, end=' ')
