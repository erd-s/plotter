import random

from utils.plotter_interface import PlotterInterface
from projects.object_grid_v2 import ObjectGridV2
from projects.dash_block.dash_line import DashLine
from projects.text.text import HorizontalText


class DashBlockIndex(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        line = DashLine(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_start_y,
            length=self.square_height,
            vertical_orientation=True,
        )

        text_size = self.square_height / 6

        if self.current_index == 0:
            text = HorizontalText(
                plotter=plotter,
                text="a",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_a()
        elif self.current_index == 1:
            text = HorizontalText(
                plotter=plotter,
                text="b",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_b()
        elif self.current_index == 2:
            text = HorizontalText(
                plotter=plotter,
                text="c",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_c()
        elif self.current_index == 3:
            text = HorizontalText(
                plotter=plotter,
                text="d",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_d()
        elif self.current_index == 4:
            text = HorizontalText(
                plotter=plotter,
                text="e",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_e()
        elif self.current_index == 5:
            text = HorizontalText(
                plotter=plotter,
                text="f",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_f()
        elif self.current_index == 6:
            text = HorizontalText(
                plotter=plotter,
                text="g",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_g()
        elif self.current_index == 7:
            text = HorizontalText(
                plotter=plotter,
                text="h",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_h()
        elif self.current_index == 8:
            text = HorizontalText(
                plotter=plotter,
                text="i",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_i()
        elif self.current_index == 9:
            text = HorizontalText(
                plotter=plotter,
                text="j",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_j()
        elif self.current_index == 10:
            text = HorizontalText(
                plotter=plotter,
                text="k",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_k()


class DashBlockGrid(ObjectGridV2):
    space_between_lines: float
    pen_width_in: float

    def __init__(
        self,
        grid_size_horizontal: int,
        grid_size_vertical: int,
        origin_x: float,
        origin_y: float,
        space_between_lines: float,
        pen_width_mm: float,
        width: float,
        height: float,
        margin: float = 0,
        inset: float = 0,
        draw_grid_lines: bool = False,
    ):
        super().__init__(
            grid_size_horizontal,
            grid_size_vertical,
            origin_x,
            origin_y,
            width,
            height,
            margin,
            inset,
            draw_grid_lines,
        )
        self.space_between_lines = space_between_lines
        self.pen_width_in = pen_width_mm * 0.039

    def object_logic(self, plotter: PlotterInterface):
        number_of_iterations = int(
            self.square_width / (self.space_between_lines + self.pen_width_in)
        )
        total_penned_width = number_of_iterations * self.pen_width_in
        total_unpenned_width = self.square_width - total_penned_width

        actual_spacing_between_lines = total_unpenned_width / (number_of_iterations - 1)

        print(f"number of iterations per square: {number_of_iterations}")

        for i in range(number_of_iterations):
            x_position = self.square_start_x + (
                i * (self.pen_width_in + actual_spacing_between_lines)
            )
            line = DashLine(
                plotter=plotter,
                origin_x=x_position,
                origin_y=self.square_start_y,
                length=self.square_height,
                vertical_orientation=True,
            )

            if i == 0 or (i == number_of_iterations - 1):
                line.draw_variant_l()
                continue

            rand_index = random.randint(0, 11)

            if rand_index == 0:
                line.draw_variant_a()
            if rand_index == 1:
                line.draw_variant_b()
            if rand_index == 2:
                line.draw_variant_c()
            if rand_index == 3:
                line.draw_variant_d()
            if rand_index == 4:
                line.draw_variant_e()
            if rand_index == 5:
                line.draw_variant_f()
            if rand_index == 6:
                line.draw_variant_g()
            if rand_index == 7:
                line.draw_variant_h()
            if rand_index == 8:
                line.draw_variant_i()
            if rand_index == 9:
                line.draw_variant_j()
            if rand_index == 10:
                line.draw_variant_k()
            if rand_index == 11:
                line.draw_variant_l()
