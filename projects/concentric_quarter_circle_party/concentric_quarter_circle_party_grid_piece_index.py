from utils.plotter_interface import PlotterInterface
from projects.concentric_quarter_circle_party.pieces import (
    ConcentricQuarterCircleGenerator,
)

from projects.object_grid_v2 import ObjectGridV2
from projects.text.text import HorizontalText
from utils.transform import centered_paths


class ConcentricQuarterCirclePartyGridPieceIndex(ObjectGridV2):
    pieces = []

    def object_logic(self, plotter: PlotterInterface):
        piece_generator = ConcentricQuarterCircleGenerator(
            plotter=plotter,
            origin_x_start=self.square_start_x,
            origin_x_end=self.square_end_x,
            origin_y_start=self.square_start_y,
            origin_y_end=self.square_end_y,
            number_of_lines=5,
        )
        index = len(self.pieces)

        match index:
            case 0:
                piece_generator.a()
                text = HorizontalText(
                    plotter=plotter,
                    text="a",
                    origin_x=self.square_center_x,
                    origin_y=self.square_center_y,
                    width=self.square_width / 10,
                )
                paths = text.text_paths()
                centered_text_paths = centered_paths(
                    paths=paths,
                    around_x=self.square_center_x,
                    around_y=self.square_center_y,
                )
                for path in centered_text_paths:
                    plotter.draw_path(path)
                self.pieces.append("a")
            case 1:
                piece_generator.b()
                text = HorizontalText(
                    plotter=plotter,
                    text="b",
                    origin_x=self.square_center_x,
                    origin_y=self.square_center_y,
                    width=self.square_width / 10,
                )
                paths = text.text_paths()
                centered_text_paths = centered_paths(
                    paths=paths,
                    around_x=self.square_center_x,
                    around_y=self.square_center_y,
                )
                for path in centered_text_paths:
                    plotter.draw_path(path)
                self.pieces.append("b")
            case 2:
                piece_generator.c()
                text = HorizontalText(
                    plotter=plotter,
                    text="c",
                    origin_x=self.square_center_x,
                    origin_y=self.square_center_y,
                    width=self.square_width / 10,
                )
                paths = text.text_paths()
                centered_text_paths = centered_paths(
                    paths=paths,
                    around_x=self.square_center_x,
                    around_y=self.square_center_y,
                )
                for path in centered_text_paths:
                    plotter.draw_path(path)
                self.pieces.append("c")
            case 3:
                piece_generator.d()
                text = HorizontalText(
                    plotter=plotter,
                    text="d",
                    origin_x=self.square_center_x,
                    origin_y=self.square_center_y,
                    width=self.square_width / 10,
                )
                paths = text.text_paths()
                centered_text_paths = centered_paths(
                    paths=paths,
                    around_x=self.square_center_x,
                    around_y=self.square_center_y,
                )
                for path in centered_text_paths:
                    plotter.draw_path(path)
                self.pieces.append("d")
            case 4:
                piece_generator.e()
                text = HorizontalText(
                    plotter=plotter,
                    text="e",
                    origin_x=self.square_center_x,
                    origin_y=self.square_center_y,
                    width=self.square_width / 10,
                )
                paths = text.text_paths()
                centered_text_paths = centered_paths(
                    paths=paths,
                    around_x=self.square_center_x,
                    around_y=self.square_center_y,
                )
                for path in centered_text_paths:
                    plotter.draw_path(path)
                self.pieces.append("e")
            case 5:
                piece_generator.f()
                text = HorizontalText(
                    plotter=plotter,
                    text="f",
                    origin_x=self.square_center_x,
                    origin_y=self.square_center_y,
                    width=self.square_width / 10,
                )
                paths = text.text_paths()
                centered_text_paths = centered_paths(
                    paths=paths,
                    around_x=self.square_center_x,
                    around_y=self.square_center_y,
                )
                for path in centered_text_paths:
                    plotter.draw_path(path)
                self.pieces.append("f")
