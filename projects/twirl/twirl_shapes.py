from projects.circles.concentric_quarter_circle import (
    draw_concentric_quarter_circle_bottom_right,
    draw_concentric_quarter_circle_bottom_left,
    draw_concentric_quarter_circle_top_left,
    draw_concentric_quarter_circle_top_right,
)
from utils.plotter_interface import PlotterInterface


class TwirlShapes:
    plotter: PlotterInterface
    start_x: float
    start_y: float
    end_x: float
    end_y: float
    width: float
    height: float

    def __init__(
        self,
        plotter: PlotterInterface,
        start_x: float,
        start_y: float,
        end_x: float,
        end_y: float,
    ):
        self.plotter = plotter
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.width = self.end_x - self.start_x
        self.height = self.end_y - self.start_y

    def draw_a(self):
        inside_radius = self.width / 6
        outside_radius = self.width / 2

        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.end_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.end_y,
            radius=outside_radius,
            number_of_lines=1,
        )

    def draw_b(self):
        top_line_y = self.start_y + (self.height / 2)
        bottom_line_y = self.end_y - (self.height / 6)
        top_line_path = [[self.start_x, top_line_y], [self.end_x, top_line_y]]
        bottom_line_path = [[self.start_x, bottom_line_y], [self.end_x, bottom_line_y]]
        self.plotter.draw_path(top_line_path)
        self.plotter.draw_path(bottom_line_path)

    def draw_c(self):
        inside_radius = self.width / 6
        outside_radius = self.width / 2

        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.end_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.end_y,
            radius=outside_radius,
            number_of_lines=1,
        )

    def draw_d(self):
        inside_radius = self.width / 6
        outside_radius = self.width / 2

        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.start_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.start_y,
            radius=outside_radius,
            number_of_lines=1,
        )

        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.end_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_bottom_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.end_y,
            radius=outside_radius,
            number_of_lines=1,
        )

    def draw_e(self):
        top_y = self.start_y + (self.height / 6)
        center_y = self.start_y + (self.height / 2)
        bottom_y = self.end_y - (self.height / 6)
        center_x = self.start_x + (self.width / 2)
        first_third_y = self.start_y + (self.height / 3)
        second_third_y = self.end_y - (self.height / 3)

        line_one = [[self.start_x, top_y], [self.end_x, center_y]]
        line_two = [[self.start_x, center_y], [self.end_x, bottom_y]]
        line_three = [[self.start_x, bottom_y], [center_x, second_third_y]]
        line_four = [[center_x, first_third_y], [self.end_x, top_y]]

        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)
        self.plotter.draw_path(line_three)
        self.plotter.draw_path(line_four)

    def draw_f(self):
        inside_radius = self.width / 6
        outside_radius = self.width / 2

        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.start_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.start_y,
            radius=outside_radius,
            number_of_lines=1,
        )

        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.end_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_bottom_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.end_y,
            radius=outside_radius,
            number_of_lines=1,
        )

    def draw_g(self):
        inside_radius = self.width / 6
        outside_radius = self.width / 2

        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.start_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_top_right(
            plotter=self.plotter,
            center_x=self.end_x,
            center_y=self.start_y,
            radius=outside_radius,
            number_of_lines=1,
        )

    def draw_h(self):
        top_line_y = self.start_y + (self.height / 6)
        bottom_line_y = self.start_y + (self.height / 2)
        top_line_path = [[self.start_x, top_line_y], [self.end_x, top_line_y]]
        bottom_line_path = [[self.start_x, bottom_line_y], [self.end_x, bottom_line_y]]
        self.plotter.draw_path(top_line_path)
        self.plotter.draw_path(bottom_line_path)

    def draw_i(self):
        inside_radius = self.width / 6
        outside_radius = self.width / 2

        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.start_y,
            radius=inside_radius,
            number_of_lines=1,
        )
        draw_concentric_quarter_circle_top_left(
            plotter=self.plotter,
            center_x=self.start_x,
            center_y=self.start_y,
            radius=outside_radius,
            number_of_lines=1,
        )

    def draw_j(self):
        pass
