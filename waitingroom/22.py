import re
from math import prod

def parse(raw_input):
    values = [tuple(map(int, re.findall(r'[-\d]+', line))) for line in raw_input.split('\n')]
    return [((xmin, xmax), (ymin, ymax), (zmin, zmax)) for xmin, xmax, ymin, ymax, zmin, zmax in values]

def common_area(rect1, rect2):
    common = [nd - st + 1 for axismins, axismaxs in [zip(rect1axis, rect2axis) for rect1axis, rect2axis in zip(rect1, rect2)] if (st := max(axismins)) < (nd := min(axismaxs))]
    return prod(common) if len(common) == 3 else 0

def build_common_map(values):
    return {(i, j + i + 1): common_area(v1, v2) for i, v1 in enumerate(values[:-1]) for j, v2 in enumerate(values[i + 1:])}

def first(values):
    common_map = build_common_map(values)
    [sum(com) for i, v in enumerate(values)]
    print(common_map.keys())

def second(values):
    pass

20, 30, 25, 35
20, 30, 20, 40
20, 30, 40, 50

example = '''
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
'''