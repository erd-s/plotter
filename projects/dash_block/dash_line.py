from utils.plotter_interface import PlotterInterface


class DashLine:
    plotter: PlotterInterface
    origin_x: float
    origin_y: float
    length: float
    vertical_orientation: bool
    spacing: float

    def __init__(
        self,
        plotter: PlotterInterface,
        origin_x: float,
        origin_y: float,
        length: float,
        vertical_orientation: bool,
    ):
        self.plotter = plotter
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.length = length
        self.vertical_orientation = vertical_orientation
        self.spacing = length / 12

    def draw_variant_a(self):
        number_of_dashes = 3
        number_of_spaces = number_of_dashes - 1
        total_length_minus_spacing = self.length - (self.spacing * number_of_spaces)
        dash_length = total_length_minus_spacing / number_of_dashes

        for i in range(number_of_dashes):
            dash_origin_y = self.origin_y + ((dash_length + self.spacing) * i)
            dash_end_y = dash_origin_y + dash_length
            point_a = [self.origin_x, dash_origin_y]
            point_b = [self.origin_x, dash_end_y]
            self.plotter.draw_path([point_a, point_b])

    def draw_variant_b(self):

        number_of_spaces = 4
        total_length_minus_spacing = self.length - (self.spacing * number_of_spaces)
        short_dash_length = self.spacing / 1.5
        big_dash_length = (total_length_minus_spacing - (short_dash_length * 3)) / 2

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, big_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, big_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)

    def draw_variant_c(self):

        short_dash_length = self.length / 6
        long_dash_length = self.length - self.spacing - short_dash_length

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, long_dash_length)

    def draw_variant_d(self):

        short_dash_length = self.length / 6
        long_dash_length = self.length - self.spacing - short_dash_length

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, long_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)

    def draw_variant_e(self):

        number_of_spaces = 4
        total_length_minus_spacing = self.length - (self.spacing * number_of_spaces)
        short_dash_length = self.spacing / 1.5
        big_dash_length = (total_length_minus_spacing - (short_dash_length * 3)) / 2

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, big_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, big_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)

    def draw_variant_f(self):

        number_of_dashes = 4
        number_of_spaces = number_of_dashes - 1
        total_length_minus_spacing = self.length - (self.spacing * number_of_spaces)
        dash_length = total_length_minus_spacing / number_of_dashes

        for i in range(number_of_dashes):
            dash_origin_y = self.origin_y + ((dash_length + self.spacing) * i)
            dash_end_y = dash_origin_y + dash_length
            point_a = [self.origin_x, dash_origin_y]
            point_b = [self.origin_x, dash_end_y]
            self.plotter.draw_path([point_a, point_b])

    def draw_variant_g(self):

        short_dash_length = self.spacing / 2
        long_dash_length = self.length - (self.spacing * 2) - (short_dash_length * 2)

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, long_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)

    def draw_variant_h(self):

        short_dash_length = self.spacing / 2
        long_dash_length = (self.length - (self.spacing * 2) - (short_dash_length)) / 2

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, long_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, long_dash_length)

    def draw_variant_i(self):

        number_of_spaces = 4
        total_length_minus_spacing = self.length - (self.spacing * number_of_spaces)
        short_dash_length = self.spacing / 1.5
        big_dash_length = (total_length_minus_spacing - (short_dash_length * 3)) / 2

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, big_dash_length)
        self.plotter.move(0, self.spacing)
        self.plotter.line(0, big_dash_length)

    def draw_variant_j(self):

        number_of_dashes = 6
        number_of_spaces = number_of_dashes - 1
        total_length_minus_spacing = self.length - (self.spacing * number_of_spaces)
        dash_length = total_length_minus_spacing / number_of_dashes

        for i in range(number_of_dashes):
            dash_origin_y = self.origin_y + ((dash_length + self.spacing) * i)
            dash_end_y = dash_origin_y + dash_length
            point_a = [self.origin_x, dash_origin_y]
            point_b = [self.origin_x, dash_end_y]
            self.plotter.draw_path([point_a, point_b])

    def draw_variant_k(self):

        number_of_dashes = 7
        number_of_spaces = number_of_dashes - 1
        total_length_minus_spacing = self.length - (self.spacing * number_of_spaces)
        dash_length = total_length_minus_spacing / number_of_dashes

        for i in range(number_of_dashes):
            dash_origin_y = self.origin_y + ((dash_length + self.spacing) * i)
            dash_end_y = dash_origin_y + dash_length
            point_a = [self.origin_x, dash_origin_y]
            point_b = [self.origin_x, dash_end_y]
            self.plotter.draw_path([point_a, point_b])

    def draw_variant_l(self):
        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, self.length)
