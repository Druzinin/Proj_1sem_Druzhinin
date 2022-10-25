from random import randint

a = [randint(0, 9) for _ in range(10)]
print(a)
b = tuple(filter(lambda x: x % 2 == 0, a))
print(len(b))
print(*b)
