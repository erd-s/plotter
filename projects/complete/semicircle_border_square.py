from utils.plotter_interface import PlotterInterface
from projects.border.semicircle_border import draw_semicircle_border


def draw_semicircle_border_square(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    width: float,
    semicircles_across: int = 8,
):
    diameter = width / semicircles_across
    radius = diameter / 2
    iterations = round(width / (diameter * 2))

    for i in range(iterations):
        x = origin_x + (i * diameter)
        y = origin_y + (i * diameter)
        w = width - (i * diameter * 2)
        draw_semicircle_border(
            plotter=plotter, origin_x=x, origin_y=y, width=w, height=w, radius=radius
        )
