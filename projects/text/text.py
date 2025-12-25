from utils.grid_points import GridPoints


class LetterPath:
    origin_x: float
    origin_y: float
    width: float
    height: float
    g: GridPoints

    def __init(self, origin_x: float, origin_y: float, height: float, width: float):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height
        self.grid = GridPoints(
            origin_x=origin_x, origin_y=origin_y, height=height, width=width
        )

    def a(self):
        path_one = [self.g.six(), self.g.one(), self.g.eight()]
        path_two = [self.g.three(), self.g.five()]
        return [path_one, path_two]

    def b(self):
        return [
            [
                self.g.zero(),
                self.g.two(),
                self.g.four(),
                self.g.eight(),
                self.g.six(),
                self.g.zero(),
            ]
        ]

    def c(self):
        return [[self.g.two(), self.g.zero(), self.g.six(), self.g.eight()]]

    def d(self):
        return [
            [self.g.zero(), self.g.five(), self.g.seven(), self.g.six(), self.g.zero()]
        ]

    def e(self):
        path_one = [self.g.zero(), self.g.two()]
        path_two = [self.g.three(), self.g.four()]
        path_three = [self.g.six(), self.g.eight()]
        path_four = [self.g.zero(), self.g.six()]
        return [path_one, path_two, path_three, path_four]

    def f(self):
        path_one = [self.g.zero(), self.g.two()]
        path_two = [self.g.three(), self.g.four()]
        path_three = [self.g.zero(), self.g.six()]
        return [path_one, path_two, path_three]

    def g(self):
        return [
            [
                self.g.two(),
                self.g.one(),
                self.g.six(),
                self.g.eight(),
                self.g.five(),
                self.g.four(),
            ]
        ]

    def h(self):
        path_one = [self.g.zero(), self.g.six()]
        path_two = [self.g.two(), self.g.eight()]
        path_three = [self.g.three(), self.g.five()]
        return [path_one, path_two, path_three]

    def i(self):
        path_one = [self.g.one(), self.g.seven()]
        path_two = [self.g.zero(), self.g.two()]
        path_three = [self.g.six(), self.g.eight()]
        return [path_one, path_two, path_three]

    def j(self):
        path_one = [self.g.one(), self.g.seven(), self.g.six()]
        path_two = [self.g.zero(), self.g.two()]
        return [path_one, path_two]

    def k(self):
        path_one = [self.g.zero(), self.g.six()]
        path_two = [self.g.three(), self.g.four(), self.g.two()]
        path_three = [self.g.four(), self.g.eight()]
        return [path_one, path_two, path_three]

    def l(self):
        return [[self.g.zero(), self.g.six(), self.g.eight()]]

    def m(self):
        return [
            [self.g.six(), self.g.zero(), self.g.seven(), self.g.two(), self.g.eight()]
        ]

    def n(self):
        return [[self.g.six(), self.g.zero(), self.g.eight(), self.g.two()]]

    def o(self):
        return [
            [self.g.zero(), self.g.two(), self.g.eight(), self.g.six(), self.g.zero()]
        ]

    def p(self):
        return [
            [self.g.six(), self.g.zero(), self.g.two(), self.g.five(), self.g.three()]
        ]

    def q(self):
        return [
            [
                self.g.eight(),
                self.g.six(),
                self.g.zero(),
                self.g.two(),
                self.g.eight(),
                self.g.four(),
            ]
        ]

    def r(self):
        path_one = [
            self.g.six(),
            self.g.zero(),
            self.g.two(),
            self.g.five(),
            self.g.three(),
        ]
        path_two = [self.g.four(), self.g.eight()]
        return [path_one, path_two]

    def s(self):
        return [
            [
                self.g.two(),
                self.g.zero(),
                self.g.three(),
                self.g.five(),
                self.g.eight(),
                self.g.six(),
            ]
        ]

    def t(self):
        path_one = [self.g.one(), self.g.seven()]
        path_two = [self.g.zero(), self.g.two()]
        return [path_one, path_two]

    def u(self):
        return [[self.g.zero(), self.g.six(), self.g.eight(), self.g.two()]]

    def v(self):
        return [[self.g.zero(), self.g.seven(), self.g.two()]]

    def w(self):
        return [
            [self.g.zero(), self.g.six(), self.g.four(), self.g.eight(), self.g.two()]
        ]

    def x(self):
        path_one = [self.g.zero(), self.g.eight()]
        path_two = [self.g.two(), self.g.six()]
        return [path_one, path_two]

    def y(self):
        path_one = [self.g.zero(), self.g.four(), self.g.two()]
        path_two = [self.g.four(), self.g.seven()]
        return [path_one, path_two]

    def z(self):
        return [[self.g.zero(), self.g.two(), self.g.six(), self.g.eight()]]
