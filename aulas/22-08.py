from matplotlib import pyplot as plt
import numpy as np

## é necessário definir a função que vai ser plotada 
def f(x):
    val = (np.sin(x))**2 * np.exp(-x)
    return val
## print(f(0.0))

#cria um vetor usando numpy com os valores de x 
x = np.linspace(0.0, 5.0, 10)
print(x)

## outra forma
N = 5
x = np.linspace(0.0, 5.0, N)
y = np.zeros(N, dtype=np.float64) # => np.zeros: 'matriz nula'

for i, xeveal in enumerate(x):
    y[i] = f(xeveal)

## outra forma 
for i in range(N):
    y[i] = f(x[i])


y = f(x)
print(y)

plt.plot(x,y)
plt.show()
