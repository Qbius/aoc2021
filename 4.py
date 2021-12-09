from itertools import chain

def parse(raw_input):
    all_drawns, *all_boards = raw_input.split('\n\n')
    drawns = list(map(int, all_drawns.split(',')))
    boards = [(list(chain(*[list(map(int, filter(lambda x: x, row.split(' ')))) for row in board.split('\n')])), []) for board in all_boards]
    return drawns, boards

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

def find_last_winning(drawns, boards):
    drawn, *rest_drawns = drawns
    boards = [(board, [*selected, next(i for i, e in enumerate(board) if e == drawn)] if drawn in board else selected) for board, selected in boards]
    losing = [(board, selected) for board, selected in boards if not is_winning(selected)]
    return (drawn, boards[0]) if len(losing) == 0 else find_last_winning(rest_drawns, losing)

def first(inpt):
    drawns, boards = inpt
    last, (board, selected) = find_winning(drawns, boards)
    return last * sum(e for i, e in enumerate(board) if i not in selected)

def second(inpt):
    drawns, boards = inpt
    last, (board, selected) = find_last_winning(drawns, boards)
    return last * sum(e for i, e in enumerate(board) if i not in selected)

example = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 '''