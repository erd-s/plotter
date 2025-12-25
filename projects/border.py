from utils.plotter_interface import PlotterInterface
import itertools
from numpy import sin, pi


def draw_border_left(
    plotter: PlotterInterface,
    paths: [[(float, float)]],
    padding: float = 0.1,
    shadow_depth: float = 0,
    angle: int = 45,
):
    coordinates = list(itertools.chain.from_iterable(paths))
    x_coordinates = []
    y_coordinates = []
    for i, coordinate in enumerate(coordinates):
        if i == 0 or i % 2 == 0:
            x_coordinates.append(coordinate)
        else:
            y_coordinates.append(coordinate)

    min_x: float = min(x_coordinates) - padding
    max_x: float = max(x_coordinates) + padding
    min_y: float = min(y_coordinates) - padding
    max_y: float = max(y_coordinates) + padding

    border_path = [
        [min_x, min_y],
        [max_x, min_y],
        [max_x, max_y],
        [min_x, max_y],
        [min_x, min_y],
    ]

    plotter.draw_path(border_path)

    if shadow_depth != 0:
        alpha = angle
        theta = 90
        beta = 180 - angle - theta
        alpha_radians = alpha * (pi / 180)
        beta_radians = beta * (pi / 180)
        x_distance = shadow_depth / (sin(alpha_radians) / sin(beta_radians))
        a_x = min_x - x_distance
        a_y = min_y + shadow_depth
        b_x = a_x
        b_y = max_y + shadow_depth
        c_x = max_x - x_distance
        c_y = max_y + shadow_depth
        shadow_path_one = [[a_x, a_y], [b_x, b_y], [c_x, c_y]]
        shadow_path_two = [[min_x, min_y], [a_x, a_y]]
        shadow_path_three = [[min_x, max_y], [b_x, b_y]]
        shadow_path_four = [[max_x, max_y], [c_x, c_y]]
        plotter.draw_path(shadow_path_one)
        plotter.draw_path(shadow_path_two)
        plotter.draw_path(shadow_path_three)
        plotter.draw_path(shadow_path_four)


def draw_border_right(
    plotter: PlotterInterface,
    paths: [[(float, float)]],
    padding: float = 0.1,
    shadow_depth: float = 0,
    angle: int = 45,
):
    coordinates = list(itertools.chain.from_iterable(paths))
    x_coordinates = []
    y_coordinates = []
    for i, coordinate in enumerate(coordinates):
        if i == 0 or i % 2 == 0:
            x_coordinates.append(coordinate)
        else:
            y_coordinates.append(coordinate)

    min_x: float = min(x_coordinates) - padding
    max_x: float = max(x_coordinates) + padding
    min_y: float = min(y_coordinates) - padding
    max_y: float = max(y_coordinates) + padding

    border_path = [
        [min_x, min_y],
        [max_x, min_y],
        [max_x, max_y],
        [min_x, max_y],
        [min_x, min_y],
    ]

    plotter.draw_path(border_path)

    if shadow_depth != 0:
        alpha = angle
        theta = 90
        beta = 180 - angle - theta
        alpha_radians = alpha * (pi / 180)
        beta_radians = beta * (pi / 180)
        x_distance = shadow_depth / (sin(alpha_radians) / sin(beta_radians))
        a_x = max_x + x_distance
        a_y = min_y + shadow_depth
        b_x = a_x
        b_y = max_y + shadow_depth
        c_x = min_x + x_distance
        c_y = max_y + shadow_depth
        shadow_path_one = [[a_x, a_y], [b_x, b_y], [c_x, c_y]]
        shadow_path_two = [[max_x, min_y], [a_x, a_y]]
        shadow_path_three = [[max_x, max_y], [b_x, b_y]]
        shadow_path_four = [[min_x, max_y], [c_x, c_y]]
        plotter.draw_path(shadow_path_one)
        plotter.draw_path(shadow_path_two)
        plotter.draw_path(shadow_path_three)
        plotter.draw_path(shadow_path_four)


def draw_border_top(
    plotter: PlotterInterface,
    paths: [[(float, float)]],
    padding: float = 0.1,
    shadow_depth: float = 0,
    angle: int = 45,
):
    coordinates = list(itertools.chain.from_iterable(paths))
    x_coordinates = []
    y_coordinates = []
    for i, coordinate in enumerate(coordinates):
        if i == 0 or i % 2 == 0:
            x_coordinates.append(coordinate)
        else:
            y_coordinates.append(coordinate)

    min_x: float = min(x_coordinates) - padding
    max_x: float = max(x_coordinates) + padding
    min_y: float = min(y_coordinates) - padding
    max_y: float = max(y_coordinates) + padding

    border_path = [
        [min_x, min_y],
        [max_x, min_y],
        [max_x, max_y],
        [min_x, max_y],
        [min_x, min_y],
    ]

    plotter.draw_path(border_path)

    if shadow_depth != 0:
        alpha = angle
        theta = 90
        beta = 180 - angle - theta
        alpha_radians = alpha * (pi / 180)
        beta_radians = beta * (pi / 180)
        x_distance = shadow_depth / (sin(alpha_radians) / sin(beta_radians))
        a_x = min_x + x_distance
        a_y = min_y - shadow_depth
        b_x = max_x + x_distance
        b_y = min_y - shadow_depth
        c_x = max_x + x_distance
        c_y = max_y - shadow_depth
        shadow_path_one = [[a_x, a_y], [b_x, b_y], [c_x, c_y]]
        shadow_path_two = [[min_x, min_y], [a_x, a_y]]
        shadow_path_three = [[max_x, min_y], [b_x, b_y]]
        shadow_path_four = [[max_x, max_y], [c_x, c_y]]
        plotter.draw_path(shadow_path_one)
        plotter.draw_path(shadow_path_two)
        plotter.draw_path(shadow_path_three)
        plotter.draw_path(shadow_path_four)
