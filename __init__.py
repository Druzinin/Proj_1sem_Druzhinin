from random import randint  # Импортирование модуля randint
N = input('Введите N: ')  # Ввод данных

while type(N) != int:  # Обработка исключений
    try:
        N = int(N)
    except ValueError:
        print('Неправильный ввод')
        N = input('Введите N: ')

a = [randint(0, 9) for i in range(N)]  # Генерация списка
print(a)

k1, k2 = 0, 0
flag = 1

for i in range(1, N):
    if a[i] < a[i - 1]:  # Текущее число меньше предыдущего
        if flag:
            k1 += 1
            flag = 0
    else:
        flag = 1

flag = 1

for i in range(1, N):
    if a[i] > a[i - 1]:  # Текущее число больше предыдущего
        if flag:
            k2 += 1
            flag = 0
    else:
        flag = 1

k = k1 + k2
print(k)  # Вывод результата
