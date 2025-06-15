from typing import List, Tuple
from src.visualization.grid_visualizer import show_grid

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