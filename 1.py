def first(values: int):
    return len([None for a, b in zip(values[:-1], values[1:]) if (b - a) > 0])

def second(values: int):
    return len([None for a, b, c, d in zip(values[:-3], values[1:-2], values[2:-1], values[3:]) if ((b + c + d) - (a + b + c)) > 0])