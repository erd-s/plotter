from config import DOC_HEIGHT, DOC_WIDTH, MARGIN
from nextdraw import NextDraw


def setup_plotter(nd: NextDraw):
    nd.interactive()
    if not nd.connect():
        quit()
    nd.pen_rate_lower = 40
    print("Current Settings:")
    print(f'Page Size: {DOC_WIDTH}"w x {DOC_HEIGHT}"h')
    print(f'Margin: {MARGIN}"')
    print(f"Center: {center_x()}, {center_y()}")
    print(f'Effective Size: {effective_width()}"w x {effective_height()}"h')
    return nd


def tear_down_plotter(plotter):
    plotter.penup()
    plotter.goto(0, 0)
    plotter.disconnect()


def effective_height():
    return DOC_HEIGHT - (2 * MARGIN)


def effective_width():
    return DOC_WIDTH - (2 * MARGIN)


def effective_x_start():
    return MARGIN


def effective_y_start():
    return MARGIN


def center_x():
    return effective_x_start() + (effective_width() / 2)


def center_y():
    return effective_y_start() + (effective_height() / 2)


def center():
    return [center_x(), center_y()]


def effective_x_end():
    return MARGIN + effective_width()


def effective_y_end():
    return MARGIN + effective_height()
