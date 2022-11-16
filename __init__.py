lst_x = [0.134, 0.561, 1.341, 2.291]
lst_y = [2.156, 3.348, 3.611, 4.112]
lst = []
n = len(lst_x)

for j in range(n):
    b = 1
    for v in range(n):
        if lst_x[j] != lst_x[v]:
            b *= lst_x[j] - lst_x[v]
    L = [f"(x - {lst_x[i]})" for i in range(n) if lst_x[j] != lst_x[i]]
    lst.append((f'{lst_y[j] * (1 / b)} * (', L))

for i in lst:
    print(i[0], end='')
    print(*i[1], sep=' * ', end=')\n')
