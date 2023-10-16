import math
import pandas as pd


# --------------- Backend --------------- #
class ResultadoSecantes:
    def __init__(self, x, fx, error, primera_iter):
        self.x = x
        self.fx = fx
        self.error = error
        self.primera_iter = primera_iter


def secantes(f, x0, x1, tol):
    if f(x0) * f(x1) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")

    f_x0 = f(x0)
    f_x1 = f(x1)
    error = tol + 1
    xr = 0.0
    retorno = [[]]
    retorno[0].append(ResultadoSecantes(x0, f_x0, 0, True))
    retorno[0].append(ResultadoSecantes(x1, f_x1, 0, True))

    while error > tol:
        xr = x1 - ((x1 - x0) / (f_x1 - f_x0)) * f_x1
        f_xr = f(xr)
        error = abs(xr - x1)
        retorno[0].append(ResultadoSecantes(xr, f_xr, error, False))

        x0 = x1
        f_x0 = f(x0)
        x1 = xr
        f_x1 = f(x1)

    retorno.append(xr)
    return retorno


def convertir_resultados(lista_resultados_secantes):
    lista = []
    for r in lista_resultados_secantes:
        l = ['{:.7f}'.format(r.x), '{:.7f}'.format(r.fx)]
        if r.primera_iter:
            l.append('---------')
        else:
            l.append('{:.7f}'.format(r.error))
        lista.append(l)

    df = pd.DataFrame(data=lista, columns=['xi', 'f(x)', 'Em(x)'])
    df.index.name = 'Iteración'
    return df


# ---------------- Insercion de datos ------------- #
f = lambda x: x * math.e ** x - 2
x0 = 1
x1 = 0
tol = 0.0005

# ---------------- Salida de datos --------------- #
r = secantes(f, x0, x1, tol)
print('Raíz hallada con método de secantes: {:.7f}'.format(r[1]))
print(convertir_resultados(r[0]))
