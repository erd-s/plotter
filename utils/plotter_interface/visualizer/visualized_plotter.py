from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from config import DOC_HEIGHT, DOC_WIDTH
from utils.plotter_interface.PlotterInterface import PlotterInterface


class VisualizedPlotter(PlotterInterface):
    current_x: float = 0
    current_y: float = 0
    path = []
    ax: Axes = []

    def __plot(self, line_style="solid", color=None):
        x_list = [x[0] for x in self.path]
        y_list = [y[1] for y in self.path]
        self.ax.plot(x_list, y_list, linestyle=line_style, color=color)
        print(f"plotting path: {self.path}")
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
        self.__plot(line_style="dotted", color="silver")

        return True

    @staticmethod
    def disconnect(**kwargs):
        plt.show()

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

            self.current_x = x
            self.current_y = y
        else:
            self.current_x = x_target
            self.current_y = y_target

    def go(self, x_delta, y_delta):
        if self.clip_to_bounds:
            x = self.current_x + x_delta
            if x < self.x_min:
                x = self.x_min
            elif x > self.x_max:
                x = self.x_max

            y = self.current_y + y_delta
            if y < self.y_min:
                y = self.y_min
            elif y > self.y_max:
                y = self.y_max

            self.current_x = x
            self.current_y = y
        else:
            self.current_x += x_delta
            self.current_y += y_delta

    def lineto(self, x_target, y_target):
        self.path.append([self.current_x, self.current_y])
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

            self.path.append([x, y])
        else:
            self.path.append([x_target, y_target])
        self.__plot()
        self.current_x += x_target
        self.current_y += y_target

    def line(self, x_delta, y_delta):
        self.path.append([self.current_x, self.current_y])
        if self.clip_to_bounds:
            x = self.current_x + x_delta
            if x < self.x_min:
                x = self.x_min
            elif x > self.x_max:
                x = self.x_max

            y = self.current_y + y_delta
            if y < self.y_min:
                y = self.y_min
            elif y > self.y_max:
                y = self.y_max

            self.path.append([x, y])
        else:
            self.path.append([self.current_x + x_delta, self.current_y + y_delta])

        self.__plot()
        self.current_x += x_delta
        self.current_y += y_delta

    def moveto(self, x_target, y_target):
        self.goto(x_target, y_target)
        self.__plot()

    def move(self, x_delta, y_delta):
        self.go(x_delta, y_delta)
        self.__plot()

    def draw_path(self, vertex_list):
        if self.clip_to_bounds:
            for i, point in enumerate(vertex_list):
                x, y = point[0], point[1]
                if self.x_min < x < self.x_max and self.y_min < y < self.y_max:
                    # both in bounds
                    self.path.append([x,y])
                    if i + 1 == len(vertex_list):
                        self.__plot()
                else:
                    if len(self.path) >= 1:
                        last_point = self.path[-1]
                        self.current_x = last_point[0]
                        self.current_y = last_point[1]
                        self.__plot()
        else:
            self.path += vertex_list
            last_point = self.path[-1]
            self.current_x = last_point[0]
            self.current_y = last_point[1]
            self.__plot()

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
    def current_pen(**kwargs):
        return False

    @staticmethod
    def turtle_pen(**kwargs):
        return False

    def interactive(self):
        pass

    def load_config(self, config_ref):
        pass
