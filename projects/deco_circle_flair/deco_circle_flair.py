from utils.plotter_interface import PlotterInterface
from projects.circles.circle import draw_circle_v2
from projects.lines.line import line_path
from utils.transform import rotate


def draw_deco_circle_flair(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    width: float,
    height: float,
    up: bool,
):
    radius_multiplier = 10
    radius = width / radius_multiplier if width < height else height / radius_multiplier
    y_offset = radius * 3 if up else -radius * 3
    draw_circle_v2(
        plotter=plotter, center_x=center_x, center_y=center_y + y_offset, radius=radius
    )
    number_of_lines = 10

    for i in range(number_of_lines):
        degree_rotation = (90 / (number_of_lines - 1)) * i
        circle_padding = 0.06
        distance_to_center = radius + circle_padding
        line_length_max = (
            (width / 2 if width < height else height / 2)
            - circle_padding
            + (radius * 3)
        )
        line_length = i * (line_length_max / number_of_lines)

        # left line
        origin_x_start = center_x - line_length - distance_to_center
        origin_x_end = center_x - distance_to_center
        path = line_path(
            origin_x_start=origin_x_start,
            origin_x_end=origin_x_end,
            origin_y_end=center_y + y_offset,
            origin_y_start=center_y + y_offset,
        )
        rotated_path = rotate(
            path=path,
            degrees=degree_rotation if up else -degree_rotation,
            rotation_x=center_x,
            rotation_y=center_y + y_offset,
        )
        plotter.draw_path(rotated_path)

        # right line
        if number_of_lines != i + 1:
            origin_x_start_right_line = center_x + line_length + distance_to_center
            origin_x_end_right_line = center_x + distance_to_center
            path = line_path(
                origin_x_start=origin_x_start_right_line,
                origin_x_end=origin_x_end_right_line,
                origin_y_end=center_y + y_offset,
                origin_y_start=center_y + y_offset,
            )
            rotated_path_right_line = rotate(
                path=path,
                degrees=-degree_rotation if up else degree_rotation,
                rotation_x=center_x,
                rotation_y=center_y + y_offset,
            )
            plotter.draw_path(rotated_path_right_line)
