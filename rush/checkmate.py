def check_board_size(board_as_string):
  for row in board_as_string.split():
    if len(row) != len(board_as_string.split()):
      return "Invalid board size"
  return len(board_as_string.split())
#If valid board size, return size, else return invalid board size.

def game_state_iterator(board, size):
  try:
    size = int(size)
    record = []
    for rows in range(0, size):
      for columns in range(0, size):
        if board[rows][columns] == "P":
          record.append(pawn_attack_pattern(board, rows, columns, size))
        elif board[rows][columns] in ["R", "Q"]:
          record.append(rook_attack_pattern(board, rows, columns, size))
        elif board[rows][columns] in ["B", "Q"]:
          record.append(bishop_attack_pattern(board, rows, columns, size))
    if True in record:
      return "Success"
    else:
      return "Fail"
  except ValueError:
    return "Invalid board size"

def pawn_attack_pattern(board, rows, columns, size):
  if rows == 0:
    return False
  if columns > 0:
    if board[rows - 1][columns - 1] == "K":
      return True
  if columns < size - 1:  #minus 1 because we start from 0 to 7, meaning board size 8.
    if board[rows - 1][columns + 1] == "K":
      return True
  return False
#Pawn attack pattern is done.
def rook_attack_pattern(board, rows, columns, size):
  obstacle = False
  for checker in range(1, size):
    if columns + checker < size:
      if board[rows][columns + checker] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows][columns + checker] == "K" and not obstacle:
          return True
  obstacle = False
  for checker in range(1, size):
    if columns - checker >= 0:
      if board[rows][columns - checker] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows][columns - checker] == "K" and not obstacle:
          return True
  obstacle = False
  for checker in range(1, size):
    if rows + checker < size:
      if board[rows + checker][columns] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows + checker][columns] == "K" and not obstacle:
          return True
  obstacle = False
  for checker in range(1, size):
    if rows - checker >= 0:
      if board[rows - checker][columns] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows - checker][columns] == "K" and not obstacle:
          return True
  return False
#Rook attack pattern is done.
def bishop_attack_pattern(board, rows, columns, size):
  obstacle = False
  for checker in range(1, size):
    if columns + checker < size and rows + checker < size:
      if board[rows + checker][columns + checker] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows + checker][columns + checker] == "K" and not obstacle:
          return True
  obstacle = False
  for checker in range(1, size):
    if columns - checker >= 0 and rows - checker >= 0:
      if board[rows - checker][columns - checker] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows - checker][columns - checker] == "K" and not obstacle:
          return True
  obstacle = False
  for checker in range(1, size):
    if columns + checker < size and rows - checker >= 0:
      if board[rows - checker][columns + checker] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows - checker][columns + checker] == "K" and not obstacle:
          return True
  obstacle = False
  for checker in range(1, size):
    if columns - checker >= 0 and rows + checker < size:
      if board[rows + checker][columns - checker] in ["Q", "R", "B", "P"]:
        obstacle = True
      else:
        if board[rows + checker][columns - checker] == "K" and not obstacle:
          return True
  return False
#Bishop attack pattern is done.