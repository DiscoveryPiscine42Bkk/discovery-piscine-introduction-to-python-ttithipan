pawn_direction = [(-1, -1), (-1, 1)]
rook_direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
bishop_direction = [(-1, -1), (-1, 1), (1, 1), (1, -1)] #(from 1,1) to 0 0 | 0 2 | 2 2 | 2 0
queen_direction = rook_direction + bishop_direction
king_direction = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
king_in_check = False


def print_board(board):
    for line in board:
        print(line)

def board_checker(board):
    row_count = 0
    board_count = 0
    for row in range(len(board)):
        row_count += 1
        for space in range(len(board[row])):
            board_count += 1
    # print(board_count, row_count) # for checking board size
    if board_count != row_count ** 2:
        print("Invalid Board: Not A Square Board")
        exit()
    else:
        print("Valid Board")

"""
def pawn_move(ori_x, ori_y): # go through
    for dx, dy in pawn_direction:
        i, j = ori_x + dx, ori_y + dy
        if board[i][j] == '.':
            board[i][j] = 'C'
        elif board[i][j] == 'K':
            print("Success")
            exit()
        elif board[i][j] == 'C':
            i += dx
            j += dy
        else:
            break
"""

def pawn_move(board, ori_x, ori_y): # not go through
    for dx, dy in pawn_direction:
        i, j = ori_x + dx, ori_y + dy
        if 0 <= i < len(board) and 0 <= j < len(board[i]):
            if board[i][j] == 'K':
                return True
                # print("Success")
                # exit()
            elif board[i][j] == '.':
                board[i][j] = 'C'

# 4,0 check at 3,1 and 3, 8

def rook_move(board, ori_x, ori_y):
    for dx, dy in rook_direction:
        i, j = ori_x + dx, ori_y + dy
        while 0 <= i < len(board) and 0 <= j < len(board[i]):
            if board[i][j] == '.':
                board[i][j] = 'C'
            elif board[i][j] == 'K':
                return True
                # print("Success")
                # exit()
            elif board[i][j] == 'C':
                i += dx
                j += dy
            else:
                break

def bishop_move(board, ori_x, ori_y):
    for dx, dy in bishop_direction:
        i, j = ori_x + dx, ori_y + dy
        while 0 <= i < len(board) and 0 <= j < len(board[i]):
            if board[i][j] == '.':
                board[i][j] = 'C'
            elif board[i][j] == 'K':
                return True
                # print("Success")
                # exit()
            elif board[i][j] == 'C':
                i += dx
                j += dy
            else:
                break

def queen_move(board, ori_x, ori_y):
    for dx, dy in queen_direction:
        i, j = ori_x + dx, ori_y + dy
        while 0 <= i < len(board) and 0 <= j < len(board[i]):
            if board[i][j] == '.':
                board[i][j] = 'C'
            elif board[i][j] == 'K':
                return True
                # print("Success")
                # exit()
            elif board[i][j] == 'C':
                i += dx
                j += dy
            else:
                break
       
def king_move(board, ori_x, ori_y):
    check_count = 0
    piece_count = 0
    for dx, dy in king_direction:
        i, j = ori_x + dx, ori_y + dy
        if 0 <= i < len(board) and 0 <= j < len(board[i]):
            if board[i][j] == 'C':
                check_count += 1
            elif board[i][j] == '.':
                continue
            elif board[i][j] == 'P' or 'R' or 'B' or 'Q':
                piece_count += 1


    return(check_count, piece_count)


def start_board(board):
    king_count = 0
    pawn_count, rook_count, bishop_count, queen_count = 0, 0, 0, 0
    king_in_check = False
    for row in range(len(board)):
        for space in range(len(board[row])):
            if board[row][space] == 'K':
                king_count += 1
                if king_count != 1:
                    print("Invalid Board: No King Found")
                    exit()
                # continue
            elif board[row][space] == 'R':
                rook_count += 1
                if rook_move(board, row, space):
                    king_in_check = True
            elif board[row][space] == 'B':
                bishop_count += 1
                if bishop_move(board, row, space):
                    king_in_check = True
            elif board[row][space] == 'Q':
                queen_count += 1
                if queen_move(board, row, space):
                    king_in_check = True
            elif board[row][space] == 'P':
                pawn_count += 1
                if pawn_move(board, row, space):
                    king_in_check = True
    print(f"Pawn Count: {pawn_count}\n"
          f"Rook Count: {rook_count}\n"
          f"Bishop Count: {bishop_count}\n"
          f"Queen Count: {queen_count}"
          )
    if king_count == 0:
        print("Invalid Board: No King Found")
        exit()
    if king_in_check:
        print("Success: King is in check")
    else:
        print("King is safe")


def around_king(board):
    for row in range(len(board)):
        for space in range(len(board[row])):
            if board[row][space] == 'K':
                check_count, piece_count = king_move(board, row, space)
    print(f"Check around king: {check_count}\n"
          f"Piece around king: {piece_count}"
          )
    
