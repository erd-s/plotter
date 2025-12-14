from projects.rectangles.rectangle import rectangle_path
from projects.spiro.spiraled_path import create_spiraled_shape
from utils.plotter_interface import PlotterInterface


def create_square_spiral(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    height: float = 1.75,
    width: float = 1.75,
):
    rect_path = rectangle_path(
        height=height, width=width, center_x=center_x, center_y=center_y
    )
    create_spiraled_shape(
        plotter=plotter,
        shape_path=rect_path,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=5,
        number_to_skip=3,
    )


def square_spiral_trio(plotter: PlotterInterface, center_x: float, center_y: float):
    create_square_spiral(
        plotter=plotter, center_x=center_x, center_y=center_y, height=1.25, width=1.25
    )
    create_square_spiral(
        plotter=plotter, center_x=center_x, center_y=center_y, height=2, width=2
    )
    create_square_spiral(
        plotter=plotter, center_x=center_x, center_y=center_y, height=3.1, width=3.1
    )
