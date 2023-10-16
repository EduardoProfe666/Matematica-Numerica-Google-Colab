import pandas as pd
from sympy import *
from sympy.abc import x

init_printing(use_latex="mathjax")


class ResultadoNewtonRaphson:
    def __init__(self, x, fx, dxfx, error, primera_iter):
        self.x = x
        self.fx = fx
        self.dxfx = dxfx
        self.error = error
        self.primera_iter = primera_iter


def newton_raphson(f, x_0, tol):
    x_anterior = x_0
    condition = True
    x_r = 0.0
    f1 = lambdify(x, f)
    f_dx = lambdify(x, diff(f, x))
    f = f1
    retorno = [[ResultadoNewtonRaphson(x_0, f(x_0), f_dx(x_0), 0, True)]]

    while condition:
        x_r = x_anterior - f(x_anterior) / f_dx(x_anterior)
        error = abs(x_r - x_anterior)

        retorno[0].append(ResultadoNewtonRaphson(x_r, f(x_r), f_dx(x_r), error, False))
        x_anterior = x_r
        condition = error > tol

    retorno.append(x_r)
    return retorno


def convertir_resultados(lista_resultados_nr):
    lista = []
    for r in lista_resultados_nr:
        l = ['{:.7f}'.format(r.x), '{:.7f}'.format(r.fx), '{:.7f}'.format(r.dxfx)]
        if r.primera_iter:
            l.append('---------')
        else:
            l.append('{:.7f}'.format(r.error))
        lista.append(l)

    df = pd.DataFrame(data=lista, columns=['xi', 'f(x)', 'f\'(x)', 'Em(x)'])
    df.index.name = 'Iteración'
    return df


x0 = 1
tol = 0.0005
f = x * exp(x) - 2

r = newton_raphson(f, x0, tol)
print('Raíz hallada con método de Newton-Raphson: {:.7f}'.format(r[1]))
print(convertir_resultados(r[0]))
