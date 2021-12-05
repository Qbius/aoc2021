from itertools import chain
from common import raw_input

rows = [[(i + 5 * coeff) for i in range(5)] for coeff in range(5)]
columns = [[(i + 5 * coeff) for coeff in range(5)] for i in range(5)]
def is_winning(selected):
    global rows
    global columns
    return any(all(i in selected for i in section) for section in rows) or any(all(i in selected for i in section) for section in columns)
    
def find_winning(drawns, boards):
    drawn, *rest_drawns = drawns
    boards = [(board, [*selected, next(i for i, e in enumerate(board) if e == drawn)] if drawn in board else selected) for board, selected in boards]
    winning = [(board, selected) for board, selected in boards if is_winning(selected)]
    return (drawn, winning[0]) if len(winning) > 0 else find_winning(rest_drawns, boards)

def first(base: raw_input):
    all_drawns, *all_boards = base.split('\n\n')
    drawns = list(map(int, all_drawns.split(',')))
    boards = [(list(chain(*[list(map(int, filter(lambda x: x, row.split(' ')))) for row in board.split('\n')])), []) for board in all_boards]
    last, (board, selected) = find_winning(drawns, boards)
    return last * sum(e for i, e in enumerate(board) if i not in selected)

def find_winning_continuous(drawns, boards):
    drawn, *rest_drawns = drawns
    boards = [(board, [*selected, next(i for i, e in enumerate(board) if e == drawn)] if drawn in board else selected) for board, selected in boards]
    losing = [(board, selected) for board, selected in boards if not is_winning(selected)]
    return (drawn, boards[0]) if len(losing) == 0 else find_winning_continuous(rest_drawns, losing)  

def second(base: raw_input):
    all_drawns, *all_boards = base.split('\n\n')
    drawns = list(map(int, all_drawns.split(',')))
    boards = [(list(chain(*[list(map(int, filter(lambda x: x, row.split(' ')))) for row in board.split('\n')])), []) for board in all_boards]
    last, (board, selected) = find_winning_continuous(drawns, boards)
    return last * sum(e for i, e in enumerate(board) if i not in selected)