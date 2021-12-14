from itertools import pairwise, starmap
from functools import cache
from collections import Counter as counter

def parse(raw_input):
    string, rules_str = [part.strip() for part in raw_input.split('\n\n')]
    rules = dict(tuple(rules_line.split(' -> ')) for rules_line in rules_str.split('\n'))
    return string, rules

def steps(string, rules, nsteps):

    @cache
    def frequencies(a, b, steps=nsteps):
        inter = rules[a + b]
        return (frequencies(a, inter, steps - 1) + frequencies(inter, b, steps - 1) + counter({inter: 1})) if steps > 0 else counter()

    total_frequencies = counter(string) + sum(starmap(frequencies, pairwise(string)), counter())
    return max(total_frequencies.values()) - min(total_frequencies.values())

def first(string, rules):
    return steps(string, rules, 10)

def second(string, rules):
    return steps(string, rules, 40)

example = '''
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''