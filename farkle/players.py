from farkle.utilities import DiceCalculator
import farkle.farkle_exceptions as farkle_exceptions

class Player():
  def __init__(self, id):
    self.score = 0
    self.id = id
    
  def add_to_score(self, points):
    self.score += points
      
  def select_dice(self, dice):
    pass
  
  def roll_again(self, current_round_points, num_remaining_dice):
    pass
  

class HumanPlayer(Player):
  def select_dice(self, dice):
    return self.to_tuple(input())
    
  def to_tuple(self, selection):
    if(not self.input_valid(selection)):
      raise farkle_exceptions.InvalidInputError
    selected_dice = []
    for char in selection:
      selected_dice.append(int(char))
    return tuple(selected_dice)
    
  def input_valid(self, selection):
    if (len(selection) == 0):
      return False
    for char in selection:
      if(not self.is_int(char)):
        return False
    return True
    
  def is_int(self, char):
    try:
      int(char)
      return True
    except ValueError:
      return False
    
  def roll_again(self, current_round_points, num_remaining_dice):
    choice = input()
    if(choice.lower() == 'y'):
      return True
    else:
      return False


class ComputerPlayer(Player):
  def __init__(self, id):
    super().__init__(id)
    self.risk_threshold = 50
    
  def select_dice(self, dice):
    return DiceCalculator.get_max_dice_combination(dice)
    
  def roll_again(self, current_round_points, num_remaining_dice):
    risk_metric = current_round_points/(num_remaining_dice**2)
    if(risk_metric < self.risk_threshold):
      return True
    else:
      return False