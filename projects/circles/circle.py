import math
from matplotlib.patches import CirclePolygon
from utils.matplotlibutils import path_from_patch
from utils.plotter_interface import PlotterInterface


def draw_circle(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
):
    path_points = []
    steps = int(radius * 100) if (int(radius * 100)) > 30 else 30

    # quadrant I
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = math.sqrt(abs((radius * radius) - (x * x)))
        path_points.append([x + center_x, y + center_y])

    # quadrant II
    x_list = []
    y_list = []
    for i in range(steps + 1):
        x = path_points[i][0]
        x_length = (radius / steps) * i
        y = center_y - math.sqrt(abs((radius * radius) - (x_length * x_length)))
        x_list.insert(0, x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        path_points.append([x, y])

    # quadrant III
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = center_y - math.sqrt(abs((radius * radius) - (x * x)))
        path_points.append([center_x - x, y])

    # quadrant IV
    x_list = []
    y_list = []
    reversed_plot_points = list(reversed(path_points))
    for i in range(steps + 1):
        x = reversed_plot_points[i][0]
        y = path_points[i][1]
        x_list.append(x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        path_points.append([x, y])

    plotter.draw_path(path_points)


def draw_circle_v2(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
):
    path_points = circle_path(origin_x=center_x, origin_y=center_y, radius=radius)
    plotter.draw_path(path_points)


def circle_path(origin_x: float, origin_y: float, radius: float):
    circle = CirclePolygon(
        xy=(origin_x, origin_y), radius=radius, resolution=int(radius * 500)
    )
    path_points = path_from_patch(circle)
    return path_points
