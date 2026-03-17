import random

from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.squiggle_fill.squiggle_path import draw_squiggle_rectangle_rounded_path
from utils.transform import rotated_path


class SquiggleGrid(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        rotation_options = [0]
        random_rotation_index = random.randint(0, len(rotation_options) - 1)
        rotation = rotation_options[random_rotation_index]
        space_between_lines = self.inset * 2
        squiggle_path = draw_squiggle_rectangle_rounded_path(
            origin_x=self.square_start_x,
            origin_y=self.square_start_y,
            height=self.square_height,
            width=self.square_width,
            space_between_lines=space_between_lines,
        )

        rotated_squiggle_path = rotated_path(
            path=squiggle_path,
            degrees=rotation,
            rotation_x=self.square_center_x,
            rotation_y=self.square_center_y,
        )
        plotter.draw_path(rotated_squiggle_path)
