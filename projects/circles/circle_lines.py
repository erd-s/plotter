from utils.plotter_interface import PlotterInterface
from utils.transform import rotated_path
from math import sqrt, ceil
import random


def draw_lined_circle(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    number_of_lines = ceil((radius * 2) / line_interval)

    for i in range(number_of_lines):
        y = round(center_y - radius + (line_interval * i), 4)
        y_distance_to_center = round(radius - (line_interval * i), 4)
        x_distance_to_center = sqrt(
            abs(
                (y_distance_to_center * y_distance_to_center)
                - round((radius * radius), 4)
            )
        )
        start_x = center_x - x_distance_to_center
        end_x = center_x + x_distance_to_center
        if abs(end_x - start_x) < 0.01:
            continue
        point_a = [start_x, y]
        point_b = [end_x, y]
        top_path = rotated_path(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )

        plotter.draw_path(top_path)


def draw_lined_circle_top_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    paths = lined_circle_top_half_paths(
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    for path in paths:
        plotter.draw_path(path)


def lined_circle_top_half_paths(
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):

    number_of_lines_halved = round(radius / line_interval)
    paths = []

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
        top_path = rotated_path(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        paths.append(top_path)

    return paths


def draw_lined_circle_left_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    paths = lined_circle_top_left_paths(
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    for path in paths:
        plotter.draw_path(path)


def lined_circle_top_left_paths(
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    number_of_lines_halved = round(radius / line_interval)
    paths = []

    for i in range(number_of_lines_halved):
        y = center_y - line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        start_x = center_x - x_distance_to_center
        point_a = [start_x, y]
        point_b = [center_x, y]
        top_path = rotated_path(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        paths.append(top_path)

        point_c = [start_x, center_y + y_distance_to_center]
        point_d = [center_x, center_y + y_distance_to_center]
        bottom_path = rotated_path(
            [point_c, point_d],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        if bottom_path != top_path:
            paths.append(bottom_path)

    return paths


def draw_lined_circle_bottom_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    paths = lined_circle_top_bottom_paths(
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    for path in paths:
        plotter.draw_path(path)


def lined_circle_top_bottom_paths(
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    number_of_lines_halved = round(radius / line_interval)
    paths = []

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
        top_path = rotated_path(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        paths.append(top_path)

    return paths


def draw_lined_circle_right_half(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    paths = lined_circle_top_right_paths(
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    for path in paths:
        plotter.draw_path(path)


def lined_circle_top_right_paths(
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):
    number_of_lines_halved = round(radius / line_interval)
    paths = []

    for i in range(number_of_lines_halved):
        y = center_y - line_interval * i
        y_distance_to_center = line_interval * i
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        end_x = center_x + x_distance_to_center
        point_a = [center_x, y]
        point_b = [end_x, y]
        top_path = rotated_path(
            [point_a, point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        paths.append(top_path)

        point_c = [center_x, center_y + y_distance_to_center]
        point_d = [
            center_x + x_distance_to_center,
            center_y + y_distance_to_center,
        ]
        bottom_path = rotated_path(
            [point_c, point_d],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        if bottom_path != top_path:
            paths.append(bottom_path)

    return paths


def draw_dashed_line_circle(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float,
    line_interval: float,
    angle: float = 0,
):

    number_of_lines = round((radius * 2) / line_interval)
    max_iterations = 23
    base_line_length = (radius * 2) / max_iterations
    deviation = base_line_length / 2

    for i in range(number_of_lines):
        line_length = random.uniform(
            base_line_length - deviation, base_line_length + deviation
        )
        y = center_y - radius + (line_interval * i)
        y_distance_to_center = radius - (line_interval * i)
        x_distance_to_center = sqrt(
            abs((y_distance_to_center * y_distance_to_center) - (radius * radius))
        )
        start_x = center_x - x_distance_to_center
        end_x = center_x + x_distance_to_center
        if start_x == end_x:
            continue

        total_x_delta = end_x - start_x
        space_in_between_length = 0.05
        number_of_dashed_iterations = int(
            total_x_delta / (line_length + space_in_between_length)
        )
        total_remainder = total_x_delta - (
            (line_length * number_of_dashed_iterations)
            + (space_in_between_length * (number_of_dashed_iterations + 1))
        )
        remainder = total_remainder / 2
        remainder_offset = remainder + space_in_between_length

        first_line_path_point_a = [start_x, y]
        first_line_path_point_b = [start_x + remainder, y]
        first_line_path = rotated_path(
            [first_line_path_point_a, first_line_path_point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        plotter.draw_path(first_line_path)

        for d in range(number_of_dashed_iterations):
            adjusted_x_start = (
                start_x
                + remainder_offset
                + ((line_length + space_in_between_length) * d)
            )
            adjusted_x_end = adjusted_x_start + line_length
            point_a = [adjusted_x_start, y]
            point_b = [adjusted_x_end, y]
            path = rotated_path(
                [point_a, point_b],
                degrees=angle,
                rotation_x=center_x,
                rotation_y=center_y,
            )

            plotter.draw_path(path)

        last_line_path_point_a = [end_x - remainder, y]
        last_line_path_point_b = [end_x, y]
        last_line_path = rotated_path(
            [last_line_path_point_a, last_line_path_point_b],
            degrees=angle,
            rotation_x=center_x,
            rotation_y=center_y,
        )
        plotter.draw_path(last_line_path)
