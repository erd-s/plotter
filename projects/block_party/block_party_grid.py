import random
from utils.plotter_interface import PlotterInterface
from projects.block_party.pieces import PieceGenerator

from projects.object_grid import ObjectGrid


class BlockPartyGrid(ObjectGrid):
    pieces = []

    def object_logic(self, plotter: PlotterInterface):
        piece_generator = PieceGenerator(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y,
            width=self.square_width,
            height=self.square_height,
        )
        index = len(self.pieces)

        above = ""
        left = ""

        if index >= self.grid_size:
            above = self.pieces[index - self.grid_size]

        if index % self.grid_size != 0:
            left = self.pieces[index - 1]

        open_bottom = ["a", "b", "f", "g", "k", "n", "o", "p", "q"]
        closed_bottom = ["c", "d", "e", "h", "i", "j", "l", "m"]
        open_right = ["a", "c", "e", "g", "h", "m", "o", "p", "q"]
        closed_right = ["b", "d", "f", "i", "j", "k", "l", "n"]
        open_top = ["d", "e", "f", "g", "j", "m", "n", "p", "q"]
        closed_top = ["a", "b", "c", "h", "i", "k", "l", "o"]
        open_left = ["b", "c", "d", "g", "i", "m", "n", "o", "q"]
        closed_left = ["a", "e", "f", "h", "j", "k", "l", "p"]

        open_top_open_left = [item for item in open_top if item in open_left]
        open_left_closed_top = [item for item in open_left if item in closed_top]
        open_top_closed_left = [item for item in open_top if item in closed_left]
        closed_top_closed_left = [item for item in closed_top if item in closed_left]
        closed_bottom_closed_right = [
            item for item in closed_bottom if item in closed_right
        ]
        should_connect_with_above = above in open_bottom
        should_connect_with_left = left in open_right

        if should_connect_with_left and should_connect_with_above:
            options = open_top_open_left
        elif should_connect_with_left:
            options = open_left_closed_top
        elif should_connect_with_above:
            options = open_top_closed_left
        else:
            options = closed_top_closed_left

        is_in_right_column = (index + 1) % self.grid_size == 0
        is_in_bottom_row = index >= (self.grid_size * self.grid_size) - self.grid_size
        is_last = is_in_right_column and is_in_bottom_row

        if is_last:
            # cant have open right or open bottom in last index
            options = list(filter(lambda o: (o in closed_bottom_closed_right), options))
        elif is_in_right_column:
            # can't have an open right on right column
            options = list(filter(lambda o: o not in open_right, options))
        elif is_in_bottom_row:
            # can't have an open bottom on bottom row
            options = list(filter(lambda o: o not in open_bottom, options))

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
            case "e":
                piece_generator.e()
            case "f":
                piece_generator.f()
            case "g":
                piece_generator.g()
            case "h":
                piece_generator.h()
            case "i":
                piece_generator.i()
            case "j":
                piece_generator.j()
            case "k":
                piece_generator.k()
            case "l":
                piece_generator.l()
            case "m":
                piece_generator.m()
            case "n":
                piece_generator.n()
            case "o":
                piece_generator.o()
            case "p":
                piece_generator.p()
            case "q":
                piece_generator.q()

        self.pieces.append(selected_option)
