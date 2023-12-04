import math

import pandas as pd
from sympy import *
from sympy.abc import x

init_printing(use_latex="mathjax")


def calcular_h(a, b, n):
    return (b - a) / n


def trapecios(f, a, b, n):
    h = calcular_h(a, b, n)
    f = lambdify(x, f)
    resultado = 0
    contador = 0

    for i in range(n + 1):
        if i == 0 or i == n:
            resultado += f(contador) / 2
        else:
            resultado += f(contador)
        contador += h

    return h * resultado


def tabla_xy(f, n):
    fx = lambdify(x, f)
    lista = []
    h = calcular_h(a, b, n)
    contador = 0

    for _ in range(n + 1):
        lista.append(['{:.7f}'.format(contador), '{:.7f}'.format(fx(contador))])
        contador += h

    df = pd.DataFrame(data=lista, columns=['xi', 'f(x)'])
    df.index.name = 'i'
    return df


f = sin(x)
a = 0
b = math.pi
n = 100000

print(f'Resultado: {trapecios(f, a, b, n)}')
print(f'h: {calcular_h(a, b, n)}')
print(tabla_xy(f, n))