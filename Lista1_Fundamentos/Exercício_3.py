import numpy as np

## Fazendo a sequencia de números 
#iniciando com os parametros 
N = 5 # limite máximo
x_0 = 0.1 #valor inicial para x
a  = 3 # constante 


#criando uma lista que se inicia no valor inicial de x
valores_x = [x_0]

#laço de repetição que calcula para cada valor inserido no valores de x
for i in range(1, N):
    x_n  = a * valores_x[i-1] * (1 - valores_x[i-1])
    valores_x.append(x_n) #==> "Gruda os valores de x_n em valores_x"
#print(valores_x) #==> mostra a lista já feita dos valores calulados

print('\nUsando a mão de obra para realizar as contas\n')

# Média
somatorio = 0 #== a somatorio se inicia em 0
for i in valores_x: # o loop vai de i (iniciado em 0) e percorre todos so valores de a (um a um)
    somatorio = somatorio + i # cada vez que acontence o loop o argumento somatorio tem um acrecimo do indice i
print(f'Usando a mão de obra para a média, temos: {somatorio / N}') # imprime somatorio 


omega = 0
for n in valores_x:
    omega += (n - (somatorio / N)) **2 #soma o quadrado da direfença
print(f'Usando a mão de obra para a variância, temos: {omega / (N-1)}')

print('\nUsando a biblioteca numpay para realizar as contas\n')

media = np.array(valores_x)
result_media = np.mean(media)
print(f'Usando a biblioteca para a média, temos: {result_media}')

variancia = np.array(valores_x)
result_variancia = np.var(variancia, ddof = 1)
print(f'Usando a biblioteca para a variança, temos: {result_variancia}')

