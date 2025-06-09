from typing import List, Tuple

def flood_fill(grid: List[List[int]], x: int, y: int, color: int):
    if grid[x][y] != 0:
        return

    rows, cols = len(grid), len(grid[0])
    stack = [(x, y)]
    grid[x][y] = color

    while stack:
        i, j = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 0:
                grid[ni][nj] = color
                stack.append((ni, nj))

def find_next_start(grid: List[List[int]]) -> Tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return -1, -1

def fill_all_regions(grid: List[List[int]], start_x: int, start_y: int):
    current_color = 2
    flood_fill(grid, start_x, start_y, current_color)
    current_color += 1

    while True:
        x, y = find_next_start(grid)
        if x == -1:
            break
        flood_fill(grid, x, y, current_color)
        current_color += 1

def print_grid(grid: List[List[int]]):
    for row in grid:
        print(' '.join(map(str, row)))
    print()

def read_grid_input() -> Tuple[List[List[int]], int, int]:
    print("Forneça a matriz:")
    grid = []
    while True:
        line = input()
        if not line.strip():
            break
        grid.append(list(map(int, line.strip().split())))

    if not grid:
        raise ValueError("Nenhuma linha foi fornecida.")

    row_lengths = set(len(row) for row in grid)
    if len(row_lengths) > 1:
        raise ValueError("Todas as linhas devem ter o mesmo número de colunas.")

    x = int(input("Digite a coordenada X inicial (linha): "))
    y = int(input("Digite a coordenada Y inicial (coluna): "))
    return grid, x, y

if __name__ == "__main__":
    grid, start_x, start_y = read_grid_input()

    print("\nGrid inicial:")
    print_grid(grid)

    fill_all_regions(grid, start_x, start_y)

    print("Grid preenchido:")
    print_grid(grid)
