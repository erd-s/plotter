from utils.plotter_interface import PlotterInterface
from projects.honeycomb_grid.honeycomb_grid import HoneycombGrid


def draw_honeycomb_grid(
    plotter: PlotterInterface,
    grid_size_horizontal: int,
    grid_size_vertical: int,
    origin_x: float,
    origin_y: float,
    width: float,
    height: float,
    pen_width_mm: float,
):
    width_adjustment = width * 0.1
    project = HoneycombGrid(
        grid_size_horizontal=grid_size_horizontal,
        grid_size_vertical=grid_size_vertical,
        origin_x=origin_x + (width_adjustment / 2),
        origin_y=origin_y,
        width=width - width_adjustment,
        height=height,
        pen_width_mm=pen_width_mm,
    )
    project.draw_object_grid(plotter=plotter)
