from statistics import median, mean

def parse(raw_input):
    return list(map(int, raw_input.split(',')))

def fuel_1(pos, values):
    return sum(abs(val - pos) for val in values)

def fuel_2(pos, values):
    triangular = lambda n: (n + n ** 2) // 2
    return sum(triangular(abs(val - pos)) for val in values)

def first(values):
    return fuel_1(int(median(values)), values)

def second(values):
    return fuel_2(int(mean(values)), values)

example = '16,1,2,0,4,2,7,1,2,14'