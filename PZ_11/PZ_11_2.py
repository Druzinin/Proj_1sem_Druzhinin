new_file = open('new_file.txt', 'w')
lst = open('text18-27.txt').readlines()
print(*lst, ''.join(lst).count(' '))
