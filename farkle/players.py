from farkle.utilities import DiceCalculator

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
    return input()
    
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