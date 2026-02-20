import random

from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.circles.circle import draw_filled_circle


class FilledCircleObjectGrid(ObjectGridV2):
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
        radius = self.square_width / 3
        random_num = random.randint(0, 10000)
        if random_num > 5500:
            return

        draw_filled_circle(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y,
            radius=radius,
            pen_width_mm=self.pen_width_mm,
        )
