from utils.plotter_interface import PlotterInterface
from projects.object_grid_v2 import ObjectGridV2
from projects.dash_block.dash_line import DashLine


class DashBlock(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        line = DashLine(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_start_y,
            length=self.square_height,
            vertical_orientation=True,
        )

        if self.current_index == 0:
            line.draw_variant_a()
        elif self.current_index == 1:
            line.draw_variant_b()
        elif self.current_index == 2:
            line.draw_variant_c()
        elif self.current_index == 3:
            line.draw_variant_d()
        elif self.current_index == 4:
            line.draw_variant_e()
        elif self.current_index == 5:
            line.draw_variant_f()
        elif self.current_index == 6:
            line.draw_variant_g()
        elif self.current_index == 7:
            line.draw_variant_h()
        elif self.current_index == 8:
            line.draw_variant_i()
        elif self.current_index == 9:
            line.draw_variant_j()
        elif self.current_index == 10:
            line.draw_variant_k()
