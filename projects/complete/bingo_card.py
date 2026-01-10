from utils.plotter_interface import PlotterInterface
from projects.grid import draw_grid_v2
from projects.text.text import HorizontalText as Text
from utils.transform import rotated_paths, centered_paths


def draw_bingo_card(
    plotter: PlotterInterface, center_x: float, center_y: float, title: str
):
    draw_grid_v2(plotter=plotter, grid_size_horizontal=5, grid_size_vertical=5)

    text = Text(plotter=plotter, text=title, origin_x=center_x + 4, origin_y=center_y)
    text_paths = text.text_paths()
    rotated_text_paths = rotated_paths(
        paths=text_paths, degrees=-90, rotation_x=center_x, rotation_y=center_y
    )
    centered_rotated_text_paths = centered_paths(
        paths=rotated_text_paths, around_x=center_x + 3.75, around_y=center_y
    )
    for path in centered_rotated_text_paths:
        plotter.draw_path(path)
