from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import (
    draw_lined_circle_bottom_half,
    draw_lined_circle_top_half,
)


def draw_semicircle_border(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    width: float,
    height: float,
):
    height_to_radius_ratio = 40
    radius = height / height_to_radius_ratio
    vertical_diameter = radius * 2
    number_of_iterations = int(height_to_radius_ratio / 2)
    semicircle_line_interval = radius / 8
    end_x = origin_x + width

    # draw right
    for i in range(number_of_iterations):
        x = end_x
        y = origin_y + (i * vertical_diameter)

        draw_lined_circle_bottom_half(
            plotter=plotter,
            center_x=x - radius,
            center_y=y + radius,
            radius=radius,
            line_interval=semicircle_line_interval,
            angle=-90,
        )
        if i != number_of_iterations - 1:
            draw_lined_circle_top_half(
                plotter=plotter,
                center_x=x - radius,
                center_y=y + vertical_diameter,
                radius=radius,
                line_interval=semicircle_line_interval,
                angle=-90,
            )

    # draw left
    for i in range(number_of_iterations):
        x = origin_x
        y = origin_y + (i * vertical_diameter)
        draw_lined_circle_top_half(
            plotter=plotter,
            center_x=x + radius,
            center_y=y + radius,
            radius=radius,
            line_interval=semicircle_line_interval,
            angle=-90,
        )
        if i != number_of_iterations - 1:
            draw_lined_circle_bottom_half(
                plotter=plotter,
                center_x=x + radius,
                center_y=y + vertical_diameter,
                radius=radius,
                line_interval=semicircle_line_interval,
                angle=-90,
            )
