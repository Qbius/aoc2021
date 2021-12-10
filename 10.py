from statistics import median
from functools import reduce

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
illegal_chunks = [f'{a}{b}' for ia, a in enumerate(opening) for ib, b in enumerate(closing) if ia != ib]

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def find_illegal(line):
    ics = sorted((line.index(ic), ic) for ic in illegal_chunks if ic in line)
    if ics:
        (_, first_illegal), *_rest = ics
        return first_illegal[1]
    else:
        line_replaced = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
        return '' if line == line_replaced else find_illegal(line_replaced)

def first(lines):
    return sum(points[res] for line in lines if (res := find_illegal(line)) != '')

def pure_form(line):
    line_replaced = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
    return line if line == line_replaced else pure_form(line_replaced)

def calculate_score(addendum):
    return reduce(lambda score, c: score * 5 + closing.index(c) + 1, addendum, 0)
    
def second(lines):
    notcorrupted = [line for line in lines if find_illegal(line) == '']
    scores = [calculate_score(''.join(closing[opening.index(c)] for c in pure_form(nc)[::-1])) for nc in notcorrupted]
    return median(scores)

example = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''