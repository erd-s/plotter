from utils.plotter_interface.PlotterInterface import PlotterInterface
from projects.circles.concentric_quarter_circle import (
    draw_concentric_quarter_circle_bottom_left,
    draw_concentric_quarter_circle_bottom_right,
    draw_concentric_quarter_circle_top_left,
    draw_concentric_quarter_circle_top_right,
)


def draw_cqc_overlap(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    height: float,
    width: float,
    number_of_lines: int = 20,
):
    draw_concentric_quarter_circle_bottom_left(
        plotter=plotter,
        center_x=origin_x,
        center_y=origin_y + height,
        number_of_lines=number_of_lines,
        radius=width,
    )
    draw_concentric_quarter_circle_bottom_right(
        plotter=plotter,
        center_x=origin_x + width,
        center_y=origin_y + height,
        number_of_lines=number_of_lines,
        radius=width,
    )
    draw_concentric_quarter_circle_top_right(
        plotter=plotter,
        center_x=origin_x + width,
        center_y=origin_y,
        number_of_lines=number_of_lines,
        radius=width,
    )
    draw_concentric_quarter_circle_top_left(
        plotter=plotter,
        center_x=origin_x,
        center_y=origin_y,
        number_of_lines=number_of_lines,
        radius=width,
    )
