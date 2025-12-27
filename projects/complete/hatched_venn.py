from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import create_lined_circle


def draw_hatched_venn_diagram_horizontal(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    offset: float = 0.5,
    line_interval: float = 0.05,
    angle: int = 45,
    radius: float = 1,
):
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x + offset,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x - offset,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x + offset,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x - offset,
        center_origin_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )


def draw_hatched_venn_diagram_vertical(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    offset: float = 0.5,
    line_interval: float = 0.05,
    angle: int = 45,
    radius: float = 1,
):
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y + offset,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y - offset,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y + offset,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    create_lined_circle(
        plotter=plotter,
        center_origin_x=center_x,
        center_origin_y=center_y - offset,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
