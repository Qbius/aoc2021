from statistics import median, mean
from common import single_line

def fuel_1(pos, values):
    return sum(abs(val - pos) for val in values)

def fuel_2(pos, values):
    triangular = lambda n: (n + n ** 2) // 2
    return sum(triangular(abs(val - pos)) for val in values)

def first(values: single_line(',', int)):
    return fuel_1(int(median(values)), values)

def second(values: single_line(',', int)):
    return fuel_2(int(mean(values)), values)

example = '16,1,2,0,4,2,7,1,2,14'