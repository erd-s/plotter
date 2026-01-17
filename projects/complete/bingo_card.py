from utils.plotter_interface import PlotterInterface
from projects.grid import draw_grid_v2, square_width, square_height
from projects.text.text import HorizontalText as Text
from utils.transform import rotated_paths, centered_paths
from projects.rectangles.rectangle import draw_rectangle


# Use the following settings for A4:
# DOC_HEIGHT = 8.27
# MARGIN_TOP = 0.385
# MARGIN_BOTTOM = 0.385
#
# DOC_WIDTH = 11.69
# MARGIN_LEFT = 1.595
# MARGIN_RIGHT = 2.595


def draw_bingo_card(
    plotter: PlotterInterface, center_x: float, center_y: float, title: str
):
    # grid
    draw_grid_v2(plotter=plotter, grid_size_horizontal=5, grid_size_vertical=5)

    # title
    text = Text(
        plotter=plotter, text=title, origin_x=center_x, origin_y=center_y, width=2
    )
    text_paths = text.text_paths()
    rotated_text_paths = rotated_paths(
        paths=text_paths, degrees=-90, rotation_x=center_x, rotation_y=center_y
    )
    centered_rotated_text_paths = centered_paths(
        paths=rotated_text_paths, around_x=center_x + 4.5, around_y=center_y
    )
    for path in centered_rotated_text_paths:
        plotter.draw_path(path)

    # free space
    free_space_width = square_width(5)
    free_space_height = square_height(5)
    number_of_iterations = 10
    for i in range(number_of_iterations):
        if i > 0:
            width = free_space_width - ((free_space_width / number_of_iterations) * i)
            height = free_space_height - (
                (free_space_height / number_of_iterations) * i
            )
            draw_rectangle(
                plotter=plotter,
                height=height,
                width=width,
                center_x=center_x,
                center_y=center_y,
            )
