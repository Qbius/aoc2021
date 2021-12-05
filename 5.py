from common import regex
from itertools import chain

def sign(n):
    return (n // abs(n)) if n != 0 else 0

def first(values: regex(r'(\d+),(\d+) -> (\d+),(\d+)', (int, int, int, int))):
    values = [(x1, y1, x2, y2) for x1, y1, x2, y2 in values if x1 == x2 or y1 == y2]
    to_points = [[(x1 + i * sign(x2 - x1), y1 + i * sign(y2 - y1)) for i in range((max(abs(x2 - x1), abs(y2 - y1)) + 1))] for x1, y1, x2, y2 in values]
    
    singular = set()
    doubledd = set()
    for point in chain(*to_points):
        if point in doubledd:
            pass
        elif point in singular:
            doubledd.add(point)
        else:
            singular.add(point)
    return len(doubledd)

def second(values: regex(r'(\d+),(\d+) -> (\d+),(\d+)', (int, int, int, int))):
    to_points = [[(x1 + i * sign(x2 - x1), y1 + i * sign(y2 - y1)) for i in range((max(abs(x2 - x1), abs(y2 - y1)) + 1))] for x1, y1, x2, y2 in values]
    
    singular = set()
    doubledd = set()
    for point in chain(*to_points):
        if point in doubledd:
            pass
        elif point in singular:
            doubledd.add(point)
        else:
            singular.add(point)
    return len(doubledd)