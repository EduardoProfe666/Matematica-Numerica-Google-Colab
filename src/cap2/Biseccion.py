import math
import pandas as pd


# --------------- Backend --------------- #
class ResultadoBiseccion:
    def __init__(self, a, b, x, fx, fa, fb, error):
        self.a = a
        self.b = b
        self.x = x
        self.fx = fx
        self.fa = fa
        self.fb = fb
        self.error = error


def biseccion(f, a, b, tol):
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")

    retorno = [[]]
    mitad = (a + b) / 2
    condicion = True

    while condicion:
        f_a = f(a)
        f_b = f(b)
        f_mitad = f(mitad)
        error = (b - a) / 2

        retorno[0].append(ResultadoBiseccion(a, b, mitad, f_mitad, f_a, f_b, error))

        if error < tol:
            retorno.append(mitad)
            condicion = False
        elif f_a * f_mitad > 0:
            a = mitad
        elif f_a * f_mitad < 0:
            b = mitad
        mitad = (a + b) / 2

    return retorno


def convertir_resultados(lista_resultados_biseccion):
    lista = []
    for r in lista_resultados_biseccion:
        l = []
        l.append('{:.7f}'.format(r.a))
        l.append('{:.7f}'.format(r.x))
        l.append('{:.7f}'.format(r.b))
        l.append('{:.7f}'.format(r.fa))
        l.append('{:.7f}'.format(r.fx))
        l.append('{:.7f}'.format(r.fb))
        l.append('{:.7f}'.format(r.error))
        lista.append(l)

    df = pd.DataFrame(data=lista, columns=['a', 'x', 'b', 'f(a)', 'f(x)', 'f(b)', 'Em(x)'])
    df = df.reset_index(drop=True)
    df.index = df.index + 1
    df.index.name = 'Iteración'
    return df


# ---------------- Insercion de datos ------------- #
f = lambda x: math.log(x) - math.sin(x)
a = 1
b = 3
tol = 0.005

# ---------------- Salida de datos --------------- #
r = biseccion(f, a, b, tol)
print('Raíz hallada con método de bisección: {:.7f}'.format(r[1]))
print(convertir_resultados(r[0]))
