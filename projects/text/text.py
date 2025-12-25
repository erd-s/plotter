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
    _character_width: float

    def __init__(
        self,
        plotter: PlotterInterface,
        text: str,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        tracking: float = 0.02,
    ):
        self.plotter = plotter
        self.text = text
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height
        self._tracking = tracking
        self._character_width = width / (
            float(len(text) + 2) + float(len(text) - 1) * tracking
        )

    def write_text(self):
        for i, letter in enumerate(self.text):
            origin_x_adjusted = (
                self.origin_x
                + (self._character_width * i)
                + (self._tracking * i)
                + self._character_width
            )
            letter_path = LetterPath(
                letter=letter,
                origin_x=origin_x_adjusted,
                origin_y=self.origin_y,
                height=self.height,
                width=self._character_width,
            )
            paths = letter_path.letter_path()
            for path in paths:
                self.plotter.draw_path(path)
