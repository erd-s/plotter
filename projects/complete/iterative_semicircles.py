from utils.plotter_interface import PlotterInterface
from projects.circles.semicircle import semicircle_path
from utils.transform import rotate
from projects.iterate_around.iterate_around import iterate_around


def create_iterative_semicircles(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    radius: float,
    degree_interval: int = 9,
):
    original_path = semicircle_path(
        origin_x=origin_x, origin_y=origin_y - radius, radius=radius
    )
    iterate_around(plotter=plotter, original_path=original_path, degree_interval=degree_interval)


def create_four_corner_iterative_semicircles(
    plotter: PlotterInterface,
    effective_x_start: float,
    effective_x_end: float,
    effective_y_start: float,
    effective_y_end: float,
    center_x: float,
    center_y: float,
    with_large_center: bool = True,
):
    x_inset = 0.6
    y_inset = 0.65
    radius = 0.275
    create_iterative_semicircles(
        plotter=plotter,
        origin_x=effective_x_start + x_inset,
        origin_y=effective_y_start + y_inset,
        radius=radius,
    )
    create_iterative_semicircles(
        plotter=plotter,
        origin_x=effective_x_end - x_inset,
        origin_y=effective_y_start + y_inset,
        radius=radius,
    )
    create_iterative_semicircles(
        plotter=plotter,
        origin_x=effective_x_start + x_inset,
        origin_y=effective_y_end - y_inset,
        radius=radius,
    )
    create_iterative_semicircles(
        plotter=plotter,
        origin_x=effective_x_end - x_inset,
        origin_y=effective_y_end - y_inset,
        radius=radius,
    )

    if with_large_center:
        create_iterative_semicircles(
            plotter=plotter,
            origin_x=center_x,
            origin_y=center_y,
            radius=1,
            degree_interval=4,
        )
