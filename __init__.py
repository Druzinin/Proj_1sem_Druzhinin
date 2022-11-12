from random import randint
n = 10
x, y = 0, 0
lst = []

a = [randint(0, 9) for _ in range(n)]
print(a)

k = abs(a[0] - a[1])

for i in range(1, n-1):
        m = abs(a[i - 1] - a[i])
        lst.append(m)
        if k > m:
            k = m
            x, y = i - 1, i

print(lst)
print(x, y)
