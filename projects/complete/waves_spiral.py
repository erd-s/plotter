from utils.plotter_interface.PlotterInterface import PlotterInterface
from projects.lines.wave import wave_path
from projects.spiro.spiraled_path import create_spiraled_shape


def create_wave_spiral(
    plotter: PlotterInterface, x_origin: float, y_origin: float, width: float = 1
):
    path = wave_path(x_origin=x_origin, y_origin=y_origin, width=width)
    create_spiraled_shape(
        plotter=plotter,
        shape_path=path,
        shape_center_x=path[0][0],
        shape_center_y=y_origin,
        degree_interval=8,
    )
