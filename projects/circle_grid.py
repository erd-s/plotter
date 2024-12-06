import random

from nextdraw import NextDraw
import math

from utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_y_start,
)

from .circle import create_circle
from .xy import create_xy


def create_circle_grid(plotter: NextDraw, grid_size: int, start_index=0):
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

        if i >= start_index:
            num_circles = 5
            for c in range(num_circles):
                radius = square_width / (num_circles + 1)
                x_offset = (square_width/-2) + ((c+1)*radius)
                y_offset = 0

                create_circle(
                    plotter=plotter,
                    origin_x=square_center_x + x_offset,
                    origin_y=square_center_y + y_offset,
                    radius=radius,
                    steps=30
                )

        plotter.moveto(square_center_x, square_center_y)

        if (i + 1) % grid_size == 0:
            # move left and down
            plotter.move(square_width * -(grid_size - 1), square_height)
        else:
            # move right
            plotter.move(square_width, 0)
