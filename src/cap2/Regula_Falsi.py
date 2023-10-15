import math
import pandas as pd


# --------------- Backend --------------- #
class ResultadoRegulaFalsi:
    def __init__(self, a, b, x, fx, fa, fb, error, primera_iter):
        self.a = a
        self.b = b
        self.x = x
        self.fx = fx
        self.fa = fa
        self.fb = fb
        self.error = error
        self.primera_iter = primera_iter


def regula_falsi(f, a, b, tol):
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")

    retorno = [[]]
    primera_iter = True
    ultimo_x = 0
    x = 0.0
    condicion = True

    while condicion:
        f_a = f(a)
        f_b = f(b)

        x = a - (b - a) * f_a / (f_b - f_a)
        f_x = f(x)
        error = abs(x - ultimo_x)

        retorno[0].append(ResultadoRegulaFalsi(a, b, x, f_x, f_a, f_b, error, primera_iter))

        if f_a * f_x < 0:
            b = x
        elif f_a * f_x > 0:
            a = x

        ultimo_x = x
        condicion = error > tol
        primera_iter = False

    retorno.append(x)
    return retorno


def convertir_resultados(lista_resultados_regula_falsi):
    lista = []
    for r in lista_resultados_regula_falsi:
        l = ['{:.7f}'.format(r.a), '{:.7f}'.format(r.x), '{:.7f}'.format(r.b), '{:.7f}'.format(r.fa),
             '{:.7f}'.format(r.fx), '{:.7f}'.format(r.fb)]
        if r.primera_iter:
            l.append('---------')
        else:
            l.append('{:.7f}'.format(r.error))
        lista.append(l)

    df = pd.DataFrame(data=lista, columns=['a', 'x', 'b', 'f(a)', 'f(x)', 'f(b)', 'Em(x)'])
    df = df.reset_index(drop=True)
    df.index = df.index + 1
    df.index.name = 'Iteración'
    return df


# ---------------- Insercion de datos ------------- #
f = lambda x: x**2 - math.e**x
a = -1
b = 0
tol = 0.0005

# ---------------- Salida de datos --------------- #
r = regula_falsi(f, a, b, tol)
print('Raíz hallada con método de bisección: {:.7f}'.format(r[1]))
print(convertir_resultados(r[0]))
