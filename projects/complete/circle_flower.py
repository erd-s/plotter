from utils.plotter_interface import PlotterInterface
from projects.circles.circle import circle_path
from projects.spiro.spiraled_path import draw_spiraled_shape


def draw_circle_flower(plotter: PlotterInterface, center_x: float, center_y: float):
    for i in range(8):
        path = circle_path(
            center_x=center_x, center_y=center_y - (2 - ((2 / 9) * i)), radius=0.2
        )
        draw_spiraled_shape(
            plotter=plotter,
            shape_path=path,
            shape_center_x=center_x,
            shape_center_y=center_y,
            degree_interval=10,
        )
