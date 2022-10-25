def add_right_digit(d, k):
    return k * 10 + d


d1, d2, K = input('Input D1: '), input('Input D2: '), input('Input K: ')

while 1:
    try:
        d1, d2, K = int(d1), int(d2), int(K)
        break
    except ValueError:
        print('Wrong input')
        d1, d2, K = input('Input D1: '), input('Input D2: '), input('Input K: ')

print(add_right_digit(d1, K))
print(add_right_digit(d2, K))
