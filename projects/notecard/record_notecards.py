from projects.notecard.notecard import NoteCard
from utils.plotter_interface import PlotterInterface
from projects.squiggle_fill.squiggle_path import draw_squiggle_rectangle_rounded


class RecordNoteCard(NoteCard):
    def object_logic(
        self,
        plotter: PlotterInterface,
        origin_x: float,
        origin_y: float,
        width: float,
        height: float,
        invert: bool = False,
    ):
        draw_squiggle_rectangle_rounded(
            plotter=plotter,
            origin_x=origin_x,
            origin_y=origin_y,
            height=height,
            width=width,
            space_between_lines=height / 7,
            reverse=invert,
        )
