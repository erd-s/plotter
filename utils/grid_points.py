class GridPoints:
    origin_x: float
    origin_y: float
    width: float
    height: float
    center_x: float
    center_y: float
    _horizontal_space: float
    _vertical_space: float

    def __init__(
        self,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        center_x_offset: float = 0,
        center_y_offset: float = 0,
    ):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height
        self.center_x = self.origin_x + (self.width / 2) + center_x_offset
        self.center_y = self.origin_y + (self.height / 2) + center_y_offset

    def zero(self):
        x = self.origin_x
        y = self.origin_y
        return [x, y]

    def one(self):
        x = self.center_x
        y = self.origin_y
        return [x, y]

    def two(self):
        x = self.origin_x + self.width
        y = self.origin_y
        return [x, y]

    def three(self):
        x = self.origin_x
        y = self.center_y
        return [x, y]

    def four(self):
        x = self.center_x
        y = self.center_y
        return [x, y]

    def five(self):
        x = self.origin_x + self.width
        y = self.center_y
        return [x, y]

    def six(self):
        x = self.origin_x
        y = self.origin_y + self.height
        return [x, y]

    def seven(self):
        x = self.center_x
        y = self.origin_y + self.height
        return [x, y]

    def eight(self):
        x = self.origin_x + self.width
        y = self.origin_y + self.height
        return [x, y]
