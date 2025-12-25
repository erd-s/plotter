from utils.plotter_interface import PlotterInterface
from projects.text.text import SidewaysText


def draw_page_title(
    plotter: PlotterInterface,
    title: str,
    effective_x_end: float,
    effective_y_start: float,
):
    text = SidewaysText(
        plotter=plotter,
        text=title,
        origin_x=effective_x_end - 0.2,
        origin_y=effective_y_start + 0.2,
    )
    text.draw_text()
