import random

from projects.rectangles.rectangle import draw_rectangle_with_bounds
from utils.utils import (
    effective_height,
    effective_width,
    effective_x_end,
    effective_x_start,
    effective_y_end,
    effective_y_start,
)
from utils.plotter_interface import PlotterInterface


def draw_tunnel(plotter: PlotterInterface):
    starting_height = 0.175
    starting_width = 0.175
    print(f"Creating tunnel with height: {starting_height}, width: {starting_width}")

    iterations = 40
    print(f"Iterations: {iterations}")

    center_rect_min_x = effective_x_start() + (effective_width() * 0.7)
    center_rect_max_x = effective_x_start() + (effective_width() * 0.9)

    center_rect_min_y = effective_y_start() + (effective_height() * 0.6)
    center_rect_max_y = effective_y_start() + (effective_height() * 0.8)

    center_rect_x = random.uniform(center_rect_min_x, center_rect_max_x)
    center_rect_y = random.uniform(center_rect_min_y, center_rect_max_y)

    print(f"Square Center: {center_rect_x, center_rect_y}")

    x_min = effective_x_start()
    x_max = effective_x_end()
    y_min = effective_y_start()
    y_max = effective_y_end()

    height = starting_height
    width = starting_width

    while height <= effective_height() * 2 or width <= effective_width() * 2:
        draw_rectangle_with_bounds(
            plotter=plotter,
            height=height,
            width=width,
            center_x=effective_x_start() + effective_width() / 2,
            center_y=effective_y_start() + effective_height() / 2,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
        )
        multiplicative_growth = height * 0.05
        static_growth = (effective_height()) / 100

        height += (
            multiplicative_growth
            if multiplicative_growth > static_growth
            else static_growth
        )
        width += (
            multiplicative_growth
            if multiplicative_growth > static_growth
            else static_growth
        )
