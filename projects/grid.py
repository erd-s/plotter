from utils.plotter_interface import PlotterInterface

from utils.utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_x_end,
    effective_y_start,
    effective_y_end,
)


def draw_grid(plotter: PlotterInterface, grid_size: int):
    square_width = effective_width() / grid_size
    square_height = effective_height() / grid_size

    # vertical
    for i in range(grid_size):
        current_y = effective_y_start() + (square_height * i)
        plotter.moveto(effective_x_start(), current_y)
        plotter.lineto(effective_x_end(), current_y)
        if i == grid_size - 1:
            plotter.moveto(effective_x_start(), effective_y_end())
            plotter.lineto(effective_x_end(), effective_y_end())

    # horizontal
    for i in range(grid_size):
        current_x = effective_x_start() + (square_width * i)
        plotter.moveto(current_x, effective_y_start())
        plotter.lineto(current_x, effective_y_end())
        if i == grid_size - 1:
            plotter.moveto(effective_x_end(), effective_y_start())
            plotter.lineto(effective_x_end(), effective_y_end())


def draw_grid_v2(
    plotter: PlotterInterface, grid_size_horizontal: int, grid_size_vertical: int
):
    square_width = effective_width() / grid_size_horizontal
    square_height = effective_height() / grid_size_vertical

    # vertical
    for i in range(grid_size_vertical):
        current_y = effective_y_start() + (square_height * i)
        plotter.moveto(effective_x_start(), current_y)
        plotter.lineto(effective_x_end(), current_y)
        if i == grid_size_vertical - 1:
            plotter.moveto(effective_x_start(), effective_y_end())
            plotter.lineto(effective_x_end(), effective_y_end())

    # horizontal
    for i in range(grid_size_horizontal):
        current_x = effective_x_start() + (square_width * i)
        plotter.moveto(current_x, effective_y_start())
        plotter.lineto(current_x, effective_y_end())
        if i == grid_size_horizontal - 1:
            plotter.moveto(effective_x_end(), effective_y_start())
            plotter.lineto(effective_x_end(), effective_y_end())
