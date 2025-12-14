from projects.lines.zigzags import create_zig_path
from utils.plotter_interface import PlotterInterface
from projects.spiro.spiraled_path import create_spiraled_shape


def create_iterative_zig_zag(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    height: float,
    width: float,
    degree_interval: int = 10,
):
    path = create_zig_path(
        center_x=center_x, center_y=center_y, height=height, width=width
    )
    create_spiraled_shape(
        plotter=plotter,
        shape_path=path,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=degree_interval,
    )
