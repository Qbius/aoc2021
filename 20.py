import numpy as np
from itertools import repeat

def parse(raw_input):
    enhancement_str, image_raw = raw_input.split('\n\n')
    enhancement = enhancement_str.strip()
    array_base = [list(0 if c == '.' else 1 for c in line) for line in image_raw.split('\n')]
    return enhancement, np.array(array_base)

def process(enhancement, array, infinitepixel):
    height, width = array.shape
    base = (np.zeros if infinitepixel == 0 else np.ones)(shape=(height + 4, width + 4), dtype=int)
    for h, row in enumerate(array):
        for w, cell in enumerate(row):
            base[h + 2, w + 2] = cell
    
    new = np.empty(shape=(height + 2, width + 2), dtype=int)
    for h in range(height + 2):
        for w in range(width + 2):
            new[h, w] = 1 if enhancement[int(''.join(map(str, base[h:h+3, w:w+3].flat)), 2)] == '#' else 0

    infinitepixel = 1 if enhancement[int(''.join(map(str, repeat(infinitepixel, 9))), 2)] == '#' else 0
    return new, infinitepixel

def first(enhancement, array):
    infpixel = 0
    for _ in range(2):
        array, infpixel = process(enhancement, array, infpixel)
    return array.sum()

def second(enhancement, array):
    infpixel = 0
    for _ in range(50):
        array, infpixel = process(enhancement, array, infpixel)
    return array.sum()

example = '''
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''