from itertools import chain

def parse(raw_input):
    lines = raw_input.split('\n')
    allsn = list(chain(*[[(c, (h, w)) for w, c in enumerate(line) if c != '.'] for h, line in enumerate(lines)]))
    east = {pos for c, pos in allsn if c == '>'}
    south = {pos for c, pos in allsn if c == 'v'}
    return east, south, (len(lines), len(lines[0]))

def count_steps(east, south, size, step=1):
    height, width = size
    
    next_east = lambda pos: (pos[0], (pos[1] + 1) % width)
    move_east = lambda pos: next_east(pos) if next_east(pos) not in east and next_east(pos) not in south else pos
    moved_east = set(map(move_east, east))

    next_soth = lambda pos: ((pos[0] + 1) % height, pos[1])
    move_soth = lambda pos: next_soth(pos) if next_soth(pos) not in moved_east and next_soth(pos) not in south else pos
    moved_soth = set(map(move_soth, south))
    
    return step if east == moved_east and south == moved_soth else count_steps(moved_east, moved_soth, size, step + 1)

def first(east, south, size):
    return count_steps(east, south, size)

example = '''
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''