import random
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
from projects.circles.circle import create_circle_v2


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
        radius=radius,
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
        radius=radius,
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
        radius=radius,
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
        radius=radius,
        direction=Direction.TOP_LEFT,
    )
    project.create_concentric_circles()

    middle_radius = radius
    while middle_radius < (
        (effective_height() if orientation == "portrait" else effective_width()) / 12
    ):
        create_circle_v2(
            plotter=plotter,
            origin_x=center_x(),
            origin_y=center_y(),
            radius=middle_radius,
        )
        middle_radius += (
            effective_height() if orientation == "portrait" else effective_width()
        ) / 120


def create_concentric_circles_v2(plotter, centered=False):
    orientation = "portrait" if effective_height() > effective_width() else "landscape"

    starting_radius = (
        effective_height() if orientation == "portrait" else effective_width()
    ) / 200

    current_radius = starting_radius
    origin_x = (
        random.uniform(
            effective_x_start() + effective_width() / 4,
            effective_x_end() - effective_width() / 4,
        )
        if not centered
        else center_x()
    )
    origin_y = (
        random.uniform(
            effective_y_start() + effective_height() / 4,
            effective_y_end() - effective_height() / 4,
        )
        if not centered
        else center_y()
    )

    print(f"Concentric circle center origin: {origin_x}, {origin_y}")
    while (
        current_radius < effective_height()
        if orientation == "portrait"
        else effective_width()
    ):
        create_circle_v2(
            plotter=plotter,
            origin_x=origin_x,
            origin_y=origin_y,
            radius=current_radius,
        )

        multiplicative_growth = current_radius * 0.03
        static_growth = (
            effective_height() if orientation == "portrait" else effective_width()
        ) / 200
        current_radius += (
            multiplicative_growth
            if multiplicative_growth > static_growth
            else static_growth
        )
