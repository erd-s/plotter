import random

from utils.plotter_interface import PlotterInterface
from projects.object_grid_v2 import ObjectGridV2
from projects.polygon.polygon import draw_polygon


class HoneycombGrid(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        if random.randint(0, 10) > 6:
            return

        height = self.square_width
        y_offset = height / -2 if self.current_column % 2 == 0 else 0

        draw_polygon(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y + y_offset,
            number_of_sides=6,
            height=height * 0.9,
        )
