import random

from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.circles.circle_lines import create_lined_circle


class CircleLinesGrid(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        radius = (
            self.square_width / 2.5
            if self.square_width < self.square_height
            else self.square_height / 2.5
        )
        angle = int(random.uniform(0, 180))
        create_lined_circle(
            plotter=plotter,
            center_origin_x=self.square_center_x,
            center_origin_y=self.square_center_y,
            radius=radius,
            line_interval=radius / 6,
            angle=angle,
        )
