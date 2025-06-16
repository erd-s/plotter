from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from config import DOC_HEIGHT, DOC_WIDTH


class VisualizedPlotter:
    current_x: float = 0
    current_y: float = 0
    path = []
    ax: Axes = []

    def plot(self, linestyle="solid", color=None):
        x_list = [x[0] for x in self.path]
        y_list = [y[1] for y in self.path]
        self.ax.plot(x_list, y_list, linestyle=linestyle, color=color)
        self.path = []

    def connect(self):
        _, ax = plt.subplots()
        plt.gca().invert_yaxis()
        gcf = plt.gcf()
        gcf.set_size_inches(DOC_WIDTH, DOC_HEIGHT)
        gcf.set_dpi(187)
        self.ax = ax
        self.ax.set_ylabel(f"{DOC_HEIGHT} in.", color="silver")
        self.ax.set_xlabel(f"{DOC_WIDTH} in.", color="silver")
        self.path.append([0, 0])
        self.path.append([DOC_WIDTH, 0])
        self.path.append([DOC_WIDTH, DOC_HEIGHT])
        self.path.append([0, DOC_HEIGHT])
        self.path.append([0, 0])
        self.plot(linestyle="dotted", color="silver")

        return True

    @staticmethod
    def disconnect():
        plt.show()

    def goto(self, x_target, y_target):
        self.current_x = x_target
        self.current_y = y_target

    def go(self, x_delta, y_delta):
        self.current_x += x_delta
        self.current_y += y_delta

    def lineto(self, x_target, y_target):
        self.path.append([self.current_x, self.current_y])
        self.path.append([x_target, y_target])
        self.plot()
        self.current_x += x_target
        self.current_y += y_target

    def line(self, x_delta, y_delta):
        self.path.append([self.current_x, self.current_y])
        self.path.append([self.current_x + x_delta, self.current_y + y_delta])
        self.plot()
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
