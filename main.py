import matplotlib.pyplot as plt
from src.utils.input_handler import read_grid_input
from src.utils.grid_operations import fill_all_regions
from src.visualization.grid_visualizer import print_grid

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
