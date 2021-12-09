from itertools import chain

def parse(raw_input):
    return [[[''.join(sorted(e)) for e in fragment.split(' ')] for fragment in line.split(' | ')] for line in raw_input.split('\n')]

def first(values):
    return len(list(chain(*[[digit for digit in code if len(digit) in [2, 3, 4, 7]] for _casts, code in values])))

def includes_whole(source, form):
    found = next(cast for cast in source if (set(cast) | set(form)) == set(cast))
    rest = [cast for cast in source if (set(cast) | set(form)) != set(cast)]
    return found, rest

def decode(casts):
    one = next(cast for cast in casts if len(cast) == 2)
    four = next(cast for cast in casts if len(cast) == 4)
    seven = next(cast for cast in casts if len(cast) == 3)
    eight = next(cast for cast in casts if len(cast) == 7)

    all069 = [cast for cast in casts if len(cast) == 6]
    nine, all06 = includes_whole(all069, four)
    zero, six_list = includes_whole(all06, one)
    six = six_list[0]

    all235 = [cast for cast in casts if len(cast) == 5]
    three, all25 = includes_whole(all235, one)
    five = next(cast for cast in all25 if (set(six) | set(cast)) == set(six))
    two = next(cast for cast in all25 if cast != five)
    
    decoded = [zero, one, two, three, four, five, six, seven, eight, nine] 
    return {cast: index for index, cast in enumerate(decoded)}

def get_val(mapped, digits):
    return int(''.join(str(mapped[digit]) for digit in digits))

def second(values):
    return sum(get_val(decode(casts), code) for casts, code in values)

example = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'