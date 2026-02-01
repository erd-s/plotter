from projects.object_grid_v2 import ObjectGridV2
from projects.circles.circle import draw_circle_v2
from utils.plotter_interface import PlotterInterface


class MarkOfAzaliahGrid(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        radius = 0.4
        y_offset = -(radius / 2)

        # vertical line
        vertical_line_start_y = self.square_center_y + radius + y_offset
        vertical_line_end_y = vertical_line_start_y + radius
        vertical_line_path = [
            [self.square_center_x, vertical_line_start_y],
            [self.square_center_x, vertical_line_end_y],
        ]

        # horizontal line
        horizontal_line_y = vertical_line_start_y + (radius * 0.75)
        horizontal_line_start_x = self.square_center_x - (radius / 4)
        horizontal_line_end_x = self.square_center_x + (radius / 4)
        horizontal_line_path = [
            [horizontal_line_start_x, horizontal_line_y],
            [horizontal_line_end_x, horizontal_line_y],
        ]

        draw_circle_v2(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y + y_offset,
            radius=radius,
        )
        plotter.draw_path(vertical_line_path)
        plotter.draw_path(horizontal_line_path)
