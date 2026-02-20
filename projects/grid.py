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
    sq_width = effective_width() / grid_size
    sq_height = effective_height() / grid_size

    # vertical
    for i in range(grid_size):
        current_y = effective_y_start() + (sq_height * i)
        plotter.moveto(effective_x_start(), current_y)
        plotter.lineto(effective_x_end(), current_y)
        if i == grid_size - 1:
            plotter.moveto(effective_x_start(), effective_y_end())
            plotter.lineto(effective_x_end(), effective_y_end())

    # horizontal
    for i in range(grid_size):
        current_x = effective_x_start() + (sq_width * i)
        plotter.moveto(current_x, effective_y_start())
        plotter.lineto(current_x, effective_y_end())
        if i == grid_size - 1:
            plotter.moveto(effective_x_end(), effective_y_start())
            plotter.lineto(effective_x_end(), effective_y_end())


def draw_grid_v2(
    plotter: PlotterInterface, grid_size_horizontal: int, grid_size_vertical: int
):
    sq_width = effective_width() / grid_size_horizontal
    sq_height = effective_height() / grid_size_vertical

    # vertical
    for i in range(grid_size_vertical):
        current_y = effective_y_start() + (sq_height * i)
        plotter.moveto(effective_x_start(), current_y)
        plotter.lineto(effective_x_end(), current_y)
        if i == grid_size_vertical - 1:
            plotter.moveto(effective_x_start(), effective_y_end())
            plotter.lineto(effective_x_end(), effective_y_end())

    # horizontal
    for i in range(grid_size_horizontal):
        current_x = effective_x_start() + (sq_width * i)
        plotter.moveto(current_x, effective_y_start())
        plotter.lineto(current_x, effective_y_end())
        if i == grid_size_horizontal - 1:
            plotter.moveto(effective_x_end(), effective_y_start())
            plotter.lineto(effective_x_end(), effective_y_end())


def draw_grid_v3(
    plotter: PlotterInterface,
    grid_size_horizontal: int,
    grid_size_vertical: int,
    origin_x: float,
    origin_y: float,
    height: float,
    width: float,
):
    sq_width = width / grid_size_horizontal
    sq_height = height / grid_size_vertical

    # vertical
    for i in range(grid_size_vertical):
        current_y = origin_y + (sq_height * i)
        plotter.moveto(origin_x, current_y)
        plotter.lineto(origin_x + width, current_y)
        if i == grid_size_vertical - 1:
            plotter.moveto(origin_x, origin_y + height)
            plotter.lineto(origin_x + width, origin_y + height)

    # horizontal
    for i in range(grid_size_horizontal):
        current_x = origin_x + (sq_width * i)
        plotter.moveto(current_x, origin_y)
        plotter.lineto(current_x, origin_y + height)
        if i == grid_size_horizontal - 1:
            plotter.moveto(origin_x + width, origin_y)
            plotter.lineto(origin_x + width, origin_y + height)


def square_width(grid_size_horizontal: int):
    return effective_width() / grid_size_horizontal


def square_height(grid_size_vertical: int):
    return effective_height() / grid_size_vertical
