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
    x_offset = effective_width() / 2.75
    y_offset = effective_height() / 4
    project = ConcentricCircles(
        plotter=plotter,
        center_x=center_x() - x_offset,
        center_y=center_y() - y_offset,
        effective_height=effective_height() / 2,
        effective_width=effective_width() / 2,
        effective_start_x=effective_x_start(),
        effective_end_x=effective_x_start() + effective_width() / 2,
        effective_start_y=effective_y_start(),
        effective_end_y=effective_y_start() + effective_height() / 2,
        direction=Direction.BOTTOM_RIGHT,
    )
    project.create_concentric_circles()
    project = ConcentricCircles(
        plotter=plotter,
        center_x=center_x() + x_offset,
        center_y=center_y() - y_offset,
        effective_height=effective_height() / 2,
        effective_width=effective_width() / 2,
        effective_start_x=center_x(),
        effective_end_x=effective_x_end(),
        effective_start_y=effective_y_start(),
        effective_end_y=effective_y_start() + effective_height() / 2,
        direction=Direction.BOTTOM_LEFT,
    )
    project.create_concentric_circles()
    project = ConcentricCircles(
        plotter=plotter,
        center_x=center_x() - x_offset,
        center_y=center_y() + y_offset,
        effective_height=effective_height() / 2,
        effective_width=effective_width() / 2,
        effective_start_x=effective_x_start(),
        effective_end_x=center_x(),
        effective_start_y=center_y(),
        effective_end_y=effective_y_end(),
        direction=Direction.TOP_RIGHT,
    )
    project.create_concentric_circles()
    project = ConcentricCircles(
        plotter=plotter,
        center_x=center_x() + x_offset,
        center_y=center_y() + y_offset,
        effective_height=effective_height() / 2,
        effective_width=effective_width() / 2,
        effective_start_x=center_x(),
        effective_end_x=effective_x_end(),
        effective_start_y=center_y(),
        effective_end_y=effective_y_end(),
        direction=Direction.TOP_LEFT,
    )
    project.create_concentric_circles()
    radius = 0.05
    while radius < 0.5:
        create_circle(
            plotter=plotter, origin_x=center_x(), origin_y=center_y(), radius=radius
        )
        radius += 0.05
