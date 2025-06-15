import matplotlib.colors as mcolors

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

def get_colormap():
    return mcolors.ListedColormap(COLORS) 