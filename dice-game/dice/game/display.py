# source code for the repsctively named functions in die.py
def display_dice_col(rolled: str) -> str:
  '''
  Creates a graphical ascii art representation of the dice rolled based on the values given.

  parameters:
    rolled; a string formatted 'x x x x x' where x is a dice value
  return: a string that represents the dice
  '''
  # a dictionary holds the individual rows for a given value rather than a multiline string
  dice = [
      [' ,--------.', ",.......,'|", '|       | |', '|   0   | |', "|       |,'", "`'''''''`"], # 1
      [' ,--------.', ",.......,'|", '|   0   | |', '|       | |', "|   0   |,'", "`'''''''`"], # 2
      [' ,--------.', ",.......,'|", '|   0   | |', '|   0   | |', "|   0   |,'", "`'''''''`"], # 3
      [' ,--------.', ",.......,'|", '| 0   0 | |', '|       | |', "| 0   0 |,'", "`'''''''`"], # 4
      [' ,--------.', ",.......,'|", '| 0   0 | |', '|   0   | |', "| 0   0 |,'", "`'''''''`"], # 5
      [' ,--------.', ",.......,'|", '| 0   0 | |', '| 0   0 | |', "| 0   0 |,'", "`'''''''`"] # 6
  ]
  # initialize variables and format the values string as a list
  out = ''
  rolled.strip()
  rolled = rolled.split(' ')
  # remove the last space so there are only dice values
  rolled.pop()
  # build each dice 
  for i in rolled:
      for value in dice[int(i)-1]:
          out += f'{value}\n'
  return out

def display_dice_row(rolled: str) -> str:
  '''
  Creates a graphical ascii art representation of the dice rolled based on the values given.

  parameters:
    rolled; a string formatted 'x x x x x' where x is a dice value
  return: a string that represents the dice
  '''
  dice = [
    ['|       | |', '|   0   | |', "|       |,'"], # 1
    ['|   0   | |', '|       | |', "|   0   |,'"], # 2
    ['|   0   | |', '|   0   | |', "|   0   |,'"], # 3
    ['| 0   0 | |', '|       | |', "| 0   0 |,'"], # 4
    ['| 0   0 | |', '|   0   | |', "| 0   0 |,'"], # 5
    ['| 0   0 | |', '| 0   0 | |', "| 0   0 |,'"] # 6
  ]
  out = ''
  rolled.strip()
  rolled = rolled.split(' ')
  # remove the last space so there are only dice values
  rolled.pop()
  # assign each graphical die a 
  die_one = dice[int(rolled[0])-1]
  die_two = dice[int(rolled[1])-1]
  die_three = dice[int(rolled[2])-1]
  die_four = dice[int(rolled[3])-1]
  die_five = dice[int(rolled[4])-1]

  out = f""" ,--------.  ,--------.  ,--------.  ,--------.  ,--------.
,.......,'| ,.......,'| ,.......,'| ,.......,'| ,.......,'|
{die_one[0]} {die_two[0]} {die_three[0]} {die_four[0]} {die_five[0]}
{die_one[1]} {die_two[1]} {die_three[1]} {die_four[1]} {die_five[1]}
{die_one[2]} {die_two[2]} {die_three[2]} {die_four[2]} {die_five[2]}
`'''''''`   `'''''''`   `'''''''`   `'''''''`   `'''''''`"""
  return out