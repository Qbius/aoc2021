from functools import cache

def parse(inpt):
    return list(map(int, inpt.split(',')))

@cache
def total_children(days):
    spawned = list(range(1, days, 7))
    return len(spawned) + sum(total_children(days - spawn - 8) for spawn in spawned)

def total_by_timers(timers, days):
    return len(timers) + sum(total_children(days - timer + 1) for timer in timers)

def first(timers):
    return total_by_timers(timers, 80)

def second(timers):
    return total_by_timers(timers, 256)
    
example = '3,4,3,1,2'
