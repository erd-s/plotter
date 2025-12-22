from utils.plotter_interface import PlotterInterface
from projects.circles.semicircle import semicircle_path
from projects.spiro.spiraled_path import create_spiraled_shape


def create_iterative_semicircles(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    radius: float = 0.6,
    open_middle_radius: float = 0,
    degree_interval: int = 6,
):
    original_path = semicircle_path(
        origin_x=center_x, origin_y=center_y - radius, radius=radius
    )
    create_spiraled_shape(
        plotter=plotter,
        shape_path=original_path,
        shape_center_x=original_path[0][0] - open_middle_radius,
        shape_center_y=original_path[0][1] - open_middle_radius,
        degree_interval=degree_interval,
    )


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
        center_x=effective_x_start + x_inset,
        center_y=effective_y_start + y_inset,
        radius=radius,
    )
    create_iterative_semicircles(
        plotter=plotter,
        center_x=effective_x_end - x_inset,
        center_y=effective_y_start + y_inset,
        radius=radius,
    )
    create_iterative_semicircles(
        plotter=plotter,
        center_x=effective_x_start + x_inset,
        center_y=effective_y_end - y_inset,
        radius=radius,
    )
    create_iterative_semicircles(
        plotter=plotter,
        center_x=effective_x_end - x_inset,
        center_y=effective_y_end - y_inset,
        radius=radius,
    )

    if with_large_center:
        create_iterative_semicircles(
            plotter=plotter,
            center_x=center_x,
            center_y=center_y,
            radius=1,
            degree_interval=4,
        )
