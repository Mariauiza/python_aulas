

## --somatório
## soma_a = 0
## for i in range(size_a) 



## --produtório
## --for bj in b
## -- prod_b *= bj 
## print(prod_b)



## exemplo 
# a = [[1 ,3, 5, 6], [4, 6, 6, 3], [4, 6, 6, 3]] ==> criação de uma lista que contém três listas como sendo seus elementos 
# size_a = len(a) tamanho de a => quantos elementos tem na lista => print (len(a)) 
# inicia a soma de a em 0, inicia um contador for que se inicia em i e conta o "comprimento de a", e dentro colocamos outro contador que 
# percorre cada lista, depois soma um a um e tira um print;

import time 

tempo_inicial = time.time()


def H (a,b,c):
    soma = a + b +c
    prod = a*b*c
    return soma, prod
A = H(1,5,3)
print (A)

tempo_total = time.time() - tempo_inicial 
print(tempo_total)#quanto tempo demorou para discorrer o código