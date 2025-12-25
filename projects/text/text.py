from utils.plotter_interface import PlotterInterface
from projects.text.letter_path import LetterPath


class Text:
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
        width: float,
        height: float = None,
        tracking: float = 0.1,
    ):
        self.plotter = plotter
        self.text = text
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width

        self._tracking = tracking
        self._letter_width = (
            self.width - ((len(self.text) - 1) * self._tracking)
        ) / len(text)
        self.height = height if height else self._letter_width

    def write_text(self):
        x_adjustment_multiplier = self._letter_width + self._tracking
        for i, letter in enumerate(self.text):
            if letter == " ":
                continue
            origin_x_adjusted = (
                self.origin_x + (x_adjustment_multiplier * i) + self._tracking
            )
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
