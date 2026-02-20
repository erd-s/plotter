import random

from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.rectangles.rectangle import draw_filled_rectangle_with_origin


class FilledSquareObjectGrid(ObjectGridV2):
    pen_width_mm: float
    inset: float

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
        self.inset = (pen_width_mm * 0.039) * 2

    def object_logic(self, plotter: PlotterInterface):
        random_num = random.randint(0, 10000)
        if random_num > 6500:
            return

        draw_filled_rectangle_with_origin(
            plotter=plotter,
            origin_x=self.square_start_x + self.inset,
            origin_y=self.square_start_y + self.inset,
            width=self.square_width - (self.inset * 2),
            height=self.square_height - (self.inset * 2),
            pen_width_mm=self.pen_width_mm,
        )
