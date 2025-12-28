from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import (
    create_lined_circle_right_half,
    create_lined_circle_top_half,
    create_lined_circle_left_half,
    create_lined_circle_bottom_half,
)


def create_lined_circle_v1(
    plotter: PlotterInterface, center_x: float, center_y: float, radius: float = 1
):
    line_interval = radius / 60

    create_lined_circle_left_half(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=90,
    )
    create_lined_circle_right_half(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval * 2,
        angle=90,
    )


def create_lined_circle_v2(
    plotter: PlotterInterface, center_x: float, center_y: float, radius: float = 1
):
    line_interval = radius / 50

    create_lined_circle_right_half(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval,
    )
    create_lined_circle_bottom_half(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=90,
    )
