import matplotlib.pyplot as plt
from typing import List
from src.utils.colors import get_colormap

def show_grid(grid: List[List[int]], delay: float = 0.2):
    """Exibe o grid no modo interativo usando Matplotlib."""
    plt.clf()
    plt.imshow(grid, cmap=get_colormap(), vmin=0, vmax=11)
    plt.xticks([])
    plt.yticks([])
    plt.pause(delay)

def print_grid(grid: List[List[int]]):
    """Imprime o grid no console."""
    for row in grid:
        print(" ".join(map(str, row)))
    print() 