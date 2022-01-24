def color(txt, num):
    return f'\033[3{num}m{txt}\033[m'


def red(txt):
    return color(txt, 1)


def green(txt):
    return color(txt, 2)


def yellow(txt):
    return color(txt, 3)


def blue(txt):
    return color(txt, 4)


def purple(txt):
    return color(txt, 5)


def light_blue(txt):
    return color(txt, 6)


def grey(txt):
    return color(txt, 7)


def white(txt):
    return color(txt, 8)
