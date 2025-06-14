import matplotlib.pyplot as plt
import numpy as np

from nextdraw import NextDraw

class VisualizedPlotter(NextDraw):
    current_x: float = 0
    current_y: float = 0
    path = []
    def connect(self):
        pass

    def disconnect(self):
        x_list = [x[0] for x in self.path]
        y_list = [y[1] for y in self.path]
        plt.show(x_list, y_list)

    def current_pos(self):
        return [self.current_x, self.current_y]

    def penup(self):
        pass

    def pendown(self):
        pass
    def lineto(self,x_target,y_target):
        self.path.append([x_target, y_target])
        self.current_x += x_target
        self.current_y += y_target

    def line(self,x_delta,y_delta):
        self.path.append([self.current_x + x_delta, self.current_y + y_delta])
        self.current_x += x_delta
        self.current_y += y_delta

    def move(self,x_delta,y_delta):
        self.current_x += x_delta
        self.current_y += y_delta

    def moveto(self,x_target,y_target):
        self.current_x = x_target
        self.current_y = y_target
