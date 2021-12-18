import json
from itertools import pairwise
from iteration_utilities import deepflatten
from math import floor, ceil

def unpack_snailfish(l, depth=1):
    return list(deepflatten([unpack_snailfish(e, depth + 1) if isinstance(e, list) else (e, depth) for e in l], ignore=tuple))

def reduce_snailfish(number):
    should_explode = any(depth1 == depth2 and depth1 > 4 for (val1, depth1), (val2, depth2) in pairwise(number))
    should_besplit = any(number >= 10 for number, depth in number)
    if should_explode:
        expl_i = next(i for i, ((val1, dep1), (val2, dep2)) in enumerate(pairwise(number)) if dep1 == dep2 and dep1 > 4)
        val1, depth = number[expl_i]
        val2, _ = number[expl_i + 1]
        if expl_i > 0:
            number[expl_i - 1] = (number[expl_i - 1][0] + val1, number[expl_i - 1][1])
        if (expl_i + 1) < (len(number) - 1):
            number[expl_i + 2] = (number[expl_i + 2][0] + val2, number[expl_i + 2][1])
        del number[expl_i + 1]
        number[expl_i] = (0, depth - 1)
        return reduce_snailfish(number)
    elif should_besplit:
        splt_i, val, depth = next((i, number, depth) for i, (number, depth) in enumerate(number) if number >= 10)
        number[splt_i] = (ceil(val / 2), depth + 1)
        number.insert(splt_i, (floor(val / 2), depth + 1))
        return reduce_snailfish(number)
    else:
        return number

def mgntud_snailfish(number):
    highest_depth = max(depth for val, depth in number)
    highest_depth_i, val1 = next((i, val) for i, (val, depth) in enumerate(number) if depth == highest_depth)
    val2, _ = number[highest_depth_i + 1]
    del number[highest_depth_i + 1]
    number[highest_depth_i] = (val1 * 3 + val2 * 2, highest_depth - 1)
    return number[0][0] if len(number) == 1 else mgntud_snailfish(number)

class snailfish(object):
    def __init__(self, number, skip_unpacking=False):
        self.number = number if skip_unpacking else unpack_snailfish(number)
        self.number = reduce_snailfish(self.number)

    def __add__(self, other):
        return snailfish([(val, dep + 1) for val, dep in (self.number + other.number)], skip_unpacking=True)

    def magnitude(self):
        return mgntud_snailfish(self.number)

def parse(raw_input):
    return list(map(snailfish, (map(json.loads, raw_input.split('\n')))))

def first(numbers):
    return sum(numbers[1:], start=numbers[0]).magnitude()

def second(numbers):
    return max((num1 + num2).magnitude() for i1, num1 in enumerate(numbers) for i2, num2 in enumerate(numbers) if i1 != i2)

example = '''
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
'''