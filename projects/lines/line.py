from utils.plotter_interface import PlotterInterface


def draw_line(
    plotter: PlotterInterface,
    origin_x_start: float,
    origin_x_end: float,
    origin_y_start: float,
    origin_y_end: float,
):
    plotter.goto(origin_x_start, origin_y_start)
    plotter.lineto(origin_x_end, origin_y_end)
    plotter.penup()


def line_path(
    origin_x_start: float,
    origin_x_end: float,
    origin_y_start: float,
    origin_y_end: float,
):
    return [[origin_x_start, origin_y_start], [origin_x_end, origin_y_end]]
