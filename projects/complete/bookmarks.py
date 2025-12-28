from projects.rectangles.rectangle import create_rectangle
from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines_grid import CircleLinesGrid


def draw_bookmarks(
    plotter: PlotterInterface,
    effective_x_start: float,
    effective_y_start: float,
    effective_width: float,
    effective_height: float,
):
    padding = 0.4
    number_per_page = 4
    width = (effective_width - (padding * (number_per_page - 1))) / number_per_page

    for i in range(number_per_page):
        origin_x = effective_x_start + (width * i) + (padding * i)
        project = CircleLinesGrid(
            grid_size_horizontal=3,
            grid_size_vertical=10,
            origin_x=origin_x,
            origin_y=effective_y_start,
            width=width,
            height=effective_height,
            inset=0.1,
        )
        project.create_object_grid(plotter=plotter)
        create_rectangle(
            plotter=plotter,
            height=effective_height,
            width=width,
            center_x=origin_x + width / 2,
            center_y=effective_y_start + effective_height / 2,
        )
