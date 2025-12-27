from projects.circles.circle import circle_path, create_circle_v2
from utils.plotter_interface import PlotterInterface
from utils.transform import rotate
from math import isclose
from math import sqrt


def create_lined_circle(
    plotter: PlotterInterface,
    center_origin_x: float,
    center_origin_y: float,
    radius: float,
    line_interval: float,
    angle: int = 0,
):
    create_circle_v2(
        plotter=plotter,
        origin_x=center_origin_x,
        origin_y=center_origin_y,
        radius=radius,
    )
    number_of_lines_halved = round(radius / line_interval)

    for i in range(number_of_lines_halved):
        y = center_origin_y - line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        start_x = center_origin_x - x_distance_to_center
        end_x = center_origin_x + x_distance_to_center
        point_a = [start_x, y]
        point_b = [end_x, y]
        plotter.draw_path([point_a, point_b])
        point_c = [start_x, center_origin_y + y_distance_to_center]
        point_d = [end_x, center_origin_y + y_distance_to_center]
        plotter.draw_path([point_c, point_d])
