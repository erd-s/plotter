from utils.plotter_interface import PlotterInterface
import math


def draw_semicircle(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    radius: float,
):
    path_points = semicircle_path(origin_x, origin_y, radius)
    plotter.draw_path(path_points)


def semicircle_path(
    origin_x: float,
    origin_y: float,
    radius: float,
):
    path_points = []
    steps = int(radius * 100) if (int(radius * 100)) > 30 else 30

    # quadrant I
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = math.sqrt(abs((radius * radius) - (x * x)))
        path_points.append([x + origin_x, y + origin_y])

    # quadrant II
    x_list = []
    y_list = []
    for i in range(steps + 1):
        x = path_points[i][0]
        x_length = (radius / steps) * i
        y = origin_y - math.sqrt(abs((radius * radius) - (x_length * x_length)))
        x_list.insert(0, x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        path_points.append([x, y])

    return path_points
