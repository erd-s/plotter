from utils.plotter_interface import PlotterInterface
from projects.object_grid_v2 import ObjectGridV2
from projects.dash_block.dash_line import DashLine
from projects.text.text import HorizontalText


class DashBlock(ObjectGridV2):
    def object_logic(self, plotter: PlotterInterface):
        line = DashLine(
            plotter=plotter,
            origin_x=self.square_center_x,
            origin_y=self.square_start_y,
            length=self.square_height,
            vertical_orientation=True,
        )

        text_size = self.square_height / 6

        if self.current_index == 0:
            text = HorizontalText(
                plotter=plotter,
                text="a",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_a()
        elif self.current_index == 1:
            text = HorizontalText(
                plotter=plotter,
                text="b",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_b()
        elif self.current_index == 2:
            text = HorizontalText(
                plotter=plotter,
                text="c",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_c()
        elif self.current_index == 3:
            text = HorizontalText(
                plotter=plotter,
                text="d",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_d()
        elif self.current_index == 4:
            text = HorizontalText(
                plotter=plotter,
                text="e",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_e()
        elif self.current_index == 5:
            text = HorizontalText(
                plotter=plotter,
                text="f",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_f()
        elif self.current_index == 6:
            text = HorizontalText(
                plotter=plotter,
                text="g",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_g()
        elif self.current_index == 7:
            text = HorizontalText(
                plotter=plotter,
                text="h",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_h()
        elif self.current_index == 8:
            text = HorizontalText(
                plotter=plotter,
                text="i",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_i()
        elif self.current_index == 9:
            text = HorizontalText(
                plotter=plotter,
                text="j",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_j()
        elif self.current_index == 10:
            text = HorizontalText(
                plotter=plotter,
                text="k",
                origin_x=self.square_start_x,
                origin_y=self.square_center_y - text_size / 2,
                height=text_size,
                width=text_size,
            )
            text.draw_text()
            line.draw_variant_k()
