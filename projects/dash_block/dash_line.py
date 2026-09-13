from utils.plotter_interface import PlotterInterface


class DashLine:
    plotter: PlotterInterface
    origin_x: float
    origin_y: float
    length: float
    vertical_orientation: bool

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

    def draw_variant_a(self):
        spacing = self.length / 10
        number_of_dashes = 3
        number_of_spaces = number_of_dashes - 1
        total_length_minus_spacing = self.length - (spacing * number_of_spaces)
        dash_length = total_length_minus_spacing / number_of_dashes

        for i in range(3):
            dash_origin_y = self.origin_y + ((dash_length + spacing) * i)
            dash_end_y = dash_origin_y + dash_length
            point_a = [self.origin_x, dash_origin_y]
            point_b = [self.origin_x, dash_end_y]
            self.plotter.draw_path([point_a, point_b])

    def draw_variant_b(self):
        spacing = self.length / 10
        number_of_spaces = 4
        total_length_minus_spacing = self.length - (spacing * number_of_spaces)
        short_dash_length = spacing / 1.5
        big_dash_length = (total_length_minus_spacing - (short_dash_length * 3)) / 2

        self.plotter.moveto(self.origin_x, self.origin_y)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, spacing)
        self.plotter.line(0, big_dash_length)
        self.plotter.move(0, spacing)
        self.plotter.line(0, short_dash_length)
        self.plotter.move(0, spacing)
        self.plotter.line(0, big_dash_length)
        self.plotter.move(0, spacing)
        self.plotter.line(0, short_dash_length)

    def draw_variant_c(self):
        pass

    def draw_variant_d(self):
        pass

    def draw_variant_e(self):
        pass

    def draw_variant_f(self):
        pass

    def draw_variant_g(self):
        pass

    def draw_variant_h(self):
        pass

    def draw_variant_i(self):
        pass

    def draw_variant_j(self):
        pass

    def draw_variant_k(self):
        pass
