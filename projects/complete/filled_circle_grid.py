from projects.filled_shape_grid.filled_circle_grid import (
    FilledCircleObjectGrid,
    FilledCircleObjectGridV2,
)
from utils.plotter_interface import PlotterInterface
from projects.grid import draw_grid_v3


def draw_filled_circle_grid(
    plotter: PlotterInterface,
    grid_size: int,
    center_x: float,
    center_y: float,
    width: float,
    pen_width_mm: float,
):
    origin_x = center_x - width / 2
    origin_y = center_y - width / 2

    draw_grid_v3(
        plotter=plotter,
        grid_size_horizontal=grid_size,
        grid_size_vertical=grid_size,
        origin_x=origin_x,
        origin_y=origin_y,
        height=width,
        width=width,
    )

    project = FilledCircleObjectGrid(
        grid_size_horizontal=grid_size,
        grid_size_vertical=grid_size,
        origin_x=origin_x,
        origin_y=origin_y,
        width=width,
        height=width,
        pen_width_mm=pen_width_mm,
    )
    project.draw_object_grid(plotter=plotter)


def draw_filled_circle_grid_v2(
    plotter: PlotterInterface,
    grid_size_horizontal: int,
    grid_size_vertical: int,
    center_x: float,
    center_y: float,
    width: float,
    height: float,
    pen_width_mm: float,
):
    origin_x = center_x - width / 2
    origin_y = center_y - height / 2

    project = FilledCircleObjectGridV2(
        grid_size_horizontal=grid_size_horizontal,
        grid_size_vertical=grid_size_vertical,
        origin_x=origin_x,
        origin_y=origin_y,
        width=width,
        height=height,
        pen_width_mm=pen_width_mm,
    )
    project.draw_object_grid(plotter=plotter)
