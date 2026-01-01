from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import (
    draw_lined_circle_right_half,
    draw_lined_circle_bottom_half,
)
from projects.rectangles.rectangle import draw_rectangle
from projects.text.text import HorizontalText
from utils.transform import centered_paths


def draw_2025(
    plotter: PlotterInterface, center_x: float, center_y: float, radius: float = 1.75
):
    draw_lined_circle_right_half(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        line_interval=0.1,
        angle=-90,
    )
    draw_lined_circle_bottom_half(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y,
        radius=radius,
        line_interval=0.05,
    )

    center_padding = 0.3
    height = (radius * 2) + center_padding
    width = height
    number_of_borders = 3
    distance = 0.15
    y_adjustment = -0.05
    text_center_y_adjustment = (
        center_y + height / 2 + (number_of_borders * distance) + y_adjustment
    )

    for i in range(number_of_borders):
        draw_rectangle(
            plotter=plotter,
            height=(height + distance * i),
            width=(width + distance * i),
            center_x=center_x,
            center_y=center_y + y_adjustment,
        )

    text = HorizontalText(
        plotter=plotter,
        text="2025",
        origin_x=center_x,
        origin_y=text_center_y_adjustment,
    )
    text_paths = text.text_paths()
    centered_text_paths = centered_paths(
        paths=text_paths, around_x=center_x, around_y=text_center_y_adjustment
    )
    for path in centered_text_paths:
        plotter.draw_path(path)
