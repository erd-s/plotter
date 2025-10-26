import random
import numpy as np

from utils.plotter_interface import PlotterInterface
from utils.utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_y_start,
    effective_x_end,
    effective_y_end,
    center_x,
    center_y,
)

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))


def create_tesselation(plotter: PlotterInterface):
    # start with 3 points near center
    point_one = [
        center_x() - random.uniform(0.2, 0.4),
        center_y() - random.uniform(0.2, 0.4),
    ]
    point_two = [
        point_one[0] + random.uniform(0.4, 0.6),
        point_one[1] + random.uniform(0.4, 0.6),
    ]
    point_three = [
        point_two[0] - random.uniform(0.2, 0.4),
        point_two[1] + random.uniform(0.2, 0.4),
    ]

    print(point_one, point_two, point_three)

    line_one = [point_one, point_two]
    line_two = [point_two, point_three]
    line_three = [point_three, point_one]

    plotter.draw_path([point_one, point_two, point_three, point_one])
    sides = [line_one, line_two, line_three]

    for i in range(3):
        current_side = sides[i]
        print(f'current side = {current_side}')
        point_a = current_side[0]
        point_b = current_side[1]
        radians = np.arctan2(point_b[1] - point_a[1], point_b[0] - point_a[0])
        degrees = (radians * 180) / np.pi

        print(f'{degrees} degrees')
        x = np.average([point_a[0], point_b[0]])
        y = np.average([point_a[1], point_b[1]])
        new_line_one = [point_a, [x, y]]
        new_line_two = [[x, y], point_b]
        if 0 < degrees < 90:
            y -= 0.4
            new_line_one = [point_a, [x, y]]
            new_line_two = [[x, y], point_b]
        elif 90 < degrees < 180:
            y += 0.4
            new_line_one = [point_a, [x, y]]
            new_line_two = [[x, y], point_b]
        elif -90 > degrees > -180:
            x -= 0.4
            new_line_one = [point_a, [x, y]]
            new_line_two = [[x, y], point_b]
        elif 0 > degrees > -90:
            x += 0.4
            new_line_one = [point_a, [x, y]]
            new_line_two = [[x, y], point_b]


        sides.append(new_line_one)
        sides.append(new_line_two)
        path = [point_a, [x,y], point_b]
        print(f'path: {path}')
        plotter.draw_path(path)


