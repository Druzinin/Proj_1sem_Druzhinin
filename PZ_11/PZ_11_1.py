f1 = open('file 1.txt', 'w')
f2 = open('file 2.txt', 'w')
l1 = ['-3 -5 0 -5 -8 -5 3 -1 -5 3']
l2 = ['-4 -7 5 -1 6 1 8 9 -5 2']
print(*l1, file=f1)
print(*l2, file=f2)
f1.close(), f2.close()

f3 = open('file 3.txt', 'w')
f1, f2 = open('file 1.txt').readline().split(), open('file 2.txt').readline().split()
f1, f2 = list(map(int, f1)), list(map(int, f2))

print('1) Элементы первого и второго файлов:', f1, f2, file=f3)
print('2) Элементы первого файла, присутствующие во втором:', [i for i in f1 if i in f2], file=f3)
print('3) Элементы второго файла, присутствующие в первом:', [i for i in f2 if i in f1], file=f3)
print('4) Количество элементов:', len(f1 + f2), file=f3)
print('5) Количество отрицательных элементов:', [i for i in f1 + f2 if i < 0], file=f3)
print('6) Количество положительных элементов:', [i for i in f1 + f2 if i > 0], file=f3)
f3.close()
print(open('file 3.txt').read())
