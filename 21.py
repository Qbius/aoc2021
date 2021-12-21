from itertools import count, cycle
from collections import Counter
from functools import cache

def parse(raw_input):
    return tuple(int(line.split(' ')[-1]) - 1 for line in raw_input.split('\n'))

def game(scoreboard, die):
    for turn in count(1):
        roll = sum([next(die), next(die), next(die)])
        player = scoreboard['player1' if turn % 2 == 1 else 'player2']
        player['pos'] += roll
        player['pos'] %= 10
        player['score'] += player['pos'] + 1
        if player['score'] >= 1000:
            return scoreboard, turn

def first(p1pos, p2pos):
    scoreboard, turn = game({'player1': {'pos': p1pos, 'score': 0}, 'player2': {'pos': p2pos, 'score': 0}}, cycle(range(1, 101)))
    scores = list(scoreboard.values())
    scores.sort(key=lambda s: s['score'])
    return scores[0]['score'] * turn * 3

@cache
def game2(p1p, p1s, p2p, p2s, p1first):
    if p1s < 21 and p2s < 21:
        if p1first:
            return sum([game2((p1p + d1 + d2 + d3) % 10, p1s + ((p1p + d1 + d2 + d3) % 10) + 1, p2p, p2s, not p1first) for d1 in range(1, 4) for d2 in range(1, 4) for d3 in range(1, 4)], Counter())
        else:
            return sum([game2(p1p, p1s, (p2p + d1 + d2 + d3) % 10, p2s + ((p2p + d1 + d2 + d3) % 10) + 1, not p1first) for d1 in range(1, 4) for d2 in range(1, 4) for d3 in range(1, 4)], Counter())
    else:
        return Counter({(1 if p1s >= 21 else 2): 1})

def second(p1pos, p2pos):
    return game2(p1pos, 0, p2pos, 0, True).most_common(1)[0][1]

def extra(*_):
    pospairs = [(p1pos, p2pos) for p1pos in range(1, 11) for p2pos in range(1, 11)]
    for p1pos, p2pos in pospairs:
        print(f'P1: {p1pos: >2}, P2: {p2pos: >2}: {first(p1pos - 1, p2pos - 1)}, {second(p1pos - 1, p2pos - 1)}')

example = '''
Player 1 starting position: 4
Player 2 starting position: 8
'''