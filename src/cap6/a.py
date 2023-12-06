from numpy import *

def biseccion_opt(a, b, f, d, tol=0.0001):
    i = 0

    x1 = (a + b) / 2 - d / 2
    x2 = (a + b) / 2 + d / 2

    y1 = f(x1)
    y2 = f(x2)

    l = b - a

    print("{}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}".format(i, a, b, l, x1, x2, y1, y2))

    while l > tol:
        if y1 < y2:
            a = x1
        else:
            b = x2

        x1 = (a + b) / 2 - d / 2
        x2 = (a + b) / 2 + d / 2

        y1 = f(x1)
        y2 = f(x2)

        l = b - a
        i += 1

        print("{}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}\t {:.7f}".format(i, a, b, l, x1, x2, y1, y2))

    print(f"El intervalo obtenido es: [{a}, {b}]")
    
a = 2.0
b = 2.1
f = lambda x : x * sin(x)
d = 0.0001
tol = 0.001

biseccion_opt(a, b, f, d, tol)