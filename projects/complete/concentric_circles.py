from utils.utils import (
    center_x,
    center_y,
    effective_height,
    effective_width,
    effective_x_start,
    effective_x_end,
    effective_y_start,
    effective_y_end,
)
from projects.circles.concentric_circles import ConcentricCircles, Direction
from projects.circles.circle import create_circle


def create_concentric_circles(plotter):
    orientation = "portrait" if effective_height() > effective_width() else "landscape"

    x_offset = (
        effective_width() if orientation == "portrait" else effective_height()
    ) / 2.75
    y_offset = (
        effective_height() if orientation == "portrait" else effective_width()
    ) / 4
    radius = (
        effective_height() if orientation == "portrait" else effective_width()
    ) / 150

    middle_radius = radius
    while middle_radius < effective_height():
        create_circle(
            plotter=plotter,
            origin_x=center_x(),
            origin_y=center_y(),
            radius=middle_radius,
        )
        middle_radius += (
            effective_height() if orientation == "portrait" else effective_width()
        ) / 120
