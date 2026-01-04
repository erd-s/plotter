import random
from utils.plotter_interface import PlotterInterface
from projects.concentric_quarter_circle_party.pieces import (
    ConcentricQuarterCircleGenerator,
)

from projects.object_grid_v2 import ObjectGridV2


class ConcentricQuarterCirclePartyGrid(ObjectGridV2):
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

        options = ["a", "b", "c", "d"]

        open_left = ["a", "d"]
        open_right = ["b", "c"]
        open_top = ["a", "b"]
        open_bottom = ["c", "d"]

        is_first_column = self.current_column == 0
        is_last_column = self.current_column == self.grid_size_horizontal - 1
        if_is_first_row = self.current_row == 0
        is_last_row = self.current_row == self.grid_size_vertical - 1

        if is_first_column:
            options = list(filter(lambda o: o in open_left, options))

        if is_last_column:
            options = list(filter(lambda o: o in open_right, options))

        if if_is_first_row:
            options = list(filter(lambda o: o in open_top, options))

        if is_last_row:
            options = list(filter(lambda o: o in open_bottom, options))

        option_index = random.randint(0, len(options) - 1)
        selected_option = options[option_index]

        match selected_option:
            case "a":
                piece_generator.a()
            case "b":
                piece_generator.b()
            case "c":
                piece_generator.c()
            case "d":
                piece_generator.d()

        self.pieces.append(selected_option)
