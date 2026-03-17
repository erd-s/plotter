from utils.plotter_interface import PlotterInterface
from projects.squiggle_fill.squiggle_path import (
    draw_squiggle_rectangle,
    draw_squiggle_rectangle_rounded,
)


def draw_squiggle_columns(
    plotter: PlotterInterface,
    center_x: float,
    effective_y_start: float,
    effective_height: float,
    effective_width: float,
    space_between_lines: float = 0.04,
):
    height = effective_height * 0.7
    width = (effective_width * 0.35) - space_between_lines
    origin_y = effective_y_start + ((effective_height - height) / 2)

    draw_squiggle_rectangle(
        plotter=plotter,
        origin_x=center_x - (width + (space_between_lines / 2)),
        origin_y=origin_y,
        height=height,
        width=width,
        space_between_lines=space_between_lines,
    )

    draw_squiggle_rectangle(
        plotter=plotter,
        origin_x=center_x + (space_between_lines / 2),
        origin_y=origin_y,
        height=height,
        width=width,
        space_between_lines=space_between_lines,
        reverse=True,
    )


def draw_squiggle_columns_rounded(
    plotter: PlotterInterface,
    center_x: float,
    effective_y_start: float,
    effective_height: float,
    effective_width: float,
    space_between_lines: float = 0.04,
):
    height = effective_height * 0.7
    width = (effective_width * 0.35) - space_between_lines
    origin_y = effective_y_start + ((effective_height - height) / 2)

    draw_squiggle_rectangle_rounded(
        plotter=plotter,
        origin_x=center_x - (width + (space_between_lines / 2)),
        origin_y=origin_y,
        height=height,
        width=width,
        space_between_lines=space_between_lines,
    )

    draw_squiggle_rectangle_rounded(
        plotter=plotter,
        origin_x=center_x + (space_between_lines / 2),
        origin_y=origin_y,
        height=height,
        width=width,
        space_between_lines=space_between_lines,
        reverse=True,
    )
