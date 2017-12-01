import random
from collections import Counter
        
      
class FarkleGame():
  def __init__(self):
    self.players = {}
    self.players[0] = HumanPlayer(0)
    self.players[1] = HumanPlayer(1)
    self.current_player_turn = 0
    self.WINNING_SCORE = 10000
    # self.players.append(ComputerPlayer(1))
    
  def get_current_player(self):
    return self.players[self.current_player_turn]
  
  def end_turn(self):
    self.current_player_turn += 1
    if(self.current_player_turn >= len(self.players)):
      self.current_player_turn = 0
    
  def roll_dice(self, num_dice):
    dice = []
    for i in range(num_dice):
      dice.append(random.randint(1,6))
    dice.sort()
    return tuple(dice)
    
  def add_to_score(self, player_id, points):
    self.players[player_id].add_to_score(points)
    
  def get_player_score(self, player_id):
    return self.players[player_id].score
    
  def selection_valid(self, selected_dice, all_dice):
    for die in selected_dice:
      if(die not in all_dice):
        return False
    if(self.is_farkle(selected_dice)):
      return False
    return True
  
  def is_farkle(self, dice):
    return len(self.get_dice_combinations(dice)) == 0
    
  def has_winner(self):
    for id, player in self.players.items():
      if(player.score >= self.WINNING_SCORE):
        return True
        
  def get_winner(self):
    for id, player in self.players.items():
      if(player.score >= self.WINNING_SCORE):
        return player
    
  def has_straight(self, dice):
    if((1 in dice and 2 in dice and 3 in dice
        and 4 in dice and 5 in dice and 6 in dice)):
      return dice
    else:
      return False
    
  def has_three_pair(self, dice):
    die_count = Counter(dice)
    if(len(dice) == 6 
        and self.numbers_are_even(die_count.values())):
      return dice
    else:
      return False
  
  def numbers_are_even(self, values):
    for value in values:
      if(value % 2 != 0):
        return False
    return True
      
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
    
  def calculate_dice_points(self, dice):
    points = 0
    
    if(self.has_straight(dice)):
      points += 3000
      dice = self.remove_selected_dice(dice, self.has_straight(dice))
    elif(self.has_three_pair(dice)):
      points += 1500
      dice = self.remove_selected_dice(dice, self.has_three_pair(dice))
    elif(self.has_three_of_a_kind(dice)):
      three_of_a_kind = self.has_three_of_a_kind(dice)
      if(three_of_a_kind[0] == 1):
        points += 1000
      else:
        points += three_of_a_kind[0] * 100
      dice = self.remove_selected_dice(dice, self.has_three_of_a_kind(dice))
    elif(self.has_one(dice)):
      points += 100
      dice = self.remove_selected_dice(dice, self.has_one(dice))
    elif(self.has_five(dice)):
      points += 50
      dice = self.remove_selected_dice(dice, self.has_five(dice))
    else:
      raise InvalidSelectionError
      
    if(len(dice) == 0):
      return points
    else:
      return points + self.calculate_dice_points(dice)
      
    
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
    self.score = 0
    self.id = id
    
  def add_to_score(self, points):
    self.score += points
    
  def select_dice(self, dice):
    return (3,3,3)
    

class HumanPlayer(Player):
  def select_dice(self, dice):
    return input()
    

class InvalidInputError(Exception):
  pass

class InvalidSelectionError(Exception):
  pass