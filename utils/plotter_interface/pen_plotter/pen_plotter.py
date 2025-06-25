from nextdraw import NextDraw
from utils.plotter_interface.PlotterInterface import PlotterInterface


class PenPlotter(PlotterInterface):
    plotter: NextDraw

    def __init__(
        self,
        plotter: NextDraw,
        clip_to_bounds: bool,
        x_min: float,
        x_max: float,
        y_min: float,
        y_max: float,
    ):
        super().__init__(
            clip_to_bounds=clip_to_bounds,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
        )
        self.plotter = plotter

    def disconnect(self):
        self.plotter.disconnect()

    def goto(self, x_target, y_target):
        if self.clip_to_bounds:
            x = x_target
            if x < self.x_min:
                x = self.x_min
            elif x > self.x_max:
                x = self.x_max

            y = y_target
            if y < self.y_min:
                y = self.y_min
            elif y > self.y_max:
                y = self.y_max

            self.plotter.goto(x, y)
        else:
            self.plotter.goto(x_target, y_target)

    def go(self, x_delta, y_delta):
        if self.clip_to_bounds:
            x = self.current_pos()[0] + x_delta
            x_dist = x_delta
            y_dist = y_delta
            if x < self.x_min:
                x = self.x_min
                x_dist = x - self.current_pos()[0]
            elif x > self.x_max:
                x = self.x_max
                x_dist = self.current_pos()[0] - x

            y = self.current_pos()[1] + y_delta
            if y < self.y_min:
                y = self.y_min
                y_dist = y - self.current_pos()[1]
            elif y > self.y_max:
                y = self.y_max
                y_dist = self.current_pos()[1] - y

            self.plotter.go(x_dist, y_dist)
        else:
            self.plotter.go(x_delta, y_delta)

    def lineto(self, x_target, y_target):
        if self.clip_to_bounds:
            x = x_target
            if x < self.x_min:
                x = self.x_min
            elif x > self.x_max:
                x = self.x_max

            y = y_target
            if y < self.y_min:
                y = self.y_min
            elif y > self.y_max:
                y = self.y_max

            self.plotter.lineto(x, y)
        else:
            self.plotter.lineto(x_target, y_target)

    def line(self, x_delta, y_delta):
        if self.clip_to_bounds:
            x = self.current_pos()[0] + x_delta
            x_dist = x_delta
            y_dist = y_delta
            if x < self.x_min:
                x = self.x_min
                x_dist = x - self.current_pos()[0]
            elif x > self.x_max:
                x = self.x_max
                x_dist = self.current_pos()[0] - x

            y = self.current_pos()[1] + y_delta
            if y < self.y_min:
                y = self.y_min
                y_dist = y - self.current_pos()[1]
            elif y > self.y_max:
                y = self.y_max
                y_dist = self.current_pos()[1] - y

            self.plotter.line(x_dist, y_dist)
        else:
            self.plotter.line(x_delta, y_delta)

    def moveto(self, x_target, y_target):
        if self.clip_to_bounds:
            x = x_target
            if x < self.x_min:
                x = self.x_min
            elif x > self.x_max:
                x = self.x_max

            y = y_target
            if y < self.y_min:
                y = self.y_min
            elif y > self.y_max:
                y = self.y_max

            self.plotter.moveto(x, y)
        else:
            self.plotter.moveto(x_target, y_target)

    def move(self, x_delta, y_delta):
        if self.clip_to_bounds:
            x = self.current_pos()[0] + x_delta
            x_dist = x_delta
            y_dist = y_delta
            if x < self.x_min:
                x = self.x_min
                x_dist = x - self.current_pos()[0]
            elif x > self.x_max:
                x = self.x_max
                x_dist = self.current_pos()[0] - x

            y = self.current_pos()[1] + y_delta
            if y < self.y_min:
                y = self.y_min
                y_dist = y - self.current_pos()[1]
            elif y > self.y_max:
                y = self.y_max
                y_dist = self.current_pos()[1] - y
            self.plotter.move(x_dist, y_dist)
        else:
            self.plotter.move(x_delta, y_delta)

    def draw_path(self, vertex_list):
        if self.clip_to_bounds:
            path_to_draw = []
            for i, point in enumerate(vertex_list):
                x, y = point[0], point[1]
                if self.x_min < x < self.x_max and self.y_min < y < self.y_max:
                    # both in bounds
                    path_to_draw.append([x, y])
                elif len(path_to_draw) > 1:
                    self.plotter.draw_path([path_to_draw])
                    self.draw_path(vertex_list[i:])
        else:
            self.plotter.draw_path(vertex_list)

    def turtle_pos(self):
        self.plotter.turtle_pos()

    def current_pos(self) -> dict:
        return self.plotter.current_pos()

    def update(self):
        self.plotter.update()

    def usb_query(self, query):
        self.plotter.usb_query(query)

    def usb_command(self, command):
        self.plotter.usb_command(command)

    def penup(self):
        self.plotter.penup()

    def pendown(self):
        self.plotter.pendown()

    def block(self):
        self.plotter.block()

    def delay(self, time_ms):
        self.plotter.delay(time_ms)

    def current_pen(self) -> bool:
        return self.plotter.current_pen()

    def turtle_pen(self) -> bool:
        return self.plotter.turtle_pen()

    def interactive(self):
        self.plotter.interactive()

    def connect(self) -> bool:
        return self.plotter.connect()

    def load_config(self, config_ref):
        return self.plotter.load_config(config_ref)
