import random
from nextdraw import NextDraw
from projects.block_party.pieces import PieceGenerator

from projects.object_grid import ObjectGrid


class BlockPartyGrid(ObjectGrid):
    pieces = []

    def object_logic(self, plotter: NextDraw):
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

        should_connect_with_above = above in ("a", "b", "f", "g", "k")
        should_connect_with_left = left in ("a", "c", "e", "g", "h")

        if should_connect_with_left and should_connect_with_above:
            options = ["d", "g"]
        elif should_connect_with_left:
            options = ["b", "c", "i"]
        elif should_connect_with_above:
            options = ["e", "f", "j"]
        else:
            options = ["a", "h", "k", "l"]

        if (index + 1) % self.grid_size == 0:
            # can't have an open right on right column
            options = list(
                filter(lambda o: o not in ("a", "c", "e", "g", "h"), options)
            )

        if index >= (self.grid_size * self.grid_size) - self.grid_size:
            # can't have an open bottom on bottom row
            options = list(
                filter(lambda o: o not in ("a", "b", "f", "g", "k"), options)
            )

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

        self.pieces.append(selected_option)
