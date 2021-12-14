from functools import cache
from common import single_line

@cache
def total_children(days, offset, timers=None):
    timers = timers if timers else tuple(range(1, days, 7))
    return len(timers) + sum(total_children(days - timer + offset, -8) for timer in timers)

def first(timers: single_line(',', int)):
    return total_children(80, 1, tuple(timers))

def second(timers: single_line(',', int)):
    return total_children(256, 1, tuple(timers))
    
example = '3,4,3,1,2'
