# Grid size
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

N = 30
# Create an initial random grid
p0, p1 = 0.8, 0.2
grid = np.random.choice([0, 1], N*N, p=[p0, p1]).reshape(N, N)

def update(frameNum, img, grid):
# Programar as regras de atualizacao
    newGrid = grid.copy()

    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
        if grid[i,j] == 1:
            if total < 2 or total > 3:
                newGrid[i,j] = 0
        else:
            if total == 3:
                newGrid[i,j] = 1
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    plt.title(f"Game of Life - Frame {frameNum}")
    return img,


fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img,grid), frames=10, interval=200, save_count=50)
plt.show()
