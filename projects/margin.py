from nextdraw import NextDraw

from utils import effective_x_start, effective_y_start, effective_y_end, effective_x_end


def draw_margin(plotter: NextDraw):
    points = [
        [effective_x_start(), effective_y_start()],
        [effective_x_end(), effective_y_start()],
        [effective_x_end(), effective_y_end()],
        [effective_x_start(), effective_y_end()],
        [effective_x_start(), effective_y_start()],
    ]

    plotter.draw_path(points)
