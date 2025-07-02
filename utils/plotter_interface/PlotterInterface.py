from typing import Protocol
from abc import abstractmethod


class PlotterInterface:
    clip_to_bounds: bool
    x_min: float
    x_max: float
    y_min: float
    y_max: float

    def __init__(
        self,
        clip_to_bounds: bool,
        x_min: float,
        x_max: float,
        y_min: float,
        y_max: float,
    ):
        self.clip_to_bounds = clip_to_bounds
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    @abstractmethod
    def disconnect(self): ...
    @abstractmethod
    def goto(self, x_target, y_target): ...
    @abstractmethod
    def go(self, x_delta, y_delta): ...
    @abstractmethod
    def lineto(self, x_target, y_target): ...
    @abstractmethod
    def line(self, x_delta, y_delta): ...
    @abstractmethod
    def moveto(self, x_target, y_target): ...
    @abstractmethod
    def move(self, x_delta, y_delta): ...
    @abstractmethod
    def draw_path(self, vertex_list): ...
    @abstractmethod
    def turtle_pos(self): ...
    @abstractmethod
    def current_pos(self) -> dict: ...
    @abstractmethod
    def update(self): ...
    @abstractmethod
    def usb_query(self, query): ...
    @abstractmethod
    def usb_command(self, command): ...
    @abstractmethod
    def penup(self): ...
    @abstractmethod
    def pendown(self): ...
    @abstractmethod
    def block(self): ...
    @abstractmethod
    def delay(self, time_ms): ...
    @abstractmethod
    def current_pen(self) -> bool: ...
    @abstractmethod
    def turtle_pen(self) -> bool: ...
    @abstractmethod
    def interactive(self): ...
    @abstractmethod
    def connect(self) -> bool: ...
    @abstractmethod
    def load_config(self, config_ref): ...

    def override_bounds(self, x_min: float, x_max: float, y_min: float, y_max: float):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
