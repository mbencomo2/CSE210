import math
from operator import truediv

def main():
  '''Main game logic goes here'''
  print(f'\nWelcome to Tic-Tac-Toe! The only winning move is not playing!')
  try:
    type = int(input('\n1. 3x3\n2. 5x5\n3. 6x6\nSelect a gamemode: '))
    if type == 1:
      print('You selected a normal game.')
      size = 3
      print()
    elif type == 2:
      print('You selected a large game.')
      size = 5
      print()
    elif type == 3:
      print('You selected a huge game.')
      size = 6
      print()
    else:
      raise ValueError
    game_board = create_board(size)
    is_game_end = False
    player = get_player('')
    while is_game_end == False:
      draw_game_area(game_board)
      if get_player_input(game_board, player):
        break
      elif is_over(game_board, player):
        break
      elif is_draw(game_board):
        break
      player = get_player(player)
  except ValueError:
    print('That is not a valid game type!')

def create_board(size: int) -> dict:
  board = {}
  row = []
  ROW_INDEX = 0
  for x in range(size**2):
    if (x+1) % size == 0:
      row.append(x)
      board[ROW_INDEX] = row
      row = []
      ROW_INDEX += 1
    else:
      row.append(x)
  return board

def draw_game_area(board: dict):
  '''
  Draw the game board, with fancy spacing characters.

  parameters:
    board: a dictionary that contains the game state
  return: none
  '''
  line  = ''
  spacer = ''
  size = len(board)
  for x in range(size):
    if (x + 1) % size == 0:
      spacer += '----'
    else:
      spacer += '----+'
  print(spacer)
  for x, y in board.items():
    row = board[x]
    for cell in range(size):
      if (cell + 1) % size == 0:
        line += f' {row[cell]:<2}'
      else:
        line += f' {row[cell]:<2} |'
      if (cell + 1) % size == 0:
        print(line)
        print(spacer)
        line = ''
  print()

def get_player(player: str = '') -> str:
  '''
  Returns the next player to make a move.
  
  parameters:
    player: the previous player, the default empty string results in 'x' starting first
  return: player string ('x' or 'o')
  '''
  if player == '' or player == 'o':
    return 'x'
  else:
    return 'o'

def get_player_input(board: dict, player) -> bool:
  '''
  Gets the player's input and stores it in the board. This function also
  allows the user to end the game by returning a bool when END is typed.

  parameters:
    board: a dictionary that contains the game state
    player: the current player, as a string
  return: bool (True)
  '''
  max = len(board)**2
  while True:
    try:
      loc = input(f"{player}'s turn, pick a number from 0 to {max}, or type END: ")
      if loc.upper() == 'END':
        print('\nSo long, and thanks for all the fish!')
        return True
      elif int(loc) >= max and not loc in board.values():
        print('That space does not exist')
      else:
        for key, value in board.items():
          if int(loc) in value:
            row = board[key]
            row[row.index(int(loc))] = player
      break
    except ValueError:
      print('Invalid entry, please try again')
    except UnboundLocalError:
      print('That is an invalid move!')


def is_over(board: dict, player: str) -> bool:
  '''
  Checks the rows, then columns, then diagonal for a tic-tac-toe

  parameters:
    board: dictionary containing the game state
    player: the current player
  '''
  size = len(board)
  # Check rows
  for key in board.keys():
    row = board[key]
    if row.count('x') == len(board):
      print(f'\nThat is the game! {player} wins.')
      draw_game_area(board)
      return True
    elif row.count('o') == size:
      print(f'\nThat is the game! {player} wins.')
      draw_game_area(board)
      return True
  # Check Columns
  for x in range(size):
    col = []
    for y in range(size):
      row = board[y]
      col.append(row[x])
    if col.count(player) == size:
      print(f'That is the game! {player} wins.')
      draw_game_area(board)
      return True
  # Check diagonal #1
  diagonal = []
  for x in range(size):
    diagonal.append((size+1)*x)
  temp = []
  row = []
  for key, value in board.items():
    temp = board[key]
    for x in range(size):
      row.append(temp[x])
  for value in diagonal:
    diagonal[diagonal.index(value)] = row[value]
    if diagonal.count('x') == len(board):
      print(f'\nThat is the game! {player} wins.')
      draw_game_area(board)
      return True
  # Check diagonal #2
  diagonal = []
  for x in range(size):
    diagonal.append((size-1)*(x+1))
  temp = []
  row = []
  for key, value in board.items():
    temp = board[key]
    for x in range(size):
      row.append(temp[x])
  for value in diagonal:
    diagonal[diagonal.index(value)] = row[value]
    if diagonal.count(player) == len(board):
      print(f'\nThat is the game! {player} wins.')
      draw_game_area(board)
      return True


def is_draw(board: dict, player: str) -> bool:
  '''
  Checks to make sure all the cells are filled, before declaring a draw.
  
  parameters:
    board: dictionary containing game state
  return: bool
  '''
  size = len(board)
  row = []
  for key, value in board.items():
    temp = board[key]
    for x in range(size):
      row.append(temp[x])
  for value in row:
    if value == 'x' or value == 'o':
      continue
    else:
      return False
  print(f"\nCat's game! No winners.")
  draw_game_area(board)
  return True


if __name__ == '__main__':
  main()