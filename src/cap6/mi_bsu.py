from numpy import *

def bsu(f, x0, s, max):
    i = 1
    x1 = x0
    x2 = x1 + s
    x3 = x2 + s

    y1 = f(x1)
    y2 = f(x2)
    y3 = f(x3)

    print ("{}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}".format(i, x1, x2, x3, y1, y2, y3) )

    if max:
        while y3 > y2:
            x1 = x1 + s
            x2 = x2 + s
            x3 = x3 + s

            y1 = f(x1)
            y2 = f(x2)
            y3 = f(x3)

            i += 1
            print("{}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}".format(i, x1, x2, x3, y1, y2, y3))
    else:
        while y3 < y2:
            x1 = x1 + s
            x2 = x2 + s
            x3 = x3 + s

            y1 = f(x1)
            y2 = f(x2)
            y3 = f(x3)

            i += 1

        print ("{}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}\t {:.5f}".format(i, x1, x2, x3, y1, y2, y3) )

    if max:
        print(f"El punto máximo es: y = {y2} y se alcanza en x = {x2}")
    else:
        print(f"El punto mínimo es: y = {y2} y se alcanza en x = {x2}")

print ("{:<3}\t {:<7}\t {:<7}\t {:<7}\t {:<7}\t {:<7}\t {:<7}".format("i", "x1", "x2", "x3", "y1", "y2", "y3") )
print ('-' * 105)
f = lambda x: sin(x)
x0 = 0
s = 0.1

bsu(f,x0,s,True)

