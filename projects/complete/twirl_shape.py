from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.twirl.twirl_shapes import TwirlShapes


# requires grid rectangles to be square, and 4x6 grid, example config:
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

        match self.current_index:
            case 0:
                shapes.draw_a()
            case 1 | 2:
                shapes.draw_b()
            case 3:
                shapes.draw_c()
            case 4 | 8 | 12 | 16:
                shapes.draw_d()
            case 5 | 6 | 9 | 10 | 13 | 14 | 17 | 18:
                shapes.draw_e()
            case 7 | 11 | 15 | 19:
                shapes.draw_f()
            case 20:
                shapes.draw_g()
            case 21 | 22:
                shapes.draw_h()
            case 23:
                shapes.draw_i()
            case 24:
                shapes.draw_j()
