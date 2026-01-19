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
    number_of_circles: int = 3,
    degree_interval: int = 3,
):
    gap = 0.02
    distance_from_center_one = 0.25
    length = 0.5

    for i in range(number_of_circles):
        total_distance_from_center = (
            (i + 1) * (length + gap)
        ) + distance_from_center_one
        path = [
            (center_x + 0.1, center_y + total_distance_from_center - length),
            (center_x, center_y + total_distance_from_center),
        ]
        draw_spiraled_shape(
            plotter=plotter,
            shape_path=path,
            shape_center_x=center_x,
            shape_center_y=center_y,
            degree_interval=degree_interval,
        )


def draw_spike_spiral(plotter: PlotterInterface, center_x: float, center_y: float):
    distance_from_center = 0.25
    length = 0.15
    x_offset = 0.1
    degree_interval = 12
    for i in range(15):
        path = [
            (center_x - (length / 2) + x_offset, center_y + distance_from_center),
            (center_x + (length / 2) + x_offset, center_y + distance_from_center),
        ]

        draw_spiraled_shape(
            plotter=plotter,
            shape_path=path,
            shape_center_x=center_x,
            shape_center_y=center_y,
            degree_interval=degree_interval,
        )
        distance_from_center += 0.02
        length += 0.09
        x_offset += 0.11


def draw_line_spiral_v2(plotter: PlotterInterface, center_x: float, center_y: float):
    distance_from_center = 0.2
    length = 0.15
    degree_interval = 12
    for i in range(75):
        path = [
            (center_x - (length / 2), center_y + distance_from_center),
            (center_x + (length / 2), center_y + distance_from_center),
        ]

        draw_spiraled_shape(
            plotter=plotter,
            shape_path=path,
            shape_center_x=center_x,
            shape_center_y=center_y,
            degree_interval=degree_interval,
        )
        distance_from_center += 0.025
        length += 0.0075
