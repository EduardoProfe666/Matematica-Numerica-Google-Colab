from numpy import array, absolute, copy, zeros
import pandas as pd


def convertir_matriz_M(a):
    matrizM = array(a, dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[0]):
            if i != j:
                matrizM[i][j] = (a[i][j] * (-1)) / a[i][i]
            else:
                matrizM[i][i] = 0
    return matrizM


matrizA = array([[1, 8, 2], [6, -2, 3], [-1, 1, 4]])
matrizConvertida = convertir_matriz_M(matrizA)
print(pd.DataFrame(matrizConvertida))


def convertir_matriz_C(a, b):
    matrizC = array(b, dtype=float)
    for i in range(b.shape[0]):
        matrizC[i] = b[i] / a[i][i]
    return matrizC


matrizB = array([7,8,4])
matrizCconvertida = convertir_matriz_C(matrizA, matrizB)
print(pd.DataFrame(matrizCconvertida.transpose()))
