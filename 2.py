from common import regex

def first(values: regex(r'([a-z]+) (\d+)', (str, int))):
    return sum(val for typ, val in values if typ == 'forward') * sum(val * (1 if typ == 'down' else -1) for typ, val in values if typ in ['up', 'down'])

def second(values: regex(r'([a-z]+) (\d+)', (str, int))):
    horizontal = 0
    aim = 0
    depth = 0
    for typ, val in values:
        if typ == 'forward':
            horizontal += val
            depth += val * aim
        elif typ in ['up', 'down']:
            aim += val * (1 if typ == 'down' else -1)
    return horizontal * depth

example = '''
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''