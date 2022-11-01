# Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит во второй или третьей
# координатной четверти».
x, y = input('Введите число 1: '), input('Введите число 2: ')

while 1:  # обработка исключений
    try:
        x, y = int(x), int(y)
        break
    except ValueError:
        print('Wrong input')
        x = input('Введите число 1: ')
        y = input('Введите число 2: ')

if x < 0 < y or x < 0 and y < 0:
    print('Да')
else:
    print('Нет')
