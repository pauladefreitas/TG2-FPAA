from typing import List, Tuple

def read_grid_input() -> Tuple[List[List[int]], int, int]:
    """Lê a matriz e as coordenadas iniciais do usuário."""
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