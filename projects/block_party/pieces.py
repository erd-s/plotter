from nextdraw import NextDraw


class GridPoint:
    center_x: float
    center_y: float
    width: float
    height: float
    thinness_coefficient: int = 2.5

    def __init__(self, center_x: float, center_y: float, width: float, height: float):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

    def a(self):
        x = self.center_x - self.width / 2
        y = self.center_y - self.height / 2
        return [x, y]

    def b(self):
        x = self.center_x - self.width / self.thinness_coefficient
        y = self.center_y - self.height / 2
        return [x, y]

    def c(self):
        x = self.center_x + self.width / self.thinness_coefficient
        y = self.center_y - self.height / 2
        return [x, y]

    def d(self):
        x = self.center_x + self.width / 2
        y = self.center_y - self.height / 2
        return [x, y]

    def e(self):
        x = self.center_x - self.width / 2
        y = self.center_y - self.height / self.thinness_coefficient
        return [x, y]

    def f(self):
        x = self.center_x - self.width / self.thinness_coefficient
        y = self.center_y - self.height / self.thinness_coefficient
        return [x, y]

    def g(self):
        x = self.center_x + self.width / self.thinness_coefficient
        y = self.center_y - self.height / self.thinness_coefficient
        return [x, y]

    def h(self):
        x = self.center_x + self.width / 2
        y = self.center_y - self.height / self.thinness_coefficient
        return [x, y]

    def i(self):
        x = self.center_x - self.width / 2
        y = self.center_y + self.height / self.thinness_coefficient
        return [x, y]

    def j(self):
        x = self.center_x - self.width / self.thinness_coefficient
        y = self.center_y + self.height / self.thinness_coefficient
        return [x, y]

    def k(self):
        x = self.center_x + self.width / self.thinness_coefficient
        y = self.center_y + self.height / self.thinness_coefficient
        return [x, y]

    def l(self):
        x = self.center_x + self.width / 2
        y = self.center_y + self.height / self.thinness_coefficient
        return [x, y]

    def m(self):
        x = self.center_x - self.width / 2
        y = self.center_y + self.height / 2
        return [x, y]

    def n(self):
        x = self.center_x - self.width / self.thinness_coefficient
        y = self.center_y + self.height / 2
        return [x, y]

    def o(self):
        x = self.center_x + self.width / self.thinness_coefficient
        y = self.center_y + self.height / 2
        return [x, y]

    def p(self):
        x = self.center_x + self.width / 2
        y = self.center_y + self.height / 2
        return [x, y]


class PieceGenerator:
    plotter: NextDraw
    grid_point: GridPoint

    def __init__(
        self,
        plotter: NextDraw,
        center_x: float,
        center_y: float,
        width: float,
        height: float,
    ):
        self.plotter = plotter
        self.grid_point = GridPoint(
            center_x=center_x, center_y=center_y, width=width, height=height
        )

    def a(self):
        line_one = [self.grid_point.n(), self.grid_point.f(), self.grid_point.h()]
        line_two = [self.grid_point.o(), self.grid_point.k(), self.grid_point.l()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)

    def b(self):
        line_one = [self.grid_point.e(), self.grid_point.g(), self.grid_point.o()]
        line_two = [self.grid_point.i(), self.grid_point.j(), self.grid_point.n()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)

    def c(self):
        line_one = [self.grid_point.e(), self.grid_point.h()]
        line_two = [self.grid_point.i(), self.grid_point.l()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)

    def d(self):
        line_one = [self.grid_point.e(), self.grid_point.f(), self.grid_point.b()]
        line_two = [self.grid_point.i(), self.grid_point.k(), self.grid_point.c()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)

    def e(self):
        line_one = [self.grid_point.b(), self.grid_point.j(), self.grid_point.l()]
        line_two = [self.grid_point.c(), self.grid_point.g(), self.grid_point.h()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)

    def f(self):
        line_one = [self.grid_point.b(), self.grid_point.n()]
        line_two = [self.grid_point.c(), self.grid_point.o()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)

    def g(self):
        line_one = [self.grid_point.b(), self.grid_point.n()]
        line_two = [self.grid_point.c(), self.grid_point.o()]
        line_three = [self.grid_point.e(), self.grid_point.f()]
        line_four = [self.grid_point.i(), self.grid_point.j()]
        line_five = [self.grid_point.g(), self.grid_point.h()]
        line_six = [self.grid_point.k(), self.grid_point.l()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)
        self.plotter.draw_path(line_three)
        self.plotter.draw_path(line_four)
        self.plotter.draw_path(line_five)
        self.plotter.draw_path(line_six)

    def h(self):
        line_one = [
            self.grid_point.h(),
            self.grid_point.f(),
            self.grid_point.j(),
            self.grid_point.l(),
        ]
        self.plotter.draw_path(line_one)

    def i(self):
        line_one = [
            self.grid_point.e(),
            self.grid_point.g(),
            self.grid_point.k(),
            self.grid_point.i(),
        ]
        self.plotter.draw_path(line_one)

    def j(self):
        line_one = [
            self.grid_point.b(),
            self.grid_point.j(),
            self.grid_point.k(),
            self.grid_point.c(),
        ]
        self.plotter.draw_path(line_one)

    def k(self):
        line_one = [
            self.grid_point.n(),
            self.grid_point.f(),
            self.grid_point.g(),
            self.grid_point.o(),
        ]
        self.plotter.draw_path(line_one)

    def l(self):
        line_one = [
            self.grid_point.f(),
            self.grid_point.g(),
            self.grid_point.k(),
            self.grid_point.j(),
            self.grid_point.f(),
        ]
        self.plotter.draw_path(line_one)

    def m(self):
        line_one = [
            self.grid_point.e(),
            self.grid_point.f(),
            self.grid_point.b()
        ]
        line_two = [
            self.grid_point.c(),
            self.grid_point.g(),
            self.grid_point.h()
        ]
        line_three = [
            self.grid_point.i(),
            self.grid_point.l()
        ]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)
        self.plotter.draw_path(line_three)

    def n(self):
        line_one = [
            self.grid_point.e(),
            self.grid_point.f(),
            self.grid_point.b()
        ]
        line_two = [
            self.grid_point.i(),
            self.grid_point.j(),
            self.grid_point.n()
        ]
        line_three = [
            self.grid_point.c(),
            self.grid_point.o()
        ]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)
        self.plotter.draw_path(line_three)

    def o(self):
        line_one = [
            self.grid_point.e(),
            self.grid_point.h()
        ]
        line_two = [
            self.grid_point.i(),
            self.grid_point.j(),
            self.grid_point.n()
        ]
        line_three = [
            self.grid_point.o(),
            self.grid_point.k(),
            self.grid_point.l()
        ]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)
        self.plotter.draw_path(line_three)

    def p(self):
        line_one = [
            self.grid_point.b(),
            self.grid_point.n()
        ]
        line_two = [
            self.grid_point.c(),
            self.grid_point.g(),
            self.grid_point.h()
        ]
        line_three = [
            self.grid_point.o(),
            self.grid_point.k(),
            self.grid_point.l()
        ]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)
        self.plotter.draw_path(line_three)

    def q(self):
        line_one = [self.grid_point.e(), self.grid_point.h()]
        line_two = [self.grid_point.i(), self.grid_point.l()]
        line_three = [self.grid_point.b(), self.grid_point.f()]
        line_four = [self.grid_point.c(), self.grid_point.g()]
        line_five = [self.grid_point.j(), self.grid_point.n()]
        line_six = [self.grid_point.k(), self.grid_point.o()]
        self.plotter.draw_path(line_one)
        self.plotter.draw_path(line_two)
        self.plotter.draw_path(line_three)
        self.plotter.draw_path(line_four)
        self.plotter.draw_path(line_five)
        self.plotter.draw_path(line_six)