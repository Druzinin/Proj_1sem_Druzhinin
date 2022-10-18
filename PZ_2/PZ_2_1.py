N = input('Input number ')

while type(N) != int:  # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print('Wrong input')
        N = input('input number ')

N = N // 3600
print(N)
