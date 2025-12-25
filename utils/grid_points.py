class GridPoints:
    origin_x: float
    origin_y: float
    width: float
    height: float
    _horizontal_space: float
    _vertical_space: float

    def __init__(self, origin_x: float, origin_y: float, width: float, height: float):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height
        self._horizontal_space = width / 3
        self._vertical_space = height / 3

    def zero(self):
        x = self.origin_x
        y = self.origin_y
        return [x, y]

    def one(self):
        x = self.origin_x + self._horizontal_space
        y = self.origin_y
        return [x, y]

    def two(self):
        x = self.origin_x + (self._horizontal_space * 2)
        y = self.origin_y
        return [x, y]

    def three(self):
        x = self.origin_x
        y = self.origin_y + (self._vertical_space * 2)
        return [x, y]

    def four(self):
        x = self.origin_x + self._horizontal_space
        y = self.origin_y + (self._vertical_space * 2)
        return [x, y]

    def five(self):
        x = self.origin_x + (self._horizontal_space * 2)
        y = self.origin_y + (self._vertical_space * 2)
        return [x, y]

    def six(self):
        x = self.origin_x
        y = self.origin_y + (self._vertical_space * 3)
        return [x, y]

    def seven(self):
        x = self.origin_x + self._horizontal_space
        y = self.origin_y + (self._vertical_space * 3)
        return [x, y]

    def eight(self):
        x = self.origin_x + (self._horizontal_space * 2)
        y = self.origin_y + (self._vertical_space * 3)
        return [x, y]
