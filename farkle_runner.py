import farkle
import sys, os, pprint

class FarkleRunner():
  
  def __init__(self):
    self.farkle = farkle.FarkleGame()
    self.farkle.add_player(farkle.HumanPlayer('ME!'))
    self.farkle.add_player(farkle.ComputerPlayer('Comp 2'))
    self.current_round_points = 0
    self.MAX_DICE = 6
  
  def run_game(self):
    print('Welcome to Farkle!')
    game_over = False
    round = 0
    while(not game_over):
      round += 1
      print('Round ' + str(round))
      current_player = self.farkle.get_current_player()
      print('\nPlayer: ' + str(current_player.id))
      self.play_turn(current_player)
      print('Total Points: ' + str(self.farkle.get_current_player().score))
      self.farkle.end_turn()
      if(self.farkle.has_winner()):
        print('Congratulations, ' + str(self.farkle.get_winner().id) + ' wins!')
        game_over = True
        
    return round
  
  def play_turn(self, player):
    self.current_round_points = 0
    points = self.run_dice_selection(self.MAX_DICE)
    print('round points:' + str(points))
    player.add_to_score(points)
  
  def run_dice_selection(self, num_dice_to_roll):
    dice = self.farkle.roll_dice(num_dice_to_roll)
    while(True):
      try:
        print('Dice Rolled: ' + str(dice))
        if(self.farkle.is_farkle(dice)):
          print('FARKLE!')
          return 0
        print('Enter dice to save:')
        selection = self.farkle.get_current_player().select_dice(dice)
        selected_dice = self.to_tuple(selection)
        print('Selected dice: ' + str(selected_dice))
        if(not self.farkle.selection_valid(selected_dice, dice)):
          raise farkle.InvalidSelectionError
        self.current_round_points += self.farkle.calculate_dice_points(selected_dice)
        print('Roll points: ' + str(self.current_round_points))
        num_remaining_dice = len(dice) - len(selected_dice)
        if(num_remaining_dice == 0):
          num_remaining_dice = self.MAX_DICE
        print('Number of dice remaining: ' + str(num_remaining_dice))
        print('Roll again? (y/n)')
        roll_again = self.farkle.get_current_player() \
          .roll_again(self.current_round_points, num_remaining_dice)
        if(roll_again):
          # turn_over = False
          return self.run_dice_selection(num_remaining_dice)
        else:
          return self.current_round_points
        
      except farkle.InvalidInputError:
        print('Invalid input. Try again.')
        
      except farkle.InvalidSelectionError:
        print('Invalid dice selected. Try again.')
 
  def to_tuple(self, selection):
    if(not self.input_valid(selection)):
      raise farkle.InvalidInputError
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
      
  def clear_screen(self):
    print('\033[H\033[J')

    
if __name__ == '__main__':
  farkle_runner = FarkleRunner()
  farkle_runner.run_game()