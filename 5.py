from common import regex

def first(values: regex(r'(\d+),(\d+) -> (\d+),(\d+)', (int, int, int, int))):
    print(values)