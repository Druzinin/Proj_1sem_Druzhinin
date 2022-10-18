n = input('Input number N: ')

while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Wrong input')
        n = input('input number N: ')

k = 0
s = 0

while s < n:
    k += 1
    s += k

print(f'k = {k}\ns = {s}')
