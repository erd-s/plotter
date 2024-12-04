from nextdraw import NextDraw

from utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_x_end,
    effective_y_start,
    effective_y_end,
    center_x,
    center_y,
)

from .irregular_cube import create_cube
from .xy import create_xy


def create_irregular_cube_grid(plotter: NextDraw, grid_size: int):
    square_width = effective_width() / grid_size
    square_height = effective_height() / grid_size

    print(f'Square Width = {square_width}"')
    print(f'Square Height = {square_height}"')

    plotter.move(
        effective_x_start() + (square_width / 2),
        effective_y_start() + (square_height / 2),
    )

    for i in range(grid_size * grid_size):
        square_center_x = plotter.current_pos()[0]
        square_center_y = plotter.current_pos()[1]

        create_cube(
            plotter,
            origin_x=square_center_x,
            origin_y=square_center_y,
            width=square_width * 0.35,
            height=square_height * 0.35,
        )

        plotter.moveto(square_center_x, square_center_y)

        if (i + 1) % grid_size == 0:
            # move left and down
            plotter.move(square_width * -(grid_size - 1), square_height)
        else:
            # move right
            plotter.move(square_width, 0)
