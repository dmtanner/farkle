from collections import Counter
import farkle.farkle_exceptions

class DiceCalculator():
  @staticmethod
  def is_farkle(dice):
    return len(DiceCalculator.get_max_dice_combination(dice)) == 0
    
  @staticmethod
  def has_straight(dice):
    if((1 in dice and 2 in dice and 3 in dice
        and 4 in dice and 5 in dice and 6 in dice)):
      return dice
    else:
      return False
    
  @staticmethod
  def has_three_pair(dice):
    die_count = Counter(dice)
    if(len(dice) == 6 
        and DiceCalculator.numbers_are_even(die_count.values())):
      return dice
    else:
      return False
  
  @staticmethod
  def numbers_are_even(values):
    for value in values:
      if(value % 2 != 0):
        return False
    return True
  
  @staticmethod    
  def has_three_of_a_kind(dice):
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
  
  @staticmethod 
  def has_one(dice):
    if(1 in dice):
      return (1,)
    else:
      return False
  
  @staticmethod  
  def has_five(dice):
    if(5 in dice):
      return (5,)
    else:
      return False
  
  @staticmethod  
  def get_max_dice_combination(dice):
    
    if(DiceCalculator.has_straight(dice)):
      return DiceCalculator.get_remaining_dice_combinations(dice, DiceCalculator.has_straight(dice))
    if(DiceCalculator.has_three_pair(dice)):
      return DiceCalculator.get_remaining_dice_combinations(dice, DiceCalculator.has_three_pair(dice))
    if(DiceCalculator.has_three_of_a_kind(dice)):
      return DiceCalculator.get_remaining_dice_combinations(dice, DiceCalculator.has_three_of_a_kind(dice))
    if(DiceCalculator.has_one(dice)):
      return DiceCalculator.get_remaining_dice_combinations(dice, DiceCalculator.has_one(dice))
    if(DiceCalculator.has_five(dice)):
      return DiceCalculator.get_remaining_dice_combinations(dice, DiceCalculator.has_five(dice))
      
    return []
  
  @staticmethod  
  def get_remaining_dice_combinations(all_dice, used_dice):
    remaining_dice = DiceCalculator.remove_selected_dice(all_dice, used_dice)
    remaining_combinations = DiceCalculator.get_max_dice_combination(remaining_dice)
    if(len(remaining_combinations) > 0):
      return used_dice + remaining_combinations
    else:
      return used_dice
    
  @staticmethod  
  def calculate_dice_points(dice):
    points = 0
    
    if(DiceCalculator.has_straight(dice)):
      points += 3000
      dice = DiceCalculator.remove_selected_dice(dice, DiceCalculator.has_straight(dice))
    elif(DiceCalculator.has_three_pair(dice)):
      points += 1500
      dice = DiceCalculator.remove_selected_dice(dice, DiceCalculator.has_three_pair(dice))
    elif(DiceCalculator.has_three_of_a_kind(dice)):
      three_of_a_kind = DiceCalculator.has_three_of_a_kind(dice)
      if(three_of_a_kind[0] == 1):
        points += 1000
      else:
        points += three_of_a_kind[0] * 100
      dice = DiceCalculator.remove_selected_dice(dice, DiceCalculator.has_three_of_a_kind(dice))
    elif(DiceCalculator.has_one(dice)):
      points += 100
      dice = DiceCalculator.remove_selected_dice(dice, DiceCalculator.has_one(dice))
    elif(DiceCalculator.has_five(dice)):
      points += 50
      dice = DiceCalculator.remove_selected_dice(dice, DiceCalculator.has_five(dice))
    else:
      raise farkle.farkle_exceptions.InvalidSelectionError
      
    if(len(dice) == 0):
      return points
    else:
      return points + DiceCalculator.calculate_dice_points(dice)
  
  @staticmethod    
  def remove_selected_dice(initial_dice, dice_to_remove):
    dice = list(initial_dice)
    try:
      for die in dice_to_remove:
        dice.remove(die)
    except:
      print('die not contained in set')
      
    return tuple(dice)