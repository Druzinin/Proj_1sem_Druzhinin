# inverse matrix
from copy import deepcopy
a = [[1, 2, 3],
     [0, -1, 2],
     [3, 0, 7]]


def func_det(x):
    dl = len(x)
    if dl == 2:
        return x[0][0] * x[1][1] - x[0][1] * x[1][0]
    else:
        for i in range(dl):
            x[i] += x[i][:2]
        s = 0
        for t in range(dl):
            n, m = 1, 1
            for p in range(dl):
                n *= x[p][t + p]
                m *= x[(dl - 1) - p][t + p]
            s += n - m
        return s


def inverse_matrix(lst):
    det = func_det(lst)
    if not det:
        print('Не существует')
        return
    else:
        print(f'1)\ndet: {det}\n2)')
    ln = len(lst)
    a_ij = [[0] * ln for _ in range(ln)]
    for i in range(ln):
        for j in range(ln):
            m = deepcopy(lst)
            del m[i]
            for n in range(ln - 1):
                del m[n][j]
            det_m = func_det(m)
            a_ij[i][j] = det_m * (-1) ** (i + 1 + j + 1)
    print(*a_ij, sep='\n')
    a_ij_t = [[r[k] for r in a_ij] for k in range(ln)]
    print('3)', *a_ij_t, sep='\n')
    inv_lst = [[0.0] * ln for _ in range(ln)]
    for i in range(ln):
        for j in range(ln):
            inv_lst[i][j] = a_ij_t[i][j] * (1 / det)
    print('4)')
    print(*inv_lst, sep='\n')
    print('5)')
    test = a_ij
    for i in range(ln):
        for j in range(ln):
            s = 0
            for v in range(ln):
                s += inv_lst[i][v] * lst[v][j]
            test[i][j] = round(s)
    print(*test, sep='\n')


inverse_matrix(a)
