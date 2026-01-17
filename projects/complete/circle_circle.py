from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import (
    lined_circle_top_right_paths,
    lined_circle_top_left_paths,
)
from projects.spiro.spiraled_path import draw_spiraled_shape_from_paths


def draw_circles_circle(plotter: PlotterInterface, center_x: float, center_y: float):
    radius = 0.25
    line_interval = 0.025
    degree_interval = 12

    right_half_paths = lined_circle_top_right_paths(
        center_x=center_x,
        center_y=center_y - (radius * 0.5) - 1.25,
        radius=radius,
        line_interval=line_interval,
    )
    left_half_paths = lined_circle_top_left_paths(
        center_x=center_x,
        center_y=center_y + (radius * 0.5) - 1.25,
        radius=radius,
        line_interval=line_interval,
    )

    draw_spiraled_shape_from_paths(
        plotter=plotter,
        shape_paths=right_half_paths,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=degree_interval,
    )

    draw_spiraled_shape_from_paths(
        plotter=plotter,
        shape_paths=left_half_paths,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=degree_interval,
    )


def draw_circles_circle_v2_right(
    plotter: PlotterInterface, center_x: float, center_y: float
):
    radius = 0.25
    line_interval = 0.025
    degree_interval = 12

    right_half_paths = lined_circle_top_right_paths(
        center_x=center_x,
        center_y=center_y - (radius * 0.5) - 1.35,
        radius=radius,
        line_interval=line_interval,
    )

    draw_spiraled_shape_from_paths(
        plotter=plotter,
        shape_paths=right_half_paths,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=degree_interval,
    )


def draw_circles_circle_v2_left(
    plotter: PlotterInterface, center_x: float, center_y: float
):
    radius = 0.25
    line_interval = 0.025
    degree_interval = 12

    left_half_paths = lined_circle_top_left_paths(
        center_x=center_x,
        center_y=center_y + (radius * 0.5) - 1.35,
        radius=radius,
        line_interval=line_interval,
    )

    draw_spiraled_shape_from_paths(
        plotter=plotter,
        shape_paths=left_half_paths,
        shape_center_x=center_x,
        shape_center_y=center_y,
        degree_interval=degree_interval,
    )
