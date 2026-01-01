from utils.plotter_interface.PlotterInterface import PlotterInterface
from projects.lines.wave import wave_path
from projects.spiro.spiraled_path import draw_spiraled_shape


def draw_wave_spiral(
    plotter: PlotterInterface, center_x: float, center_y: float, width: float = 1
):
    path = wave_path(origin_x=center_x, origin_y=center_y, width=width)
    draw_spiraled_shape(
        plotter=plotter,
        shape_path=path,
        shape_center_x=path[0][0],
        shape_center_y=center_y,
        degree_interval=8,
    )
