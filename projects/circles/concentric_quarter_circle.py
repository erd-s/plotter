from utils.plotter_interface import PlotterInterface
import math


def __quarter_circle_path(
    center_x: float, center_y: float, radius: float, quadrant: int
):
    all_path_points = []
    path_points_to_return = []

    steps = int(radius * 100) if (int(radius * 100)) > 30 else 30

    # quadrant II
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = math.sqrt(abs((radius * radius) - (x * x)))
        point = [x + center_x, y + center_y]
        all_path_points.append(point)
        if quadrant == 2:
            path_points_to_return.append(point)

    # quadrant I
    x_list = []
    y_list = []
    for i in range(steps + 1):
        x = all_path_points[i][0]
        x_length = (radius / steps) * i
        y = center_y - math.sqrt(abs((radius * radius) - (x_length * x_length)))
        x_list.insert(0, x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        point = [x, y]
        all_path_points.append(point)
        if quadrant == 1:
            path_points_to_return.append(point)

    # quadrant IV
    for i in range(steps + 1):
        x = (radius / steps) * i
        y = center_y - math.sqrt(abs((radius * radius) - (x * x)))
        point = [center_x - x, y]
        all_path_points.append(point)
        if quadrant == 4:
            path_points_to_return.append(point)

    # quadrant III
    x_list = []
    y_list = []
    reversed_plot_points = list(reversed(all_path_points))
    for i in range(steps + 1):
        x = reversed_plot_points[i][0]
        y = all_path_points[i][1]
        x_list.append(x)
        y_list.insert(0, y)

    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        point = [x, y]
        all_path_points.append(point)
        if quadrant == 3:
            path_points_to_return.append(point)

    return path_points_to_return


def _draw_concentric_quarter_circle(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    number_of_lines: int,
    quadrant: int,
):
    radius_interval = radius / number_of_lines
    for i in range(number_of_lines):
        current_circle_radius = radius - (radius_interval * i)
        path = __quarter_circle_path(
            center_x=center_x,
            center_y=center_y,
            radius=current_circle_radius,
            quadrant=quadrant,
        )
        plotter.draw_path(path)


def draw_concentric_quarter_circle_bottom_left(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    number_of_lines: int,
):
    _draw_concentric_quarter_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        number_of_lines=number_of_lines,
        quadrant=1,
    )


def draw_concentric_quarter_circle_bottom_right(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    number_of_lines: int,
):
    _draw_concentric_quarter_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        number_of_lines=number_of_lines,
        quadrant=4,
    )


def draw_concentric_quarter_circle_top_left(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    number_of_lines: int,
):
    _draw_concentric_quarter_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        number_of_lines=number_of_lines,
        quadrant=2,
    )


def draw_concentric_quarter_circle_top_right(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    number_of_lines: int,
):
    _draw_concentric_quarter_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        number_of_lines=number_of_lines,
        quadrant=3,
    )
