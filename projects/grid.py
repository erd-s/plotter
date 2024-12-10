from nextdraw import NextDraw

from utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_x_end,
    effective_y_start,
    effective_y_end,
)


def create_grid(plotter: NextDraw, grid_size: int):
    square_width = effective_width() / grid_size
    square_height = effective_height() / grid_size

    # horizontal
    for i in range(grid_size):
        current_y = effective_y_start() + (square_height * i)
        plotter.goto(effective_x_start(), current_y)
        plotter.pendown()
        plotter.lineto(effective_x_end(), current_y)
        plotter.penup()
        if i == grid_size - 1:
            plotter.goto(effective_x_start(), effective_y_end())
            plotter.pendown()
            plotter.lineto(effective_x_end(), effective_y_end())
            plotter.penup()

    # vertical
    for i in range(grid_size):
        current_x = effective_x_start() + (square_width * i)
        plotter.goto(current_x, effective_y_start())
        plotter.pendown()
        plotter.lineto(current_x, effective_y_end())
        plotter.penup()
        if i == grid_size - 1:
            plotter.goto(effective_x_end(), effective_y_start())
            plotter.pendown()
            plotter.lineto(effective_x_end(), effective_y_end())
            plotter.penup()
