from utils.plotter_interface import PlotterInterface
from projects.grid import draw_grid_v3


class ObjectGridV2:
    square_center_x: float
    square_center_y: float
    square_width: float
    square_height: float
    square_start_x: float
    square_end_x: float
    square_start_y: float
    square_end_y: float
    grid_size_horizontal: int
    grid_size_vertical: int
    origin_x: float
    origin_y: float
    width: float
    height: float
    inset: float
    current_index: int = 0
    current_row: int = 0
    current_column: int = 0
    draw_grid_lines: bool

    def __init__(
        self,
        grid_size_horizontal: int,
        grid_size_vertical: int,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        margin: float = 0,
        inset: float = 0,
        draw_grid_lines: bool = False,
    ):
        self.grid_size_horizontal = grid_size_horizontal
        self.grid_size_vertical = grid_size_vertical
        self.origin_x = origin_x + margin
        self.origin_y = origin_y + margin
        self.width = width - (margin * 2)
        self.height = height - (margin * 2)
        self.inset = inset
        self.draw_grid_lines = draw_grid_lines

    def draw_object_grid(
        self, plotter: PlotterInterface, start_index=0, iterations: int = None
    ):
        self.square_width = (self.width / self.grid_size_horizontal) - (self.inset * 2)
        self.square_height = (self.height / self.grid_size_vertical) - (self.inset * 2)

        print(f'Grid Square Width = {self.square_width}"')
        print(f'Grid Square Height = {self.square_height}"')

        if self.draw_grid_lines:
            draw_grid_v3(
                plotter=plotter,
                grid_size_horizontal=self.grid_size_horizontal,
                grid_size_vertical=self.grid_size_vertical,
                origin_x=self.origin_x,
                origin_y=self.origin_y,
                height=self.height,
                width=self.width,
            )

        plotter.move(
            self.origin_x + (self.square_width / 2) + (self.current_row * self.inset),
            self.origin_y
            + (self.square_height / 2)
            + (self.current_column * self.inset),
        )

        iteration = 0

        for i in range(self.grid_size_horizontal * self.grid_size_vertical):
            self.current_index = i
            self.square_center_x = (
                self.origin_x
                + (self.square_width / 2)
                + (self.current_column * self.square_width)
                + ((self.current_column + 1) * (self.inset * 2))
                - self.inset
            )
            self.square_center_y = (
                self.origin_y
                + (self.square_height / 2)
                + (self.current_row * self.square_height)
                + ((self.current_row + 1) * (self.inset * 2))
                - self.inset
            )
            self.square_start_x = self.square_center_x - (self.square_width * 0.5)
            self.square_end_x = self.square_center_x + (self.square_width * 0.5)
            self.square_start_y = self.square_center_y - (self.square_height * 0.5)
            self.square_end_y = self.square_center_y + (self.square_height * 0.5)

            if i >= start_index:
                self.object_logic(plotter=plotter)
                iteration += 1
            if iterations == iteration:
                return

            if (i + 1) % self.grid_size_horizontal == 0:
                # move left and down
                self.current_row += 1
                self.current_column = 0
                plotter.moveto(
                    self.origin_x + (self.square_width / 2),
                    self.origin_y
                    + (self.current_row * self.square_height)
                    - (self.square_height / 2)
                    + (self.current_row * self.inset),
                )
            else:
                # move right
                self.current_column += 1

    def object_logic(self, plotter: PlotterInterface):
        # override with object logic
        return
