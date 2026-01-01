from utils.plotter_interface import PlotterInterface
from projects.deco_circle_flair.deco_circle_flair_grid import DecoFlairObjectGrid


def draw_deco_flair_grid(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    width: float,
    height: float,
):
    grid_size_horizontal = 5
    grid_size_vertical = 6
    project = DecoFlairObjectGrid(
        grid_size_horizontal=grid_size_horizontal,
        grid_size_vertical=grid_size_vertical,
        origin_x=origin_x,
        origin_y=origin_y,
        width=width,
        height=height,
        inset=0,
    )
    project.draw_object_grid(plotter=plotter)
