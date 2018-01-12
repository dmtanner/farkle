from farkle import (game, farkle_exceptions)
import sys, os, pprint

class FarkleRunner():
  
  def __init__(self):
    self.game = game.FarkleGame()
    self.game.add_computer_player('Computer 1')
    self.game.add_computer_player('Computer 2')
    self.MAX_DICE = 6
  
  def run_game(self):
    print('Welcome to Farkle!')
    game_over = False
    round = 0
    while(not game_over):
      round += 1
      print('\n---Round ' + str(round) + '---')
      current_player = self.game.get_current_player()
      print('Player: ' + str(current_player.id))
      print('Score: ' + str(current_player.score))
      self.play_turn(current_player)
      print('Score: ' + str(current_player.score))
      self.game.end_turn()
      if(self.game.has_winner()):
        print('Congratulations, ' + str(self.game.get_winner().id) + ' wins!')
        game_over = True
        
  def play_turn(self, player):
    current_round_points = 0
    points = self.run_dice_selection(current_round_points, self.MAX_DICE)
    print('Round points:' + str(points))
    player.add_to_score(points)
  
  def run_dice_selection(self, current_round_points, num_dice_to_roll):
    dice = self.game.roll_dice(num_dice_to_roll)
    while(True):
      try:
        print('Dice Rolled: ' + str(dice))
        if(self.game.is_farkle(dice)):
          print('FARKLE!')
          return 0
        print('Enter dice to save:')
        selected_dice = self.game.get_selected_dice(dice)
        print('Selected dice: ' + str(selected_dice))
        if(not self.game.selection_valid(selected_dice, dice)):
          raise farkle_exceptions.InvalidSelectionError
        current_round_points += self.game.calculate_dice_points(selected_dice)
        print('Roll points: ' + str(current_round_points))
        num_remaining_dice = len(dice) - len(selected_dice)
        if(num_remaining_dice == 0):
          num_remaining_dice = self.MAX_DICE
        print('Number of dice remaining: ' + str(num_remaining_dice))
        print('Roll again? (y/n)')
        roll_again = self.game.get_roll_again(current_round_points, num_remaining_dice)
        if(roll_again):
          return self.run_dice_selection(current_round_points, num_remaining_dice)
        else:
          return current_round_points
        
      except farkle_exceptions.InvalidInputError:
        print('Invalid input. Try again.')
        
      except farkle_exceptions.InvalidSelectionError:
        print('Invalid dice selected. Try again.')
      
  def clear_screen(self):
    print('\033[H\033[J')

    
if __name__ == '__main__':
  farkle_runner = FarkleRunner()
  farkle_runner.run_game()