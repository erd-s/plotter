from projects.rectangles.rectangle import draw_rectangle_with_origin
from utils.plotter_interface import PlotterInterface
from projects.text.text import HorizontalText


def draw_item_sheet(
    plotter: PlotterInterface,
    origin_x: float,
    origin_y: float,
    height: float,
    width: float,
):
    items_per_page = 5
    padding = 0.05
    item_padding = padding * 2
    effect_height = (height - item_padding) / (
        items_per_page + ((items_per_page - 1) * item_padding)
    )
    number_of_checkboxes = 5
    attune_status_width = (
        effect_height - (padding * (number_of_checkboxes - 1))
    ) / number_of_checkboxes
    name_and_uses_origin_x = origin_x + attune_status_width + padding
    name_and_uses_width = width * 0.4

    name_and_uses_height = (effect_height / 2) - (padding / 2)
    effect_origin_x = name_and_uses_origin_x + name_and_uses_width + padding
    effect_width = width - (padding * 2) - name_and_uses_width - attune_status_width
    items_origin_y = origin_y + padding

    # item 1
    for i in range(items_per_page):
        # attune status
        for r in range(number_of_checkboxes):
            draw_rectangle_with_origin(
                plotter=plotter,
                origin_x=origin_x,
                origin_y=items_origin_y
                + (i * effect_height)
                + (item_padding * i)
                + (r * (attune_status_width + padding)),
                height=attune_status_width,
                width=attune_status_width,
            )

        # name
        draw_rectangle_with_origin(
            plotter=plotter,
            origin_x=name_and_uses_origin_x,
            origin_y=items_origin_y + (i * effect_height) + (item_padding * i),
            height=name_and_uses_height,
            width=name_and_uses_width,
        )

        # uses
        draw_rectangle_with_origin(
            plotter=plotter,
            origin_x=name_and_uses_origin_x,
            origin_y=items_origin_y
            + name_and_uses_height
            + padding
            + (i * effect_height)
            + (item_padding * i),
            height=name_and_uses_height,
            width=name_and_uses_width,
        )

        # effect
        draw_rectangle_with_origin(
            plotter=plotter,
            origin_x=effect_origin_x,
            origin_y=items_origin_y + (i * effect_height) + (item_padding * i),
            height=effect_height,
            width=effect_width,
        )

        # char_width = 0.15
        #
        # item_name_title = "item"
        # attune_text = HorizontalText(
        #     plotter=plotter,
        #     text=item_name_title,
        #     origin_x=name_and_uses_origin_x + 0.1,
        #     origin_y=title_origin_y,
        #     width=len(item_name_title) * char_width,
        #     height=0.1,
        # )
        # attune_text.draw_text()
        #
        # desc_name_title = "description"
        # attune_text = HorizontalText(
        #     plotter=plotter,
        #     text=desc_name_title,
        #     origin_x=effect_origin_x + 0.1,
        #     origin_y=title_origin_y,
        #     width=len(desc_name_title) * char_width,
        #     height=0.1,
        # )
        # attune_text.draw_text()
