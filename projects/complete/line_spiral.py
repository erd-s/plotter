from utils.plotter_interface.PlotterInterface import PlotterInterface
from projects.lines.wave import wave_path
from projects.spiro.spiraled_path import draw_spiraled_shape


def draw_line_spiral(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    length: float,
    distance_from_center: float,
):
    path = [
        (center_x, center_y + distance_from_center),
        (center_x, center_y + distance_from_center + length),
    ]
    draw_spiraled_shape(
        plotter=plotter,
        shape_path=path,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=3,
    )


def draw_line_spirals(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
):
    gap = 0.02
    distance_from_center_one = 0.25
    length_one = 0.5
    path = [
        (center_x + 0.1, center_y + distance_from_center_one),
        (center_x, center_y + distance_from_center_one + length_one),
    ]
    draw_spiraled_shape(
        plotter=plotter,
        shape_path=path,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=3,
    )

    distance_from_center_two = gap + distance_from_center_one + length_one
    length_two = 0.5
    path = [
        (center_x + 0.1, center_y + distance_from_center_two),
        (center_x, center_y + distance_from_center_two + length_two),
    ]
    draw_spiraled_shape(
        plotter=plotter,
        shape_path=path,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=3,
    )

    distance_from_center_three = gap + distance_from_center_two + length_two
    length_three = 0.5
    path = [
        (center_x + 0.1, center_y + distance_from_center_three),
        (center_x, center_y + distance_from_center_three + length_three),
    ]
    draw_spiraled_shape(
        plotter=plotter,
        shape_path=path,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=3,
    )
