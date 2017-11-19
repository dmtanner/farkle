import random
from collections import Counter


class FarkleRunner():
  def __init__(self):
    self.farkle = FarkleGame()
    
  def run_game(self):
    print('Welcome to Farkle!\nStart?')
    game_over = False
    while(not game_over):
      current_round_points = 0
      dice = self.farkle.roll_dice()
      self.select_dice(dice)
      game_over = True
 
  def select_dice(self, dice):
      print('Dice: ' + str(dice))
      print('Choose dice to save:')
      combinations = self.farkle.get_dice_combinations(dice)
      for i, combo in enumerate(combinations):
        print(i+1, end='. ')
        print(combo, end='   ')
        print(combinations[combo], end=' ')
        print('points')
      
      try:
        number_selected = int(input())
        selected_combination = combinations[number_selected - 1]
        selected_dice = selected_combination[0]
        current_round_points += selected_combination[1]
        remaining_dice = farkle.remove_selected_dice(dice, selected_dice)
        remaining_dice
        
        print(current_round_points)
      except:
        raise
        print('Invalid selection, try again.')
        
        
class FarkleGame():
  def __init__(self):
    self.players = {}
    self.players[0] = Player(0)
    # self.players.append(ComputerPlayer(1))
    
  def roll_dice(self):
    dice = []
    for i in range(6):
      dice.append(random.randint(1,6))
    dice.sort()
    return tuple(dice)
    
  def add_to_score(self, player_id, points):
    self.players[player_id].add_to_score(points)
    
  def get_player_score(self, player_id):
    return self.players[player_id].score
  
  def has_straight(self, dice):
    if((1 in dice and 2 in dice and 3 in dice
        and 4 in dice and 5 in dice and 6 in dice)):
      return dice
    else:
      return False
    
  def has_three_pair(self, dice):
    die_count = Counter(dice)
    die_count_values = list(die_count.values())
    if(len(dice) == 6 and min(die_count_values) >= 2):
      return dice
    else:
      return False
      
  def has_three_of_a_kind(self, dice):
    if(dice.count(1) >= 3):
      return (1,1,1)
    if(dice.count(6) >= 3):
      return (6,6,6)
    if(dice.count(5) >= 3):
      return (5,5,5)
    if(dice.count(4) >= 3):
      return (4,4,4)
    if(dice.count(3) >= 3):
      return (3,3,3)
    if(dice.count(2) >= 3):
      return (2,2,2)
    return False
    
  def has_one(self, dice):
    if(1 in dice):
      return (1,)
    else:
      return False
    
  def has_five(self, dice):
    if(5 in dice):
      return (5,)
    else:
      return False
    
  def get_dice_combinations(self, dice):
    combinations = {}
    
    if(self.has_straight(dice)):
      combinations[self.has_straight(dice)] = 3000
    if(self.has_three_pair(dice)):
      combinations[self.has_three_pair(dice)] = 1500
    if(self.has_three_of_a_kind(dice)):
      three_of_a_kind = self.has_three_of_a_kind(dice)
      points = 0
      if(three_of_a_kind[0] == 1):
        points = 1000
      else:
        points = three_of_a_kind[0] * 100
      combinations[three_of_a_kind] = points
    if(self.has_one(dice)):
      combinations[self.has_one(dice)] = 100
    if(self.has_five(dice)):
      combinations[self.has_five(dice)] = 50
      
    # sort combos by point value
    # combinations = {(key, combinations[key]) for key in sorted(
    #                 combinations, key=combinations.get, reverse=True)}
    return combinations
    
  def remove_selected_dice(self, initial_dice, dice_to_remove):
    dice = list(initial_dice)
    try:
      for die in dice_to_remove:
        dice.remove(die)
    except:
      print('die not contained in set')
      
    return tuple(dice)
    
    
class Player():
  def __init__(self, id):
    self.id = id
    self.score = 0
    
  def add_to_score(self, points):
    self.score += points
    

if __name__ == '__main__':
  farkle = FarkleRunner()
  farkle.run_game()