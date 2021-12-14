from itertools import chain

def parse(raw_input):
    start, rules_str = [part.strip() for part in raw_input.split('\n\n')]
    rules = dict(tuple(rules_line.split(' -> ')) for rules_line in rules_str.split('\n'))
    return start, rules

def merge(*dicts):
    return {key: sum(dic.get(key, 0) for dic in dicts) for key in set(chain(*[dic.keys() for dic in dicts]))}

precalced = {}
def total_score(a, b, rules, stepsleft):
    if stepsleft == 0:
        return {}
    if (a, b, stepsleft) not in precalced:
        inter = rules[a + b]
        prev1 = total_score(a, inter, rules, stepsleft - 1)
        prev2 = total_score(inter, b, rules, stepsleft - 1)
        this = {inter: 1}
        precalced[a, b, stepsleft] = merge(prev1, prev2, this)
    return precalced[a, b, stepsleft]

def start_scoring(string, rules, steps):
    initial = {c: string.count(c) for c in set(string)}
    merged = merge(initial, *[total_score(a, b, rules, steps) for a, b in zip(string[:-1], string[1:])])
    return max(merged.values()) - min(merged.values())

def first(info):
    start, rules = info
    return start_scoring(start, rules, 10)

def second(info):
    start, rules = info
    return start_scoring(start, rules, 40)

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