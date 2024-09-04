# Cada nó pertencerá a um array e terá dois atributos base, suas coordenadas
import matplotlib.pyplot as plt
import random as rand

# Cria um dict que armazena o objeto nó, e suas coordenadas
def newKnot(ax: plt.Axes.scatter, x, y):
    _knot = ax.scatter(x, y)
   
    knot = {
        "knot": _knot,
        "x": x,
        "y": y
    }
    return knot

# Cria uma conexão entre nós
def createLine(ax, knotA, knotB):
    xA = knotA["x"]
    yA = knotA["y"]
   
    xB = knotB["x"]
    yB = knotB["y"]
   
    ax.plot([xA, xB], [yA, yB])

fig, ax = plt.subplots()

ax.set_ylim(top=10)
ax.set_xlim(right=10)

# Lista de nós
knots = []

for i in range(10):
    xRand = rand.randrange(0, 10)
    yRand = rand.randrange(0, 10)
   
    knots.append(newKnot(ax, xRand, yRand))

for i in range(10):
    createLine(ax, knots[rand.randrange(0, 10)], knots[rand.randrange(0, 10)])

plt.show()