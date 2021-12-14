
def parse(raw_input):
    split = raw_input.split('\n')
    return {(w, h): int(split[h][w]) for w in range(len(split[0])) for h in range(len(split))}

def all_adjacent(point, map):
    pw, ph = point
    width, height = 10, 10
    return [
        ((ww + pw), (hh + ph)) 
            for ww in [-1, 0, 1]
            for hh in [-1, 0, 1]
            if 
                ((ww + pw) >= 0) and
                ((ww + pw) < width) and
                ((hh + ph) >= 0) and
                ((hh + ph) < height)
    ]

def increase_by_1(point, map, flashed):
    if point not in flashed:
        map[point] += 1
        if map[point] > 9:
            flashed.add(point)
            map[point] = 0
            for ap in all_adjacent(point, map):
                increase_by_1(ap, map, flashed)

def step(map):
    flashed = set()
    for point in map.keys():
        increase_by_1(point, map, flashed)
    return len(flashed), map

def n_steps(map, n):
    res = 0
    for _ in range(n):
        score, map = step(map)
        res += score
    return res

def first(dumbos):
    return n_steps(dumbos, 100)

def find_synchronized(map):
    nstep = 0
    while True:
        score, map = step(map)
        nstep += 1
        if score == len(map):
            return nstep

def second(dumbos):
    return find_synchronized(dumbos)

example = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''