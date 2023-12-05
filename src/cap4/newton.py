import pandas as pd
from numpy import array, zeros


def diferencias_divididas(xi, yi):
    n = yi.shape[0]
    coef = zeros((n, n))
    coef[:, 0] = yi

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (xi[i + j] - xi[i])

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


xi = array([1.15, 1.20, 1.10, 1.25, 1.05, 1.30])
yi = array([0.93304, 0.91817, 0.95135, 0.90640, 0.97350, 0.89747])

diffs = diferencias_divididas(xi, yi)
print(convertir_resultados(xi, yi, diffs))
