import checkmate

board = '''
R...
.K..
....
....
'''

print(
    checkmate.game_state_iterator(board.split(),
                                  checkmate.check_board_size(board)))
