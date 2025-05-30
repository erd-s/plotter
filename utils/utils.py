from config import DOC_HEIGHT, DOC_WIDTH, MARGIN_TOP, MARGIN_BOTTOM, MARGIN_LEFT, MARGIN_RIGHT


def effective_height():
    return DOC_HEIGHT - (MARGIN_TOP + MARGIN_BOTTOM)


def effective_width():
    return DOC_WIDTH - (MARGIN_LEFT + MARGIN_RIGHT)


def effective_x_start():
    return MARGIN_LEFT


def effective_y_start():
    return MARGIN_TOP


def center_x():
    return effective_x_start() + (effective_width() / 2)


def center_y():
    return effective_y_start() + (effective_height() / 2)


def center():
    return [center_x(), center_y()]


def effective_x_end():
    return DOC_WIDTH - MARGIN_RIGHT


def effective_y_end():
    return DOC_HEIGHT - MARGIN_BOTTOM
