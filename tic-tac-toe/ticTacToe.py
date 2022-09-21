from array import array


def main():
  '''Main game logic goes here'''
  p1 = []
  p2 = []
  game_end = False
  turns = 0
  print(f'\nWelcome to Tic-Tac-Toe! The only winning move is not playing!')
  while True:
    type = int(input('\n1. 3x3\n2. 5x5\n3. 9x9\nSelect a gamemode: '))
    if type == 1:
      print('You selected a normal game.')
      game_size = 3
    elif type == 2:
      print('You selected a large game.')
      game_size = 5
    elif type == 3:
      print('You selected a huge game.')
      game_size = 9
    # while loop for main game sesion
    while game_end == False:
      print()
      draw_game_area(p1, p2, game_size)
      game_end = game_input(p1, p2, 1, game_size)
      turns += 1
      if turns >= game_size**2:
        # Game is over in 9 turns
        print('\nGame over! Who won?')
        draw_game_area(p1, p2, game_size)
        break
      elif game_end:
        break
      else:
        game_end = False
        print()
      draw_game_area(p1, p2, game_size)
      game_end = game_input(p1, p2, 2, game_size)
      turns += 1
      if turns >= game_size**2:
        # Game is over in 9 turns
        draw_game_area(p1, p2, game_size)
        print('\nGame over! Who won?')
        break
      elif game_end:
        break
      else:
        game_end = False
    break

def sub_player_icon(cell, p1, p2):
  '''Replaces the numbered cell with the icon for either player'''
  if cell in p1:
    icon = 'X'
  elif cell in p2:
    icon = 'O'
  else: 
    icon = cell
  return icon

def draw_game_area(p1: list, p2: list, size: int):
  '''Draw the game board'''
  x = 0
  row = ''
  while x < size**2:
    row = ''
    for n in range(size):
      x += 1
      if (n+1 % size) == size:
        row += f' {sub_player_icon(x, p1, p2):<2}'
      else:
        row += f' {sub_player_icon(x, p1, p2):<2} |'
    print(row)
    print()

def game_input(p1: list, p2: list, player: int, size):
  '''main game logic'''
  while True:
    if player == 1:
      move = input('\nP1 Move(1-9, END): ')
    elif player == 2:
      move = input('\nP2 Move(1-9, END): ')
    # Validate user input for player 1 
    try:
      if move.upper() == 'END':
        return True # Player ends the game
      elif int(move) in p2 or int(move) in p1:
        print('No cheating!')
        break # Player tries to override other player's space
      elif int(move) > size**2:
        print('You did not input a valid move.')
      else:
        if player == 1:
          p1.append(int(move)) # Valid move
        elif player == 2:
          p2.append(int(move)) # Valid move
      break
    except ValueError:
      # Catch when the user does not input a number
      print('You did not input a valid move.')
      break

main()