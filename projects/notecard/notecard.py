from utils.plotter_interface import PlotterInterface
from projects.text.text import HorizontalText
from utils.transform import centered_paths
from projects.rectangles.rectangle import draw_rectangle


class NoteCard:
    origin_x: float
    origin_y: float
    width: float
    height: float
    padding: float
    number_of_cards: int
    current_column = 0
    current_row = 0

    def __init__(
        self,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        padding: float,
        number_of_cards: int = 4,
    ):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height
        self.padding = padding
        self.number_of_cards = number_of_cards

    def draw_notecard(self, plotter: PlotterInterface, title: str):
        card_width = self.width / (self.number_of_cards / 2)
        card_height = self.height / (self.number_of_cards / 2)
        shape_width = card_width / 20

        for c in range(self.number_of_cards):
            left_origin_x = (
                self.origin_x
                + (self.padding * 1.5)
                + (self.current_column * card_width)
            )
            right_origin_x = (
                self.origin_x
                + card_width
                - (self.padding * 1.5)
                + (self.current_column * card_width)
                - shape_width
            )
            top_origin_y = (
                self.origin_y + (self.padding * 1.5) + (self.current_row * card_height)
            )
            bottom_origin_y = (
                self.origin_y
                + card_height
                + (self.current_row * card_height)
                - shape_width
                - (self.padding * 1.5)
            )

            # top left
            self.object_logic(
                plotter=plotter,
                origin_x=left_origin_x,
                origin_y=top_origin_y,
                width=shape_width,
                height=shape_width,
            )

            # top right
            self.object_logic(
                plotter=plotter,
                origin_x=right_origin_x,
                origin_y=top_origin_y,
                width=shape_width,
                height=shape_width,
                invert=True,
            )

            # bottom left
            self.object_logic(
                plotter=plotter,
                origin_x=left_origin_x,
                origin_y=bottom_origin_y,
                width=shape_width,
                height=shape_width,
            )

            # bottom right
            self.object_logic(
                plotter=plotter,
                origin_x=right_origin_x,
                origin_y=bottom_origin_y,
                width=shape_width,
                height=shape_width,
                invert=True,
            )

            # title
            text_height = 0.1
            text_width = len(title) * 0.15
            text = HorizontalText(
                plotter=plotter,
                text=title,
                origin_x=0,
                origin_y=0,
                width=text_width,
                height=text_height,
            )
            text_paths = text.text_paths()
            card_center_x = (
                self.origin_x + (self.current_column * card_width) + card_width / 2
            )
            centered_text_paths = centered_paths(
                text_paths,
                around_x=card_center_x,
                around_y=top_origin_y + (text_height / 2) + self.padding / 2,
            )
            for path in centered_text_paths:
                plotter.draw_path(path)

            draw_rectangle(
                plotter=plotter,
                height=card_height - self.padding,
                width=card_width - self.padding,
                center_x=self.origin_x
                + (card_width * self.current_column)
                + card_width / 2,
                center_y=self.origin_y
                + (card_height * self.current_row)
                + card_height / 2,
            )

            self.current_column += 1

            # end of row 1, shift down
            if self.current_column == (self.number_of_cards / 2):
                self.current_column = 0
                self.current_row = 1

    def object_logic(
        self,
        plotter: PlotterInterface,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        invert: bool = False,
    ):
        # override with object logic
        pass
