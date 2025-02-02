from nextdraw import NextDraw

from utils.utils import (
    effective_x_start,
    effective_y_start,
    effective_y_end,
    effective_x_end,
)


def draw_margin(plotter: NextDraw, delta: float = 0):
    points = [
        [effective_x_start() + delta, effective_y_start() + delta],
        [effective_x_end() - delta, effective_y_start() + delta],
        [effective_x_end() - delta, effective_y_end() - delta],
        [effective_x_start() + delta, effective_y_end() - delta],
        [effective_x_start() + delta, effective_y_start() + delta],
    ]

    plotter.draw_path(points)
    plotter.moveto(0, 0)
    plotter.delay(300)
