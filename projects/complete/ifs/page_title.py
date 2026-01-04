from utils.plotter_interface import PlotterInterface
from projects.text.text import VerticalText, HorizontalSidewaysText, HorizontalText
from projects.border.border import draw_border_left, draw_border_top
from utils.transform import centered_paths

# Use the following config for page title right:

# DOC_HEIGHT = 8.27
# MARGIN_TOP = 0.3
# MARGIN_BOTTOM = 0.3
#
# DOC_WIDTH = 11.69
# MARGIN_LEFT = 0.3
# MARGIN_RIGHT = 0.3


def draw_page_title_right(
    plotter: PlotterInterface,
    title: str,
    effective_x_start: float,
    effective_y_start: float,
):
    shadow_depth = 0.075
    text = HorizontalSidewaysText(
        plotter=plotter,
        text=title,
        origin_x=effective_x_start + 0.3,
        origin_y=effective_y_start,
    )
    text.draw_text()

    paths = text.text_paths()
    draw_border_top(plotter=plotter, paths=paths, shadow_depth=shadow_depth, angle=45)


# Use the following config for page title left:


# DOC_HEIGHT = 11.69
# MARGIN_TOP = 0.3
# MARGIN_BOTTOM = 0.3
#
# DOC_WIDTH = 8.27
# MARGIN_LEFT = 0.3
# MARGIN_RIGHT = 0.3
def draw_page_title_left(
    plotter: PlotterInterface,
    title: str,
    effective_x_start: float,
    effective_y_start: float,
):
    shadow_depth = 0.075
    text = VerticalText(
        plotter=plotter,
        text=title,
        origin_x=effective_x_start + shadow_depth + 0.2,
        origin_y=effective_y_start + 0.3,
    )
    text.draw_text()

    paths = text.text_paths()
    draw_border_left(plotter=plotter, paths=paths, shadow_depth=shadow_depth, angle=45)


def draw_page_title_center(
    plotter: PlotterInterface, title: str, center_x: float, origin_y: float
):
    text = HorizontalText(plotter=plotter, text=title, origin_x=0, origin_y=origin_y)
    text_paths = text.text_paths()
    centered_text_paths = centered_paths(
        text_paths, around_x=center_x, around_y=origin_y
    )
    for path in centered_text_paths:
        plotter.draw_path(path)
