def parse(raw_input):
    dots_strs, fold_instructions_str = [part.split('\n') for part in raw_input.split('\n\n')]
    dots = [list(map(int, dot_str.split(','))) for dot_str in dots_strs]
    fold_instructions = [tuple(map(lambda x: int(x) if x.isdigit() else (x == 'x'), fold_str.split(' ')[-1].split('='))) for fold_str in fold_instructions_str]
    return dots, fold_instructions

def fold(dots, fold_instructions):
    for is_horizontal, line in fold_instructions:
        for i, dot in enumerate(dots):
            relevant_index = 0 if is_horizontal else 1
            if dot[relevant_index] > line:
                dots[i][relevant_index] = line - (dot[relevant_index] - line)
    return set(map(tuple, dots))

def first(dots, fold_instructions):
    fold_instructions = fold_instructions[:1]
    return len(fold(dots, fold_instructions))

def second(dots, fold_instructions):
    folded_dots = fold(dots, fold_instructions)
    max_x, max_y = max(x for x, y in folded_dots) + 1, max(y for x, y in folded_dots) + 1
    return '\n' + '\n'.join(''.join('█' if (x, y) in folded_dots else ' ' for x in range(max_x)) for y in range(max_y))

example = '''
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''