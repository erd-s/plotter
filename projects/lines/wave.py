import numpy as np
from utils.matplotlibutils import joined_coordinate_list


def wave_path(origin_x: float, origin_y: float, width: float):
    x = np.arange(origin_x, origin_x + width, 0.005)
    y = np.sin(np.pi * x * (width + width))
    path = joined_coordinate_list(x_points=x.flat, y_points=y.flat)

    for point in path:
        point[1] += origin_y

    return path
