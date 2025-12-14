from projects.complete.iterative_semicircles import create_iterative_semicircles
from projects.complete.waves_spiral import create_wave_spiral
from utils.plotter_interface import PlotterInterface
from projects.complete.square_spiral import (
    create_square_spiral_v2,
)
from projects.complete.line_spiral import create_line_spirals
from projects.complete.iterative_zig_zag import create_iterative_zig_zag


def joker(plotter: PlotterInterface, center_x: float, center_y: float):
    create_wave_spiral(
        plotter=plotter, center_x=center_x, center_y=center_y, width=0.875
    )


def teenager(plotter: PlotterInterface, center_x: float, center_y: float):
    create_square_spiral_v2(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        height=1.5,
        width=1.8,
        degree_interval=12,
        number_to_skip=1,
    )


def rebel(plotter: PlotterInterface, center_x: float, center_y: float):
    create_iterative_zig_zag(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        height=1.75,
        width=1.75,
        degree_interval=10,
    )


def strategist(plotter: PlotterInterface, center_x: float, center_y: float):
    create_square_spiral_v2(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        height=1.4,
        width=1.75,
        number_to_skip=4,
    )


def professor(plotter: PlotterInterface, center_x: float, center_y: float):
    create_iterative_semicircles(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        radius=0.6,
        degree_interval=6,
    )


def big_self(plotter: PlotterInterface, center_x: float, center_y: float):
    create_line_spirals(plotter=plotter, center_x=center_x, center_y=center_y)
