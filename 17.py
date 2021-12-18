import re

def parse(raw_input):
    return tuple(map(int, re.match(r'target area: x=([-\d]+)\.\.([-\d]+), y=([-\d]+)\.\.([-\d]+)', raw_input).groups()))

def tri(n):
    return (n + n ** 2) // 2

def sign(n):
    return (abs(n) // n) if n != 0 else 0

def first(xmin, xmax, ymin, ymax):
    return tri(abs(ymin) - 1)

def enters(xpos, ypos, xvel, yvel, xmin, xmax, ymin, ymax):
    within = xpos >= xmin and xpos <= xmax and ypos >= ymin and ypos <= ymax
    return xpos <= xmax and ypos >= ymin and (within or enters(xpos + xvel, ypos + yvel, xvel - sign(xvel), yvel - 1, xmin, xmax, ymin, ymax))

def second(xmin, xmax, ymin, ymax):
    minxvel, maxxvel = 0, xmax
    minyvel, maxyvel = ymin, (abs(ymin) - 1)
    area = (xmin, xmax, ymin, ymax)
    return len([None for xvel in range(minxvel, maxxvel + 1) for yvel in range(minyvel, maxyvel + 1) if enters(0, 0, xvel, yvel, *area)])

example = 'target area: x=20..30, y=-10..-5'