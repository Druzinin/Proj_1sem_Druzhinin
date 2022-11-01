# Найти сумму 1 + 1 / 2 + 1 / 3 + 1 / N
N = input('Input number N: ')

while type(N) != int:  # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print('Wrong input')
        N = input('input number N: ')

i = 0
s = 0

while i != N:
    i += 1
    s += 1 / i

print('s =', s)
