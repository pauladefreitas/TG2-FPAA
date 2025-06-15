import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from typing import List, Tuple

COLORS = [
    "#FFFFFF",  # 0 - Branco
    "#000000",  # 1 - Preto
    "#FF0000",  # 2 - Vermelho
    "#FFA500",  # 3 - Laranja
    "#FFFF00",  # 4 - Amarelo
    "#00FF00",  # 5 - Verde
    "#00FFFF",  # 6 - Ciano
    "#0000FF",  # 7 - Azul
    "#800080",  # 8 - Roxo
    "#FFC0CB",  # 9 - Rosa
    "#A52A2A",  # 10 - Marrom
    "#808080",  # 11 - Cinza
]

cmap = mcolors.ListedColormap(COLORS)

def show_grid(grid: List[List[int]], delay: float = 0.2):
    """Exibe o grid no modo interativo usando Matplotlib."""
    plt.clf()
    plt.imshow(grid, cmap=cmap, vmin=0, vmax=len(COLORS) - 1)
    plt.xticks([])
    plt.yticks([])
    plt.pause(delay)

def flood_fill(
    grid: List[List[int]],
    x: int,
    y: int,
    color: int,
    *,
    visualize: bool = False,
):
    """Preenche a região conectada partindo de (x, y) com 'color'."""
    if grid[x][y] != 0:
        return

    rows, cols = len(grid), len(grid[0])
    stack = [(x, y)]
    grid[x][y] = color

    if visualize:
        show_grid(grid)

    while stack:
        i, j = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 0:
                grid[ni][nj] = color
                stack.append((ni, nj))
                if visualize:
                    show_grid(grid)


def find_next_start(grid: List[List[int]]) -> Tuple[int, int]:
    """Encontra a próxima célula livre (valor 0)."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return -1, -1


def fill_all_regions(
    grid: List[List[int]],
    start_x: int,
    start_y: int,
    *,
    visualize: bool = False,
):
    """Preenche todas as regiões livres do grid começando pela posição inicial."""
    current_color = 2

    flood_fill(grid, start_x, start_y, current_color, visualize=visualize)
    current_color += 1

    while True:
        x, y = find_next_start(grid)
        if x == -1:
            break
        flood_fill(grid, x, y, current_color, visualize=visualize)
        current_color += 1

def print_grid(grid: List[List[int]]):
    for row in grid:
        print(" ".join(map(str, row)))
    print()


def read_grid_input() -> Tuple[List[List[int]], int, int]:
    print("Forneça a matriz (enter em branco encerra):")
    grid: List[List[int]] = []
    while True:
        try:
            line = input()
        except EOFError:
            break 
        if not line.strip():
            break
        grid.append(list(map(int, line.strip().split())))

    if not grid:
        raise ValueError("Nenhuma linha foi fornecida.")

    row_lengths = {len(row) for row in grid}
    if len(row_lengths) > 1:
        raise ValueError("Todas as linhas devem ter o mesmo número de colunas.")

    x = int(input("Digite a coordenada X inicial (linha): "))
    y = int(input("Digite a coordenada Y inicial (coluna): "))
    return grid, x, y

def main():
    grid, start_x, start_y = read_grid_input()

    print("\nGrid inicial:")
    print_grid(grid)

    plt.figure(figsize=(5, 5))
    plt.ion()

    fill_all_regions(grid, start_x, start_y, visualize=True)

    plt.ioff()
    plt.show()

    print("Grid preenchido:")
    print_grid(grid)

if __name__ == "__main__":
    main()
