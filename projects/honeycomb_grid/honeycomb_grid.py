import random

from utils.plotter_interface import PlotterInterface
from projects.object_grid_v2 import ObjectGridV2
from projects.polygon.polygon import draw_polygon, draw_filled_polygon


class HoneycombGrid(ObjectGridV2):
    pen_width_mm: float

    def __init__(
        self,
        grid_size_horizontal: int,
        grid_size_vertical: int,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        pen_width_mm: float,
        margin: float = 0,
    ):
        super().__init__(
            grid_size_horizontal=grid_size_horizontal,
            grid_size_vertical=grid_size_vertical,
            origin_x=origin_x,
            origin_y=origin_y,
            width=width,
            height=height,
            margin=margin,
        )
        self.pen_width_mm = pen_width_mm

    def object_logic(self, plotter: PlotterInterface):
        height = self.square_width
        y_offset = height / -4 if self.current_column % 2 == 0 else height / 4

        if random.randint(0, 100) >= 85:
            draw_filled_polygon(
                plotter=plotter,
                center_x=self.square_center_x,
                center_y=self.square_center_y + y_offset,
                number_of_sides=6,
                height=height * 0.9,
                pen_width_mm=self.pen_width_mm,
            )
        else:
            draw_polygon(
                plotter=plotter,
                center_x=self.square_center_x,
                center_y=self.square_center_y + y_offset,
                number_of_sides=6,
                height=height * 0.9,
            )
