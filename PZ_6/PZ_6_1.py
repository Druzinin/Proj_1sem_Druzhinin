from random import randint
n = input('Input N')
lst = []
k = 0

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Wrong input')
        n = input()

a = [randint(0, 9) for _ in range(n)]

for i in a:
    if k % 2:
        lst.append(i)
    k += 1

print(*a)
print(*lst)
