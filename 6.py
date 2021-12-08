from common import raw_input

def total_children(days, cooldown):
    spawned = list(range(cooldown, days, 7))
    return (len(spawned) + sum(total_children(days, spawn + 9) for spawn in spawned)) if len(spawned) > 0 else 0

def total_lanternfish(days, initial):
    return sum(total_children(days, cd) for cd in initial) + len(initial)


def first(values: raw_input):
    timers = list(map(int, values.split(',')))
    return total_lanternfish(80, timers)

def second(values: raw_input):
    timers = list(map(int, values.split(',')))
    for i in range(256):
        print(f'{i:0>2}: {total_children(i, 0)}')
    #return total_lanternfish(256, timers)

