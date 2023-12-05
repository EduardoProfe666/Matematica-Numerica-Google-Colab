import pandas as pd
from numpy import array, zeros
import numpy as np


def diferencias_divididas(xi, yi):
    n = len(yi)
    coef = zeros([n, n])
    coef[:, 0] = yi

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (xi[i + j] - xi[i])
            if j == i == 1:
                print(coef[i + 1][j - 1])
                print(coef[i][j - 1])
                print(coef[i + 1][j - 1] - coef[i][j - 1])
                a = coef[i + 1][j - 1] - coef[i][j - 1]
                b = xi[i + j] - xi[i]
                print(xi[i + j])
                print(xi[i])
                print(xi[i + j] - xi[i])
                print(a/b)

    return coef


def convertir_resultados(xi, yi, diferencias_divididas):
    lista = []
    n = len(diferencias_divididas[0])
    for i, r in enumerate(diferencias_divididas):
        l = ['{:.7f}'.format(xi[i]), '{:.7f}'.format(yi[i])]
        for j, diff in enumerate(r):
            if j != 0 and j < n - i:
                l.append('{:.7f}'.format(diff))
            elif j != 0:
                l.append('---------')
        lista.append(l)

    cols = ['xi', 'f(x)']
    for i in range(1, n):
        cols.append('diff ' + str(i))

    df = pd.DataFrame(data=lista, columns=cols)
    df.index.name = 'Iteración'
    return df


xi = array([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5])
yi = array([3, 14, 34, 64, 107, 165, 240, 336, 451, 591])

diffs = diferencias_divididas(xi, yi)
print(convertir_resultados(xi, yi, diffs))
