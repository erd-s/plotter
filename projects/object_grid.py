from nextdraw import NextDraw

from utils.positioning import (
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

    def __init__(self):
        pass

    def create_object_grid(
        self,
        plotter: NextDraw,
        grid_size: int,
        start_index=0,
        iterations: int = None,
    ):
        self.square_width = effective_width() / grid_size
        self.square_height = effective_height() / grid_size

        print(f'Square Width = {self.square_width}"')
        print(f'Square Height = {self.square_height}"')

        plotter.move(
            effective_x_start() + (self.square_width / 2),
            effective_y_start() + (self.square_height / 2),
        )

        iteration = 0
        for i in range(grid_size * grid_size):
            print(f"Index: {i}")
            self.square_center_x = plotter.current_pos()[0]
            self.square_center_y = plotter.current_pos()[1]

            if i >= start_index:
                self.object_logic(plotter=plotter)
                iteration += 1
            if iterations == iteration:
                return

            plotter.moveto(self.square_center_x, self.square_center_y)

            if (i + 1) % grid_size == 0:
                # move left and down
                plotter.move(self.square_width * -(grid_size - 1), self.square_height)
            else:
                # move right
                plotter.move(self.square_width, 0)

    def object_logic(self, plotter: NextDraw):
        # override with object logic
        return
