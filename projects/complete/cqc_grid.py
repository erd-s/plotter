from utils.plotter_interface import PlotterInterface
from projects.object_grid_v2 import ObjectGridV2
from projects.circles.concentric_quarter_circle import (
    draw_concentric_quarter_circle_bottom_left,
    draw_concentric_quarter_circle_top_right,
)


class CQCGrid(ObjectGridV2):
    number_of_lines: int

    def __init__(
        self,
        grid_size_horizontal: int,
        grid_size_vertical: int,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        number_of_lines: int,
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
        self.number_of_lines = number_of_lines

    def object_logic(self, plotter: PlotterInterface):
        # these two make a wavy pattern
        draw_concentric_quarter_circle_bottom_left(
            plotter=plotter,
            center_x=self.square_start_x,
            center_y=self.square_start_y + self.square_height,
            number_of_lines=self.number_of_lines,
            radius=self.square_width,
        )
        draw_concentric_quarter_circle_top_right(
            plotter=plotter,
            center_x=self.square_start_x + self.square_width,
            center_y=self.square_start_y,
            number_of_lines=self.number_of_lines,
            radius=self.square_width,
        )

        # uncomment these to make the full circle pattern
        # draw_concentric_quarter_circle_top_left(
        #     plotter=plotter,
        #     center_x=self.square_start_x,
        #     center_y=self.square_start_y,
        #     number_of_lines=self.number_of_lines,
        #     radius=self.square_width,
        # )
        # draw_concentric_quarter_circle_bottom_right(
        #     plotter=plotter,
        #     center_x=self.square_start_x + self.square_width,
        #     center_y=self.square_start_y + self.square_height,
        #     number_of_lines=self.number_of_lines,
        #     radius=self.square_width,
        # )
