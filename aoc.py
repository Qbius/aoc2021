from sys import argv
from typing import get_type_hints
from common import regex, RegexBase, raw_input

if len(argv) != 2:
    print('only specify the day please')
    exit()

name = argv[1]
notimpl = lambda _: 'not implemented'

day_module = __import__(name)
day_input_raw = open(f'inputs/{name}.txt').read()
day_input = [line.strip() for line in open(f'inputs/{name}.txt').readlines()]

day_first = getattr(day_module, 'first', notimpl)
day_second = getattr(day_module, 'second', notimpl)

def call_with_appropriate_arg(day_f):
    global day_input
    type_hints = list(get_type_hints(day_f).values())
    if not type_hints:
        return day_f(day_input)
    elif RegexBase in type_hints[0].__bases__:
        return day_f(type_hints[0].process(day_input))
    elif type_hints[0] == raw_input:
        return day_f(day_input_raw)
    else:
        return day_f(list(map(type_hints[0], day_input)))

print('First:', call_with_appropriate_arg(day_first))
print('Second:', call_with_appropriate_arg(day_second))