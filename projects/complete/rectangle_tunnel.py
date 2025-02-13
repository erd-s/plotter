import random

from projects.rectangles.rectangle import create_rectangle
from utils.utils import *
from nextdraw import NextDraw


def create_tunnel(plotter: NextDraw):
    starting_height = 0.25
    starting_width = 0.25
    print(f"Creating tunnel with height: {starting_height}, width: {starting_width}")

    iterations = 35
    print(f"Iterations: {iterations}")

    center_rect_min_x = effective_x_start() + (effective_width() * 0.2)
    center_rect_min_y = effective_y_start() + (effective_height() * 0.6)
    center_rect_max_x = effective_x_start() + (effective_width() * 0.8)
    center_rect_max_y = effective_y_start() + (effective_height() * 0.8)
    center_rect_x = random.uniform(center_rect_min_x, center_rect_max_x)
    center_rect_y = random.uniform(center_rect_min_y, center_rect_max_y)

    print(f"Square Center: {center_rect_x, center_rect_y}")

    x_min = effective_x_start()
    x_max = effective_x_end()
    y_min = effective_y_start()
    y_max = effective_y_end()

    for i in range(iterations):
        height = starting_height + (i * i * 0.01)
        width = starting_width + (i * i * 0.01)

        print(f"Iteration: {i + 1} - Rectangle h: {height}, w: {width}")

        if height - starting_height < 0.04 or width - starting_width < 0.04:
            print(f"Iteration {i + 1} skip")
            continue

        try:
            create_rectangle(
                plotter=plotter,
                height=height,
                width=width,
                center_x=center_rect_x,
                center_y=center_rect_y,
                x_min=x_min,
                x_max=x_max,
                y_min=y_min,
                y_max=y_max,
            )
        except Exception as e:
            print(e)
