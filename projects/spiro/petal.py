from utils.plotter_interface import PlotterInterface
from utils.utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_y_start,
    effective_x_end,
    effective_y_end,
)


def create_spiro_petal(plotter: PlotterInterface, steps: int):
    x_increment = effective_width() / steps
    y_increment = effective_height() / steps

    # A
    for i in range(steps):
        start_x = effective_x_start()
        start_y = (i * y_increment) + effective_y_start()
        end_x = effective_x_start() + ((i + 1) * x_increment)
        end_y = effective_y_end()
        plotter.moveto(start_x, start_y)
        plotter.lineto(end_x, end_y)
        plotter.penup()

    # B
    for i in range(steps):
        start_x = (i * x_increment) + effective_x_start()
        start_y = effective_y_end()
        end_x = effective_x_end()
        end_y = effective_y_start() + effective_height() - (y_increment * (i + 1))
        plotter.moveto(start_x, start_y)
        plotter.lineto(end_x, end_y)
        plotter.penup()

    # C
    for i in range(steps):
        start_x = effective_x_end()
        start_y = effective_y_end() - (i * y_increment)
        end_x = effective_x_end() - (x_increment * (i + 1))
        end_y = effective_y_start()
        plotter.moveto(start_x, start_y)
        plotter.lineto(end_x, end_y)
        plotter.penup()

    # D
    for i in range(steps):
        start_x = effective_x_end() - (x_increment * i)
        start_y = effective_y_start()
        end_x = effective_x_start()
        end_y = effective_y_start() + (y_increment * (i + 1))
        plotter.moveto(start_x, start_y)
        plotter.lineto(end_x, end_y)
        plotter.penup()
