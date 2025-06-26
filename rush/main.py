import checkmate
import sys

example_board = '''\
..P..
.....
..K..
...R.
.....\
''' 

def create_board(example_board):
    board = example_board.strip().splitlines()
    board = [list(row) for row in board]
    return board

if len(sys.argv) == 1:
    board = create_board(example_board)
    checkmate.start_board(board)
    checkmate.board_checker(board)
    checkmate.print_board(board)
    checkmate.around_king(board)
else:
    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            content = f.read()
            start = content.find("\\")
            stop = content.find("\\", start + 1)
            between = content[start + 1:stop]
        board = create_board(between)
        checkmate.start_board(board)
        checkmate.board_checker(board)
        checkmate.print_board(board)
        checkmate.around_king(board)