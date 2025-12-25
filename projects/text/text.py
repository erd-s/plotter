from utils.plotter_interface import PlotterInterface
from projects.text.letter_path import LetterPath


class HorizontalText:
    plotter: PlotterInterface
    text: str
    origin_x: float
    origin_y: float
    width: float
    height: float
    _tracking: float
    _letter_width: float

    def __init__(
        self,
        plotter: PlotterInterface,
        text: str,
        origin_x: float,
        origin_y: float,
        width: float = None,
        height: float = None,
    ):
        self.plotter = plotter
        self.text = text
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width if width else len(text) * 0.25

        self._tracking = (self.width / (len(text))) / 5
        self._letter_width = (
            self.width - ((len(self.text) - 1) * self._tracking)
        ) / len(text)
        self.height = height if height else self._letter_width

    def draw_text(self):
        x_adjustment_multiplier = self._letter_width + self._tracking
        for i, letter in enumerate(self.text):
            if letter == " ":
                continue
            origin_x_adjusted = self.origin_x + (x_adjustment_multiplier * i)
            letter_path = LetterPath(
                letter=letter,
                origin_x=origin_x_adjusted,
                origin_y=self.origin_y,
                height=self.height,
                width=self._letter_width,
            )
            paths = letter_path.letter_path()
            for path in paths:
                self.plotter.draw_path(path)


class VerticalText:
    plotter: PlotterInterface
    text: str
    origin_x: float
    origin_y: float
    width: float
    height: float
    _tracking: float
    _letter_height: float

    def __init__(
        self,
        plotter: PlotterInterface,
        text: str,
        origin_x: float,
        origin_y: float,
        width: float = None,
        height: float = None,
    ):
        self.plotter = plotter
        self.text = text
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.height = height if height else len(text) * 0.25
        self._tracking = (self.height / (len(text))) / 5
        self._letter_height = (
            self.height - ((len(self.text) - 1) * self._tracking)
        ) / len(text)
        self.width = width if width else self._letter_height

    def draw_text(self):
        y_adjustment_multiplier = self._letter_height + self._tracking
        for i, letter in enumerate(self.text):
            if letter == " ":
                continue
            origin_y_adjusted = self.origin_y + (y_adjustment_multiplier * i)
            letter_path = LetterPath(
                letter=letter,
                origin_x=self.origin_x,
                origin_y=origin_y_adjusted,
                height=self._letter_height,
                width=self.width,
            )
            paths = letter_path.letter_path()
            for path in paths:
                self.plotter.draw_path(path)
