from utils.plotter_interface import PlotterInterface
from projects.circles.concentric_quarter_circle import (
    draw_concentric_quarter_circle_bottom_left,
    draw_concentric_quarter_circle_bottom_right,
    draw_concentric_quarter_circle_top_left,
    draw_concentric_quarter_circle_top_right,
)


class ConcentricQuarterCircleGenerator:
    plotter: PlotterInterface
    origin_x_start: float
    origin_x_end: float
    origin_y_start: float
    origin_y_end: float
    number_of_lines: int
    radius: float

    def __init__(
        self,
        plotter: PlotterInterface,
        origin_x_start: float,
        origin_x_end: float,
        origin_y_start: float,
        origin_y_end: float,
        number_of_lines: int,
    ):
        self.plotter = plotter
        self.origin_x_start = origin_x_start
        self.origin_x_end = origin_x_end
        self.origin_y_start = origin_y_start
        self.origin_y_end = origin_y_end
        self.number_of_lines = number_of_lines
        self.radius = (origin_x_end - origin_x_start) * 0.45

    def a(self):
        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def b(self):
        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def c(self):
        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def d(self):
        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def e(self):
        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def f(self):
        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def g(self):
        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def h(self):
        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def i(self):
        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def j(self):
        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )

    def k(self):
        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_start,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.origin_x_start,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.origin_x_end,
            center_y=self.origin_y_end,
            radius=self.radius,
            number_of_lines=self.number_of_lines,
        )
