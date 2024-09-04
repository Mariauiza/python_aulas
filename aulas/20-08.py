# BIBLIOTECA NUMPY
import numpy as np  ##  importa a biblioteca numpy 
## para usar uma função função.np

## NOTAS:
# Array: variável especial que pode conter mais de um valor por vez => armazenas valores, são LISTAS
# Matriz -> conter muitos valores sob um único nome, e você pode acessar os valores consultando um número de índice.


## declaração de vetores

vec = np.array([1.0, 2.0, 3.0])
#print(vec, '\n') => #[1. 2. 3.]

## print(vec = [0]) como pegar um elemento específico do vetor

## declaração de matrizes => 'listas de listas' 

mat = np.array([[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
#print(mat) => #[[1 2 3]
           #[4 5 6]
           #[7 8 9]]

## MATRIZES 'ESPECIAIS'
    ## Matriz nula = np.zeros (shape = (m,n), dtype =np.float64)
# mat_zero = np.zeros(shape = (4,3), dtype = np.float64)
# print(mat_zero,'\n')

#  ## Matriz identidade = np.ident (n, dtype = np.float64)
# mat_identidade = np.identity(3, dtype = np.float64)
# print(mat_identidade,'\n')

#  ## Matriz Diagonal = np.diag ([numeros que vão na diagonla])
# mat_diag = np.diag([1.0, 2.0, 6.0, 8.0]) # => pega uma lista de números e coloca na diagonal
# print(mat_diag,'\n')


#  ## Matriz de um valor = np.ident (n, dtype = np.float64)
# mat_ones = np.ones(shape=(2,3), dtype = np.float64)
# print(mat_ones,'\n')
# print(3*mat_ones,'\n')


 ## Matriz randonica = np.random.rand (nxn)
# mat_randonicas = np.random.rand(2,3)
# print(mat_randonicas,'\n')


##MULTIPLICAÇÃO ENTRE MATRIZES
m = 2
r = 3
n = 1

A = np.random.rand(m, r)
B = np.random.rand(r, n)
C = np.zeros(shape=(m, n), dtype=np.float64)

for i in range(m): # => percorre as linhas 
    for j in range(n):  
        C[i, j]= 0.0
        for k in range(r):
            C[i,j] += A[i,k]*B[k,j]
print(C)

## MULTIPLICAÇÃO ENTRE MATRIZES => OUTRAS NOTAÇÕES 
C = A @ B
C = A.dot(B)

##MULTIPLICAÇÃO ENTRE MATRIZES
# mat_randonicas1 = np.random.rand(2,3)
# mat_randonicas2 = np.random.rand(2,3)
# mat_mult = mat_randonicas1 * mat_randonicas2
# print(f' {mat_randonicas1} \n\n X \n\n{mat_randonicas2}\n\n = \n\n {mat_mult} ')
