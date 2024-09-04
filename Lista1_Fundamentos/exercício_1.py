# Importação das bibliotecas necessárias
import random, time, numpy
from matplotlib import pyplot as plt

# Função que calcula vetores e uma matriz elevada à potência m
def calculaVetores(n, m):
    
    # Inicializa o tempo de execução
    time_inicial = time.time()
    
    # Inicializa vetores vazios para armazenar os números aleatórios
    vetor_a = []
    vetor_b = []

    # Preenche os vetores 'vetor_a' e 'vetor_b' com 'n' números aleatórios entre 1 e 10
    for i in range(n):
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        vetor_a.append(num1)
        vetor_b.append(num2)

    # Gera números aleatórios para multiplicar os elementos dos vetores
    alfa = random.randint(1,10)
    beta = random.randint(1,10)

    # Calcula a distribuição 'dist_a' multiplicando cada elemento de 'vetor_a' por 'alfa'
    dist_a = []
    for i in vetor_a:
        dist_a.append(i * alfa)

    # Calcula a distribuição 'dist_b' multiplicando cada elemento de 'vetor_b' por 'beta'
    dist_b = []
    for i in vetor_b:
        dist_b.append(i * beta)

    # Calcula o vetor resultante 'vetor_c' somando os elementos correspondentes de 'dist_a' e 'dist_b'
    vetor_c = []
    for i in range(n):
        vetor_c.append(dist_a[i] + dist_b[i]) 

    # Inicializa uma matriz vazia para armazenar números aleatórios
    matriz = []
    
    # Preenche a matriz com 'n' linhas e 'n' colunas de números aleatórios entre 1 e 9
    for i in range(n):
        A = random.sample(range(1,10), n) 
        matriz.append(A)

    # Eleva a matriz à potência 'm' usando a função 'matrix_power' do numpy
    matriz_pot = numpy.linalg.matrix_power(matriz, m)

    # Calcula o tempo total de execução da função
    time_exec = time.time() - time_inicial

    # Retorna o vetor resultante, a matriz elevada à potência, e o tempo de execução
    return vetor_c, matriz_pot, time_exec

# Define uma lista de diferentes valores para 'n' (dimensões) e 'm' (potências)
n_dimensoes = [4, 2, 6]
m = [2, 3, 4]
list_time_exec = []  # Lista para armazenar os tempos de execução

# Loop para calcular vetores e matrizes para cada par de valores em 'n_dimensoes' e 'm'
for i in range(len(n_dimensoes)):
    vc, mat, temp = calculaVetores(n_dimensoes[i], m[i])
    print('\n', vc, mat, temp)  # Imprime o vetor resultante, a matriz elevada, e o tempo de execução
    list_time_exec.append(temp)  # Armazena o tempo de execução na lista

# Imprime a lista dos tempos de execução
print(f'lista do tempo = {list_time_exec}')

# Cria um gráfico que relaciona o tempo de execução com as dimensões (gráfico normal)
fig, ax = plt.subplots()             
ax.plot(list_time_exec, n_dimensoes)
plt.title('Tempo de Execução vs Dimensão (Escala Linear)')
plt.xlabel('Tempo de Execução (s)')
plt.ylabel('Dimensão (n)')

# Ajusta o layout do gráfico e o exibe
plt.tight_layout()
plt.show() 

# Cria um gráfico log-log usando os mesmos dados
plt.figure(figsize=(8, 6))
plt.loglog(list_time_exec, n_dimensoes, marker='o')
plt.title('Tempo de Execução vs Dimensão (Escala Log-Log)')
plt.xlabel('Tempo de Execução (s)')
plt.ylabel('Dimensão (n)')
plt.grid(True, which="both", ls="--")  # Adiciona grades ao gráfico
plt.tight_layout()
plt.show()
