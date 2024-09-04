import numpy as np
from matplotlib import pyplot as plt

# Parâmetros iniciais
N = 1000  # Limite máximo de iterações
x_0 = 0.1  # Valor inicial para x
a_valores = np.linspace(0, 4, N)  # Lista de valores para a

# Loop para calcular e plotar a sequência de valores para cada a
for a_x in a_valores:
    valores_x = [x_0]  # Reinicia a lista para cada a_x

    # Calcula a sequência de x_n
    for i in range(1, N):
        x_n = a_x * valores_x[i-1] * (1 - valores_x[i-1])
        valores_x.append(x_n)

    # Plotando os resultados
    plt.plot(a_valores, valores_x, label=f'a = {a_x}')

# Configurações do gráfico
plt.title('Valores obtidos em x_n para cada valor de a')
plt.xlabel('Iteração (n)')
plt.ylabel('Valor de x_n')
#plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()
