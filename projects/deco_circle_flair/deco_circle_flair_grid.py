from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.deco_circle_flair.deco_circle_flair import (
    draw_deco_circle_flair,
)


class DecoFlairObjectGrid(ObjectGridV2):
    def object_logic(
        self, plotter: PlotterInterface, start_index=0, iterations: int = None
    ):
        is_even_column = self.current_column % 2 == 0
        is_even_row = self.current_row % 2 == 0
        draw_up = (is_even_column and is_even_row) or (
            not is_even_column and not is_even_row
        )
        draw_deco_circle_flair(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y,
            width=self.square_width,
            height=self.square_height,
            up=draw_up,
        )
