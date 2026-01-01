from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import draw_lined_circle


def draw_hatched_venn_diagram_horizontal(
    plotter: PlotterInterface,
    center_x: float,
    center_y: float,
    offset: float = 0.5,
    line_interval: float = 0.05,
    angle: int = 45,
    radius: float = 1,
):
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x + offset,
        center_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x - offset,
        center_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x + offset,
        center_y=center_y,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x - offset,
        center_y=center_y,
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
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y + offset,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y - offset,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y + offset,
        radius=radius,
        line_interval=line_interval,
        angle=-angle,
    )
    draw_lined_circle(
        plotter=plotter,
        center_x=center_x,
        center_y=center_y - offset,
        radius=radius,
        line_interval=line_interval,
        angle=angle,
    )
