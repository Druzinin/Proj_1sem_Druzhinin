n = input('Input number ')

while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Wrong input')
        n = input('Input number ')

if 0 < n < 3:
    print('зима')
elif 2 < n < 6:
    print('весна')
elif 5 < n < 9:
    print('лето')
elif 8 < n < 12:
    print('осень')
elif n == 12:
    print('зима')
else:
    print('Wrong input')
