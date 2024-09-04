# impotando as bibliotecas 

import numpy as np
import time
from matplotlib import pyplot as plt


time_inicial_for = time.time()

# a função f_matriz recebe os parametros m, n e r, que são as dimensões da sua matriz
def f_matriz(m, n, r):

    ## definição das matrizes randonicas
    A = np.random.randint(0, 10, size = (m, r))
    B = np.random.randint(0, 10, size = (r, n))
    C = np.random.zeros(shape = (m,n), dtype = np.int32)

    ## multiplicação com 'for'
    for i in range(m): ##vare as colunas
        for j in range(n):
            C[i,j] = 0.0 #=> a matriz C está iniciada em z
            for k in range(r):
                C[i,j] += A[i, k]*B[k, j] #=> aqui de fato ocorre a multiplicação
    return C
n_dim = [[2,2,2], [3,3,3]]
print(f'Usando for, A X B = \n {C}')