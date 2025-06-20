from utils.plotter_interface import PlotterInterface

from utils.utils import (
    effective_width,
    effective_height,
    effective_x_start,
    effective_y_start,
)


class ObjectGrid:
    square_center_x: float
    square_center_y: float
    square_width: float
    square_height: float
    margin: float = 0
    grid_size: int

    def __init__(self, grid_size: int):
        self.grid_size = grid_size

    def create_object_grid(
        self, plotter: PlotterInterface, start_index=0, iterations: int = None
    ):
        self.square_width = effective_width() / self.grid_size
        self.square_height = effective_height() / self.grid_size

        print(f'Grid Square Width = {self.square_width}"')
        print(f'Grid Square Height = {self.square_height}"')

        plotter.move(
            effective_x_start() + (self.square_width / 2),
            effective_y_start() + (self.square_height / 2),
        )

        iteration = 0
        row = 0
        column = 0
        for i in range(self.grid_size * self.grid_size):
            self.square_center_x = (
                effective_x_start()
                + (self.square_width / 2)
                + (column * self.square_width)
            )
            self.square_center_y = (
                effective_y_start()
                + (self.square_height / 2)
                + (row * self.square_height)
            )
            next_square_center_x = self.square_center_x + self.square_width

            if i >= start_index:
                self.object_logic(plotter=plotter)
                iteration += 1
            if iterations == iteration:
                return

            if (i + 1) % self.grid_size == 0:
                # move left and down
                row += 1
                column = 0
                plotter.moveto(
                    effective_x_start() + (self.square_width / 2),
                    effective_y_start()
                    + (row * self.square_height)
                    - (self.square_height / 2),
                )
            else:
                # move right
                column += 1
                plotter.moveto(next_square_center_x, self.square_center_y)

    def object_logic(self, plotter: PlotterInterface):
        # override with object logic
        return
