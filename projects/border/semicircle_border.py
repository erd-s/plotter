from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import (
    draw_lined_circle_left_half,
    draw_lined_circle_right_half,
    draw_lined_circle_bottom_half,
    draw_lined_circle_top_half,
)
from math import floor


def draw_semicircle_border(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    width: float,
    height: float,
):
    radius = width / 30
    diameter = radius * 2
    horizontal_iterations = int(width / diameter)
    vertical_iterations = int(height / diameter)
    origin_x_adjustment = ((width / radius) - floor(width / radius)) / 2
    origin_y_adjustment = ((height / radius) - floor(height / radius)) / 2
    adjusted_origin_x = origin_x + origin_x_adjustment
    adjusted_origin_y = origin_y + origin_y_adjustment
    semicircle_line_interval = radius / 8
    adjusted_width = width - origin_x_adjustment * 2
    adjusted_height = height - origin_y_adjustment * 2
    print(
        f"""
    x adjustment = {origin_x_adjustment}
    y adjustment = {origin_y_adjustment}
    adjusted origin x = {adjusted_origin_x}
    adjusted origin y = {adjusted_origin_y}
    adjusted width = {adjusted_width}
    adjusted height = {adjusted_height}
    radius = {radius}
    """
    )

    # draw top
    for i in range(horizontal_iterations):
        x = adjusted_origin_x + (i * diameter) + radius
        y = adjusted_origin_y + (radius / 2)
        draw_lined_circle_top_half(
            plotter=plotter,
            center_x=x,
            center_y=y,
            radius=radius,
            line_interval=semicircle_line_interval,
        )
        if i != horizontal_iterations - 1:
            draw_lined_circle_bottom_half(
                plotter=plotter,
                center_x=x + radius,
                center_y=y,
                radius=radius,
                line_interval=semicircle_line_interval,
            )

    # draw bottom
    for i in range(horizontal_iterations):
        x = adjusted_origin_x + (i * diameter) + radius
        y = (
            origin_y + adjusted_height + radius
            if width < height
            else adjusted_origin_y + adjusted_height + (radius / 2)
        )
        draw_lined_circle_bottom_half(
            plotter=plotter,
            center_x=x,
            center_y=y,
            radius=radius,
            line_interval=semicircle_line_interval,
        )

        if i != horizontal_iterations - 1:
            draw_lined_circle_top_half(
                plotter=plotter,
                center_x=x + radius,
                center_y=y,
                radius=radius,
                line_interval=semicircle_line_interval,
            )

    # draw left
    for i in range(vertical_iterations):
        x = adjusted_origin_x + radius
        y = adjusted_origin_y + (i * diameter) + (radius / 2)
        draw_lined_circle_top_half(
            plotter=plotter,
            center_x=x,
            center_y=y,
            radius=radius,
            line_interval=semicircle_line_interval,
            angle=-90,
        )
        if i != vertical_iterations - 1:
            draw_lined_circle_bottom_half(
                plotter=plotter,
                center_x=x,
                center_y=y + radius,
                radius=radius,
                line_interval=semicircle_line_interval,
                angle=-90,
            )

    # draw right
    for i in range(vertical_iterations):
        x = (
            adjusted_origin_x + adjusted_width - radius
            if width < height
            else origin_x + adjusted_width - radius
        )
        y = adjusted_origin_y + (i * diameter) + (radius / 2)

        draw_lined_circle_bottom_half(
            plotter=plotter,
            center_x=x,
            center_y=y,
            radius=radius,
            line_interval=semicircle_line_interval,
            angle=-90,
        )
        if i != vertical_iterations - 1:
            draw_lined_circle_top_half(
                plotter=plotter,
                center_x=x,
                center_y=y + radius,
                radius=radius,
                line_interval=semicircle_line_interval,
                angle=-90,
            )
