from statistics import median, mean
from common import raw_input

def fuel_1(pos, values):
    return sum(abs(val - pos) for val in values)

def fuel_2(pos, values):
    triangular = lambda n: (n + n ** 2) // 2
    return sum(triangular(abs(val - pos)) for val in values)

def parse_and_apply(values, find_f, fuel_f):
    values = list(map(int, values.split(',')))
    best_position = int(find_f(values))
    return fuel_f(best_position, values)


def first(values: raw_input):
    return parse_and_apply(values, median, fuel_1)

def second(values: raw_input):
    return parse_and_apply(values, mean, fuel_2)
