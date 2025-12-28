from utils.plotter_interface import PlotterInterface


class ObjectGridV2:
    square_center_x: float
    square_center_y: float
    square_width: float
    square_height: float
    square_start_x: float
    square_end_x: float
    square_start_y: float
    square_end_y: float
    inset: float = 0
    grid_size_horizontal: int
    grid_size_vertical: int
    origin_x: float
    origin_y: float
    width: float
    height: float

    def __init__(
        self,
        grid_size_horizontal: int,
        grid_size_vertical: int,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        inset: float = 0,
    ):
        self.grid_size_horizontal = grid_size_horizontal
        self.grid_size_vertical = grid_size_vertical
        self.origin_x = origin_x + inset
        self.origin_y = origin_y + inset
        self.width = width - inset * 2
        self.height = height - inset * 2
        self.inset = inset

    def create_object_grid(
        self, plotter: PlotterInterface, start_index=0, iterations: int = None
    ):
        self.square_width = self.width / self.grid_size_horizontal
        self.square_height = self.height / self.grid_size_vertical

        print(f'Grid Square Width = {self.square_width}"')
        print(f'Grid Square Height = {self.square_height}"')

        plotter.move(
            self.origin_x + (self.square_width / 2),
            self.origin_y + (self.square_height / 2),
        )

        iteration = 0
        row = 0
        column = 0
        for i in range(self.grid_size_horizontal * self.grid_size_vertical):
            self.square_center_x = (
                self.origin_x + (self.square_width / 2) + (column * self.square_width)
            )
            self.square_center_y = (
                self.origin_y + (self.square_height / 2) + (row * self.square_height)
            )
            self.square_start_x = self.square_center_x - (self.square_width * 0.5)
            self.square_end_x = self.square_center_x + (self.square_width * 0.5)
            self.square_start_y = self.square_center_y - (self.square_height * 0.5)
            self.square_end_y = self.square_center_y + (self.square_height * 0.5)

            plotter.override_bounds(
                x_min=self.square_start_x,
                x_max=self.square_end_x,
                y_min=self.square_start_y,
                y_max=self.square_end_y,
            )

            next_square_center_x = self.square_center_x + self.square_width

            if i >= start_index:
                self.object_logic(plotter=plotter)
                iteration += 1
            if iterations == iteration:
                return

            if (i + 1) % self.grid_size_horizontal == 0:
                # move left and down
                row += 1
                column = 0
                plotter.moveto(
                    self.origin_x + (self.square_width / 2),
                    self.origin_y
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
