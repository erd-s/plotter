import random

from nextdraw import NextDraw

from utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_y_start,
)

from .circle import create_circle
from .xy import create_xy


def create_circle_grid(plotter: NextDraw, grid_size: int):
    square_width = effective_width() / grid_size
    square_height = effective_height() / grid_size

    print(f'Square Width = {square_width}"')
    print(f'Square Height = {square_height}"')

    plotter.moveto(
        effective_x_start() + (square_width / 2),
        effective_y_start() + (square_height / 2),
    )

    for i in range(grid_size * grid_size):
        square_center_x = plotter.current_pos()[0]
        square_center_y = plotter.current_pos()[1]

        for _ in range(5):
            radius = square_height / 3
            rand_x_offset = random.uniform(radius * 0.25, radius * 0.5)
            if random.choice([True, False]):
                rand_x_offset *= -1

            rand_y_offset = random.uniform(radius * 0.25, radius * 0.5)
            if random.choice([True, False]):
                rand_y_offset *= -1

            create_circle(
                plotter=plotter,
                origin_x=square_center_x,
                origin_y=square_center_y,
                radius=radius,
                steps=30,
                offset_x=rand_x_offset,
                offset_y=rand_y_offset,
            )

        plotter.moveto(square_center_x, square_center_y)

        if (i + 1) % grid_size == 0:
            # move left and down
            plotter.move(square_width * -(grid_size - 1), square_height)
        else:
            # move right
            plotter.move(square_width, 0)
