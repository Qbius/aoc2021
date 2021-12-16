from itertools import repeat
from functools import cache
import sys
sys.setrecursionlimit(10000)

def parse(raw_input):
    return [tuple(map(int, line)) for line in raw_input.split('\n')]

@cache
def risk_level(h, w, board):
    width, height = len(board[0]), len(board)
    risklevels = [risk_level(h + hh, w + ww, board) for hh, ww in [(0, 1), (1, 0)] if (h + hh) < height and (w + ww) < width]
    return board[h][w] + (min(risklevels) if risklevels else 0)

def first(board):
    return risk_level(0, 0, tuple(board)) - board[0][0]

@cache
def risk_level_2(h, w, board):
    width, height = len(board[0]), len(board)
    risklevels = [risk_level_2(h + hh, w + ww, board) for hh, ww in [(0, 1), (1, 0)] if (h + hh) < height and (w + ww) < width]
    if h == w: print(h, w)
    return board[h][w] + (min(risklevels) if risklevels else 0)

def shift(number, n):
    return (number + n) % 10 + 1 if (number + n) > 9 else (number + n)

def second(board):
    width, height = len(board[0]), len(board)
    new_board = tuple(tuple(shift(board[h][w], th + tw) for tw in range(5) for w in range(width)) for th in range(5) for h in range(height))
    return risk_level_2(0, 0, tuple(new_board)) - new_board[0][0]

example = '''
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''
