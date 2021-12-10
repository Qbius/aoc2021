from itertools import chain
from math import prod

def parse(raw_input):
    return [list(map(int, line)) for line in raw_input.split('\n')]

def lowest_points(map):
    width, height = len(map[0]), len(map)
    get = lambda h, w: map[h][w] if (h >= 0 and h < height) and (w >= 0 and w < width) else 10
    return [(h, w) for h in range(height) for w in range(width) if all(get(h + hh, w + ww) > map[h][w] for hh, ww in [(1, 0), (-1, 0), (0, 1), (0, -1)])]

def first(map):
    return sum(map[h][w] + 1 for h, w in lowest_points(map))

def travel(point, map, basin):
    h, w = point
    height, width = len(map), len(map[0]), 
    adjacent = [(nh, nw) for ww, hh in [(1, 0), (-1, 0), (0, 1), (0, -1)] if ((nh := (h + hh)), (nw:= (w + ww))) not in basin and nw >= 0 and nw < width and nh >= 0 and nh < height and map[nh][nw] != 9]
    basin.update(adjacent)
    return [point, *list(chain(*[travel(p, map, basin) for p in adjacent]))]

def get_basin(lp, map):
    return set(travel(lp, map, set()))

def second(map):
    basins = [get_basin(lp, map) for lp in lowest_points(map)]
    return prod(sorted(len(basin) for basin in basins)[::-1][:3])

def extra(map):
    basins = [get_basin(lp, map) for lp in lowest_points(map)]
    basins.sort(key=lambda b: -len(b))
    geant = set().union(*basins[:3])
    for h in range(len(map)):
        for w in range(len(map[0])):
            if map[h][w] == 9:
                map[h][w] = '9'
            else:
                map[h][w] = '@' if (h, w) in geant else ' '
    with open('extra/day9basins.txt', 'w') as o_file:
        o_file.write('\n'.join(''.join(line) for line in map))

example = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''