import numpy as np
from utils.matplotlibutils import joined_coordinate_list

def wave_path(x_origin: float, y_origin: float, height: float, width: float):
    x = np.arange(x_origin, x_origin + width, 0.005)
    y = np.cos(np.pi * x * 4)
    path = joined_coordinate_list(x_points=x.flat, y_points=y.flat)

    for point in path:
        point[1] += y_origin

    return path

