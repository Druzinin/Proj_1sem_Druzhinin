# Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит во второй или третьей
# координатной четверти».
x, y = input('Input number 1: '), input('Input number 2: ')

while type(x) != int:  # обработка исключений
    try:
        x = int(x)
    except ValueError:
        print('Wrong input')
        x = input('input number 1: ')

while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print('Wrong input')
        y = input('input number 2: ')

print('Да' if x < 0 < y or x < 0 and y < 0 else 'Нет')
