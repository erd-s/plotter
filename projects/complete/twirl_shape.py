from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.twirl.twirl_shapes import TwirlShapes


# requires grid rectangles to be square, and 2:3 grid, example config:
# DOC_HEIGHT = 8.27
# MARGIN_TOP = 0.235
# MARGIN_BOTTOM = 0.235
#
# DOC_WIDTH = 5.83
# MARGIN_LEFT = 0.315
# MARGIN_RIGHT = 0.315
class TwirlShape(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        shapes = TwirlShapes(
            plotter=plotter,
            start_x=self.square_start_x,
            start_y=self.square_start_y,
            end_x=self.square_end_x,
            end_y=self.square_end_y,
        )

        if self.current_column == 0:
            if self.current_row == 0:
                shapes.draw_a()
            elif self.current_row == self.grid_size_vertical - 1:
                shapes.draw_g()
            else:
                shapes.draw_d()
        elif self.current_column == self.grid_size_horizontal - 1:
            if self.current_row == 0:
                shapes.draw_c()
            elif self.current_row == self.grid_size_vertical - 1:
                shapes.draw_i()
            else:
                shapes.draw_f()
        else:
            if self.current_row == 0:
                shapes.draw_b()
            elif self.current_row == self.grid_size_vertical - 1:
                shapes.draw_h()
            else:
                shapes.draw_e()
