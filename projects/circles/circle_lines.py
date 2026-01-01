from utils.plotter_interface import PlotterInterface
from utils.transform import rotate
from math import sqrt


def draw_lined_circle(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: int = 0,
):

    number_of_lines_halved = round(radius / line_interval)

    for i in range(number_of_lines_halved):
        y = center_y - line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        start_x = center_x - x_distance_to_center
        end_x = center_x + x_distance_to_center
        point_a = [start_x, y]
        point_b = [end_x, y]
        top_path = rotate(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )

        plotter.draw_path(top_path)
        point_c = [start_x, center_y + y_distance_to_center]
        point_d = [end_x, center_y + y_distance_to_center]
        bottom_path = rotate(
            [point_c, point_d],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        if bottom_path != top_path:
            plotter.draw_path(bottom_path)


def draw_lined_circle_top_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: int = 0,
):

    number_of_lines_halved = round(radius / line_interval)

    for i in range(number_of_lines_halved):
        y = center_y - line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        start_x = center_x - x_distance_to_center
        end_x = center_x + x_distance_to_center
        point_a = [start_x, y]
        point_b = [end_x, y]
        top_path = rotate(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        plotter.draw_path(top_path)


def draw_lined_circle_left_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: int = 0,
):

    number_of_lines_halved = round(radius / line_interval)

    for i in range(number_of_lines_halved):
        y = center_y - line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        start_x = center_x - x_distance_to_center
        point_a = [start_x, y]
        point_b = [center_x, y]
        top_path = rotate(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        plotter.draw_path(top_path)

        point_c = [start_x, center_y + y_distance_to_center]
        point_d = [center_x, center_y + y_distance_to_center]
        bottom_path = rotate(
            [point_c, point_d],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        if bottom_path != top_path:
            plotter.draw_path(bottom_path)


def draw_lined_circle_bottom_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: int = 0,
):

    number_of_lines_halved = round(radius / line_interval)

    for i in range(number_of_lines_halved):
        y = center_y + line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        start_x = center_x - x_distance_to_center
        end_x = center_x + x_distance_to_center
        point_a = [start_x, y]
        point_b = [end_x, y]
        top_path = rotate(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        plotter.draw_path(top_path)


def draw_lined_circle_right_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: int = 0,
):

    number_of_lines_halved = round(radius / line_interval)

    for i in range(number_of_lines_halved):
        y = center_y - line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        center_x - x_distance_to_center
        end_x = center_x + x_distance_to_center
        point_a = [center_x, y]
        point_b = [end_x, y]
        top_path = rotate(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        plotter.draw_path(top_path)

        point_c = [center_x, center_y + y_distance_to_center]
        point_d = [
            center_x + x_distance_to_center,
            center_y + y_distance_to_center,
        ]
        bottom_path = rotate(
            [point_c, point_d],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        if bottom_path != top_path:
            plotter.draw_path(bottom_path)
