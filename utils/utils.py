from config import DOC_HEIGHT, DOC_WIDTH, MARGIN_HORIZONTAL, MARGIN_VERTICAL


def effective_height():
    return DOC_HEIGHT - (2 * MARGIN_VERTICAL)


def effective_width():
    return DOC_WIDTH - (2 * MARGIN_HORIZONTAL)


def effective_x_start():
    return MARGIN_HORIZONTAL


def effective_y_start():
    return MARGIN_VERTICAL


def center_x():
    return effective_x_start() + (effective_width() / 2)


def center_y():
    return effective_y_start() + (effective_height() / 2)


def center():
    return [center_x(), center_y()]


def effective_x_end():
    return MARGIN_HORIZONTAL + effective_width()


def effective_y_end():
    return MARGIN_VERTICAL + effective_height()


def horizontal_margin():
    return MARGIN_HORIZONTAL


def vertical_margin():
    return MARGIN_VERTICAL
