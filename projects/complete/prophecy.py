from utils.plotter_interface import PlotterInterface
from projects.dnd.mark_of_azaliah_grid import MarkOfAzaliahGrid
from projects.text.text import HorizontalText
from utils.transform import centered_paths


def draw_mark_phases(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    width: float,
    height: float,
):
    project = MarkOfAzaliahGrid(
        grid_size_horizontal=5,
        grid_size_vertical=1,
        origin_x=origin_x,
        origin_y=origin_y,
        height=height,
        width=width,
    )
    project.draw_object_grid(plotter=plotter)
    title = "prophecy of lilith"
    text_height = 0.1
    text_width = len(title) * text_height + 1.5
    text = HorizontalText(
        plotter=plotter,
        text=title,
        origin_x=origin_x + (width / 2) - text_width / 2,
        origin_y=origin_y + (height * 0.075),
        height=text_height,
        width=text_width,
    )
    text.draw_text()
