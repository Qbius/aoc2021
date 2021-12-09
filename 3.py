def most_common(column):
    return sorted(column)[len(column) // 2]

def first(values):
    common = ''.join(map(most_common, zip(*values)))
    return int(common, 2) * int(''.join('0' if c == '1' else '1' for c in common), 2)

def find_matching(all_values, flip_bit=False):
    if len(all_values) == 1:
        return all_values[0]
    else:
        first_column, *_rest = list(zip(*all_values))
        most_common_bit = most_common(first_column)
        if flip_bit:
            most_common_bit = '1' if most_common_bit == '0' else '0'
        return most_common_bit + find_matching([val[1:] for val in all_values if val[0] == most_common_bit], flip_bit)

def second(values):
    return int(find_matching(values), 2) * int(find_matching(values, flip_bit=True), 2)

example = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''