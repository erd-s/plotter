from matplotlib import pyplot as plt
from matplotlib.axes import Axes


class VisualizedPlotter:
    current_x: float = 0
    current_y: float = 0
    path = []
    ax: Axes = []

    def plot(self):
        x_list = [x[0] for x in self.path]
        y_list = [y[1] for y in self.path]
        self.ax.plot(x_list, y_list)
        self.path = []

    def connect(self):
        _, ax = plt.subplots()
        self.ax = ax
        return True

    def disconnect(self):
        plt.show()

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
        self.plot()

    def move(self, x_delta, y_delta):
        self.current_x += x_delta
        self.current_y += y_delta
        self.plot()

    def draw_path(self, vertex_list):
        for path in vertex_list:
            self.path.append(path)

        last_point = vertex_list[-1]
        self.current_x = last_point[0]
        self.current_y = last_point[1]
        self.plot()

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

    @staticmethod
    def current_pen():
        return False

    @staticmethod
    def turtle_pen():
        return False

    def interactive(self):
        pass

    def load_config(self, config_ref):
        pass
