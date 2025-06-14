from nextdraw import NextDraw
from projects.block_party.pieces import PieceGenerator

from projects.object_grid import ObjectGrid


class BlockPartyGridPieceIndex(ObjectGrid):
    pieces = []

    def object_logic(self, plotter: NextDraw):
        piece_generator = PieceGenerator(
            plotter=plotter,
            center_x=self.square_center_x,
            center_y=self.square_center_y,
            width=self.square_width - 0.1,
            height=self.square_height - 0.1,
        )
        index = len(self.pieces)

        match index:
            case 0:
                piece_generator.a()
                self.pieces.append("a")
            case 1:
                piece_generator.b()
                self.pieces.append("b")
            case 2:
                piece_generator.c()
                self.pieces.append("c")
            case 3:
                piece_generator.d()
                self.pieces.append("d")
            case 4:
                piece_generator.e()
                self.pieces.append("e")
            case 5:
                piece_generator.f()
                self.pieces.append("f")
            case 6:
                piece_generator.g()
                self.pieces.append("g")
            case 7:
                piece_generator.h()
                self.pieces.append("h")
            case 8:
                piece_generator.i()
                self.pieces.append("i")
            case 9:
                piece_generator.j()
                self.pieces.append("j")
            case 10:
                piece_generator.k()
                self.pieces.append("k")
            case 11:
                piece_generator.l()
                self.pieces.append("l")
            case 12:
                piece_generator.m()
                self.pieces.append("m")
            case 13:
                piece_generator.n()
                self.pieces.append("n")
            case 14:
                piece_generator.o()
                self.pieces.append("o")
            case 15:
                piece_generator.p()
                self.pieces.append("p")
            case 16:
                piece_generator.q()
                self.pieces.append("q")
