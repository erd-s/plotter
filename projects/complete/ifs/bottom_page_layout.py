from utils.plotter_interface import PlotterInterface
from utils.utils import (
    effective_x_start,
    effective_x_end,
    effective_y_start,
    effective_y_end,
    center_x,
)
from projects.lines.line import draw_line


def draw_bottom_page_layout(
    plotter: PlotterInterface, draw_quarter_horizontal_line: bool
):
    # horizontal bottom line
    draw_line(
        plotter=plotter,
        origin_x_start=effective_x_start(),
        origin_x_end=effective_x_end(),
        origin_y_start=effective_y_end(),
        origin_y_end=effective_y_end(),
    )

    # horizontal mid line
    if draw_quarter_horizontal_line:
        draw_line(
            plotter=plotter,
            origin_x_start=effective_x_start(),
            origin_x_end=effective_x_end(),
            origin_y_start=effective_y_end() / 2,
            origin_y_end=effective_y_end() / 2,
        )

    # vertical mid line
    draw_line(
        plotter=plotter,
        origin_x_start=center_x(),
        origin_x_end=center_x(),
        origin_y_start=effective_y_start(),
        origin_y_end=effective_y_end(),
    )
