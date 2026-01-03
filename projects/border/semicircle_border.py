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
    radius = (width if width < height else height) / 30
    horizontal_radius = radius if width < height else radius * (width / height)
    vertical_radius = radius if height < width else radius * (width / height)
    horizontal_diameter = horizontal_radius * 2
    vertical_diameter = vertical_radius * 2

    semicircle_line_interval = radius / 8

    width_delta = (width / horizontal_diameter) - floor(width / horizontal_diameter)
    height_delta = (height / vertical_diameter) - floor(height / vertical_diameter)

    adjusted_width = width - width_delta
    adjusted_height = height - height_delta

    horizontal_iterations = int(adjusted_width / horizontal_diameter)
    vertical_iterations = int(adjusted_height / vertical_diameter)

    adjusted_origin_x = origin_x + (width_delta / 2)
    adjusted_origin_y = origin_y + (height_delta / 2)
    adjusted_end_x = adjusted_origin_x + adjusted_width
    adjusted_end_y = adjusted_origin_y + adjusted_height

    print(
        f"""
    width = {width}
    height = {height}
    width delta = {width_delta}
    height delta = {height_delta}

    expected adjusted width = {adjusted_width}
    expected adjusted height = {adjusted_height}
    actual_width = {horizontal_radius * horizontal_iterations * 2}
    actual_height = {vertical_radius * vertical_iterations * 2}

    adjusted origin x = {adjusted_origin_x}
    adjusted end x = {adjusted_end_x}
    adjusted origin y = {adjusted_origin_y}
    adjusted end y = {adjusted_end_y}

    horizontal_iterations = {horizontal_iterations}
    vertical_iterations = {vertical_iterations}
    horizontal radius = {horizontal_radius}
    horizontal diameter = {horizontal_diameter}
    vertical radius = {vertical_radius}
    vertical diameter = {vertical_diameter}

    """
    )

    # draw top
    for i in range(horizontal_iterations):
        x = adjusted_origin_x + (i * horizontal_diameter)
        y = adjusted_origin_y
        draw_lined_circle_top_half(
            plotter=plotter,
            center_x=x + horizontal_radius,
            center_y=y + horizontal_radius,
            radius=horizontal_radius,
            line_interval=semicircle_line_interval,
        )
        if i != horizontal_iterations - 1:
            draw_lined_circle_bottom_half(
                plotter=plotter,
                center_x=x + horizontal_diameter,
                center_y=y + horizontal_radius,
                radius=horizontal_radius,
                line_interval=semicircle_line_interval,
            )

    # draw right
    for i in range(vertical_iterations):
        x = adjusted_end_x
        y = adjusted_origin_y + (i * vertical_diameter)

        draw_lined_circle_bottom_half(
            plotter=plotter,
            center_x=x - vertical_radius,
            center_y=y + vertical_radius,
            radius=vertical_radius,
            line_interval=semicircle_line_interval,
            angle=-90,
        )
        if i != vertical_iterations - 1:
            draw_lined_circle_top_half(
                plotter=plotter,
                center_x=x - vertical_radius,
                center_y=y + vertical_diameter,
                radius=vertical_radius,
                line_interval=semicircle_line_interval,
                angle=-90,
            )

    # draw bottom
    for i in range(horizontal_iterations):
        x = adjusted_origin_x + (i * horizontal_diameter)
        y = adjusted_end_y
        draw_lined_circle_bottom_half(
            plotter=plotter,
            center_x=x + horizontal_radius,
            center_y=y - horizontal_radius,
            radius=horizontal_radius,
            line_interval=semicircle_line_interval,
        )

        if i != horizontal_iterations - 1:
            draw_lined_circle_top_half(
                plotter=plotter,
                center_x=x + horizontal_diameter,
                center_y=y - horizontal_radius,
                radius=horizontal_radius,
                line_interval=semicircle_line_interval,
            )

    # draw left
    for i in range(vertical_iterations):
        x = adjusted_origin_x
        y = adjusted_origin_y + (i * vertical_diameter)
        draw_lined_circle_top_half(
            plotter=plotter,
            center_x=x + vertical_radius,
            center_y=y + vertical_radius,
            radius=vertical_radius,
            line_interval=semicircle_line_interval,
            angle=-90,
        )
        if i != vertical_iterations - 1:
            draw_lined_circle_bottom_half(
                plotter=plotter,
                center_x=x + vertical_radius,
                center_y=y + vertical_diameter,
                radius=vertical_radius,
                line_interval=semicircle_line_interval,
                angle=-90,
            )
