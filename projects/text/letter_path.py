from utils.grid_points import GridPoints


class LetterPath:
    letter: str
    origin_x: float
    origin_y: float
    width: float
    height: float
    _grid: GridPoints

    def __init__(
        self, letter: str, origin_x: float, origin_y: float, height: float, width: float
    ):
        self.letter = letter
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height
        self._grid = GridPoints(
            origin_x=origin_x, origin_y=origin_y, height=height, width=width
        )

    def letter_path(self):
        if self.letter == "a":
            return self._a()
        elif self.letter == "b":
            return self._b()
        elif self.letter == "c":
            return self._c()
        elif self.letter == "d":
            return self._d()
        elif self.letter == "e":
            return self._e()
        elif self.letter == "f":
            return self._f()
        elif self.letter == "g":
            return self._g()
        elif self.letter == "h":
            return self._h()
        elif self.letter == "i":
            return self._i()
        elif self.letter == "j":
            return self._j()
        elif self.letter == "k":
            return self._k()
        elif self.letter == "l":
            return self._l()
        elif self.letter == "m":
            return self._m()
        elif self.letter == "n":
            return self._n()
        elif self.letter == "o":
            return self._o()
        elif self.letter == "p":
            return self._p()
        elif self.letter == "q":
            return self._q()
        elif self.letter == "r":
            return self._r()
        elif self.letter == "s":
            return self._s()
        elif self.letter == "t":
            return self._t()
        elif self.letter == "u":
            return self._u()
        elif self.letter == "v":
            return self._v()
        elif self.letter == "w":
            return self._w()
        elif self.letter == "x":
            return self._x()
        elif self.letter == "y":
            return self._y()
        elif self.letter == "z":
            return self._z()

    def _a(self):
        path_one = [self._grid.six(), self._grid.one(), self._grid.eight()]
        path_two = [self._grid.three(), self._grid.five()]
        return [path_one, path_two]

    def _b(self):
        return [
            [
                self._grid.zero(),
                self._grid.two(),
                self._grid.four(),
                self._grid.eight(),
                self._grid.six(),
                self._grid.zero(),
            ]
        ]

    def _c(self):
        return [
            [self._grid.two(), self._grid.zero(), self._grid.six(), self._grid.eight()]
        ]

    def _d(self):
        return [
            [
                self._grid.zero(),
                self._grid.five(),
                self._grid.seven(),
                self._grid.six(),
                self._grid.zero(),
            ]
        ]

    def _e(self):
        path_one = [self._grid.zero(), self._grid.two()]
        path_two = [self._grid.three(), self._grid.four()]
        path_three = [self._grid.six(), self._grid.eight()]
        path_four = [self._grid.zero(), self._grid.six()]
        return [path_one, path_two, path_three, path_four]

    def _f(self):
        path_one = [self._grid.zero(), self._grid.two()]
        path_two = [self._grid.three(), self._grid.four()]
        path_three = [self._grid.zero(), self._grid.six()]
        return [path_one, path_two, path_three]

    def _g(self):
        return [
            [
                self._grid.two(),
                self._grid.zero(),
                self._grid.six(),
                self._grid.eight(),
                self._grid.five(),
                self._grid.four(),
            ]
        ]

    def _h(self):
        path_one = [self._grid.zero(), self._grid.six()]
        path_two = [self._grid.two(), self._grid.eight()]
        path_three = [self._grid.three(), self._grid.five()]
        return [path_one, path_two, path_three]

    def _i(self):
        path_one = [self._grid.one(), self._grid.seven()]
        path_two = [self._grid.zero(), self._grid.two()]
        path_three = [self._grid.six(), self._grid.eight()]
        return [path_one, path_two, path_three]

    def _j(self):
        path_one = [self._grid.one(), self._grid.seven(), self._grid.six()]
        path_two = [self._grid.zero(), self._grid.two()]
        return [path_one, path_two]

    def _k(self):
        path_one = [self._grid.zero(), self._grid.six()]
        path_two = [self._grid.three(), self._grid.four(), self._grid.two()]
        path_three = [self._grid.four(), self._grid.eight()]
        return [path_one, path_two, path_three]

    def _l(self):
        return [[self._grid.zero(), self._grid.six(), self._grid.eight()]]

    def _m(self):
        return [
            [
                self._grid.six(),
                self._grid.zero(),
                self._grid.seven(),
                self._grid.two(),
                self._grid.eight(),
            ]
        ]

    def _n(self):
        return [
            [self._grid.six(), self._grid.zero(), self._grid.eight(), self._grid.two()]
        ]

    def _o(self):
        return [
            [
                self._grid.zero(),
                self._grid.two(),
                self._grid.eight(),
                self._grid.six(),
                self._grid.zero(),
            ]
        ]

    def _p(self):
        return [
            [
                self._grid.six(),
                self._grid.zero(),
                self._grid.two(),
                self._grid.five(),
                self._grid.three(),
            ]
        ]

    def _q(self):
        return [
            [
                self._grid.eight(),
                self._grid.six(),
                self._grid.zero(),
                self._grid.two(),
                self._grid.eight(),
                self._grid.four(),
            ]
        ]

    def _r(self):
        path_one = [
            self._grid.six(),
            self._grid.zero(),
            self._grid.two(),
            self._grid.five(),
            self._grid.three(),
        ]
        path_two = [self._grid.four(), self._grid.eight()]
        return [path_one, path_two]

    def _s(self):
        return [
            [
                self._grid.two(),
                self._grid.zero(),
                self._grid.three(),
                self._grid.five(),
                self._grid.eight(),
                self._grid.six(),
            ]
        ]

    def _t(self):
        path_one = [self._grid.one(), self._grid.seven()]
        path_two = [self._grid.zero(), self._grid.two()]
        return [path_one, path_two]

    def _u(self):
        return [
            [self._grid.zero(), self._grid.six(), self._grid.eight(), self._grid.two()]
        ]

    def _v(self):
        return [[self._grid.zero(), self._grid.seven(), self._grid.two()]]

    def _w(self):
        return [
            [
                self._grid.zero(),
                self._grid.six(),
                self._grid.four(),
                self._grid.eight(),
                self._grid.two(),
            ]
        ]

    def _x(self):
        path_one = [self._grid.zero(), self._grid.eight()]
        path_two = [self._grid.two(), self._grid.six()]
        return [path_one, path_two]

    def _y(self):
        path_one = [self._grid.zero(), self._grid.four(), self._grid.two()]
        path_two = [self._grid.four(), self._grid.seven()]
        return [path_one, path_two]

    def _z(self):
        return [
            [self._grid.zero(), self._grid.two(), self._grid.six(), self._grid.eight()]
        ]
