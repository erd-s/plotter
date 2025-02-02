from config import DOC_HEIGHT, DOC_WIDTH, MARGIN


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
