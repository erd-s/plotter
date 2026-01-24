from projects.object_grid_v2 import ObjectGridV2
from utils.plotter_interface import PlotterInterface
from projects.twirl.twirl_shapes import TwirlShapes
from projects.text.text import HorizontalText


class TwirlShapeIndex(ObjectGridV2):
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
                text = HorizontalText(
                    plotter=plotter,
                    text="a",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 1:
                shapes.draw_b()
                text = HorizontalText(
                    plotter=plotter,
                    text="b",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 2:
                shapes.draw_c()
                text = HorizontalText(
                    plotter=plotter,
                    text="c",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 3:
                shapes.draw_d()
                text = HorizontalText(
                    plotter=plotter,
                    text="d",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 4:
                shapes.draw_e()
                text = HorizontalText(
                    plotter=plotter,
                    text="e",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 5:
                shapes.draw_f()
                text = HorizontalText(
                    plotter=plotter,
                    text="f",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 6:
                shapes.draw_g()
                text = HorizontalText(
                    plotter=plotter,
                    text="g",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 7:
                shapes.draw_h()
                text = HorizontalText(
                    plotter=plotter,
                    text="h",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 8:
                shapes.draw_i()
                text = HorizontalText(
                    plotter=plotter,
                    text="i",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
            case 9:
                shapes.draw_j()
                text = HorizontalText(
                    plotter=plotter,
                    text="j",
                    origin_x=self.square_center_x - 0.075,
                    origin_y=self.square_center_y - 0.075,
                    width=0.15,
                    height=0.15,
                )
                text.draw_text()
