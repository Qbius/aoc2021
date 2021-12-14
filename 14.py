from itertools import chain

def parse(raw_input):
    string, rules_str = [part.strip() for part in raw_input.split('\n\n')]
    rules = dict(tuple(rules_line.split(' -> ')) for rules_line in rules_str.split('\n'))
    return string, rules

def merge(*dicts):
    dicts = [dic for dic in dicts if dic]
    return {key: sum(dic.get(key, 0) for dic in dicts) for key in set(chain(*[dic.keys() for dic in dicts]))}

class freq_calc(object):
    def __init__(self, string, rules):
        self.string = string
        self.rules = rules

    def steps(self, nsteps):
        self.precalced = {}
        initial = {c: self.string.count(c) for c in set(self.string)}
        pair_frequencies = [self.frequencies(a, b, nsteps) for a, b in zip(self.string[:-1], self.string[1:])]
        merged = merge(initial, *pair_frequencies)
        return max(merged.values()) - min(merged.values())

    def frequencies(self, a, b, steps):
        if (a, b, steps) not in self.precalced:
            inter = self.rules[a + b]
            self.precalced[a, b, steps] = merge(self.frequencies(a, inter, steps - 1), self.frequencies(inter, b, steps - 1), {inter: 1}) if steps > 0 else {}
        return self.precalced[a, b, steps]

def first(info):
    return freq_calc(*info).steps(10)

def second(info):
    return freq_calc(*info).steps(40)

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