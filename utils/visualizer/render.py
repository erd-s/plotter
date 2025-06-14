import matplotlib.pyplot as plt
from nextdraw import NextDraw


class VisualizedPlotter(NextDraw):
    current_x: float = 0
    current_y: float = 0
    path = []

    def disconnect(self):
        x_list = [x[0] for x in self.path]
        y_list = [y[1] for y in self.path]
        plt.show(x_list, y_list)

    def goto(self, x_target, y_target):
        self.current_x = x_target
        self.current_y = y_target

    def go(self, x_delta, y_delta):
        self.current_x += x_delta
        self.current_y += y_delta

    def lineto(self, x_target, y_target):
        self.path.append([x_target, y_target])
        self.current_x += x_target
        self.current_y += y_target

    def line(self, x_delta, y_delta):
        self.path.append([self.current_x + x_delta, self.current_y + y_delta])
        self.current_x += x_delta
        self.current_y += y_delta

    def moveto(self, x_target, y_target):
        self.current_x = x_target
        self.current_y = y_target

    def move(self, x_delta, y_delta):
        self.current_x += x_delta
        self.current_y += y_delta

    def draw_path(self, vertex_list):
        for path in vertex_list:
            self.path.append(path)

        last_point = vertex_list[-1]
        self.current_x = last_point[0]
        self.current_y = last_point[1]

    def turtle_pos(self):
        return self.current_pos()

    def current_pos(self):
        return [self.current_x, self.current_y]

    def update(self):
        pass

    def usb_query(self, query):
        pass

    def usb_command(self, command):
        pass

    def penup(self):
        pass

    def pendown(self):
        pass

    def block(self):
        pass

    def delay(self, time_ms):
        pass

    def current_pen(self):
        return False

    def turtle_pen(self):
        return False

    def interactive(self):
        pass

    def connect(self):
        pass
