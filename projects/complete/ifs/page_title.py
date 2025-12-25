from utils.plotter_interface import PlotterInterface
from projects.text.text import (
    SidewaysText,
    VerticalText,
    HorizontalText,
    HorizontalSidewaysText,
)
from projects.border import draw_border_left, draw_border_right, draw_border_top


# Use the following config:

# DOC_HEIGHT = 8.3
# MARGIN_TOP = 0.3
# MARGIN_BOTTOM = 0.3
#
# DOC_WIDTH = 11.7
# MARGIN_LEFT = 0.3
# MARGIN_RIGHT = 0.3


def draw_page_title(
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
        origin_y=effective_y_start + shadow_depth,
    )
    text.draw_text()

    paths = text.text_paths()
    draw_border_top(plotter=plotter, paths=paths, shadow_depth=shadow_depth, angle=45)
