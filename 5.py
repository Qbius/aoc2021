from common import regex
from itertools import chain

def sign(n):
    return (n // abs(n)) if n != 0 else 0

def find_doubled_points(lines):
    to_points = [[(x1 + i * sign(x2 - x1), y1 + i * sign(y2 - y1)) for i in range((max(abs(x2 - x1), abs(y2 - y1)) + 1))] for x1, y1, x2, y2 in lines]
    
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


def first(values: regex(r'(\d+),(\d+) -> (\d+),(\d+)', (int, int, int, int))):
    return find_doubled_points([(x1, y1, x2, y2) for x1, y1, x2, y2 in values if x1 == x2 or y1 == y2])

def second(values: regex(r'(\d+),(\d+) -> (\d+),(\d+)', (int, int, int, int))):
    return find_doubled_points(values)

example = '''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''