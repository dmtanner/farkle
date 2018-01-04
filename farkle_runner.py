from farkle import (game, utilities, players, farkle_exceptions)
import sys, os, pprint

class FarkleRunner():
  
  def __init__(self):
    self.game = game.FarkleGame()
    # self.game.add_player(farkle.HumanPlayer('Marcus'))
    # self.game.add_player(farkle.HumanPlayer('Kyle'))
    self.game.add_player(players.ComputerPlayer('Computer 1'))
    self.game.add_player(players.ComputerPlayer('Computer 2'))
    # self.game.add_player(farkle.ComputerPlayer('Computer 3'))
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
      print('Total Points: ' + str(self.game.get_current_player().score))
      self.play_turn(current_player)
      print('Total Points: ' + str(self.game.get_current_player().score))
      self.game.end_turn()
      if(self.game.has_winner()):
        print('Congratulations, ' + str(self.game.get_winner().id) + ' wins!')
        game_over = True
        
  def play_turn(self, player):
    points = self.run_dice_selection(0, self.MAX_DICE)
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
        selection = self.game.get_current_player().select_dice(dice)
        selected_dice = self.to_tuple(selection)
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
        roll_again = self.game.get_current_player() \
          .roll_again(current_round_points, num_remaining_dice)
        if(roll_again):
          return self.run_dice_selection(current_round_points, num_remaining_dice)
        else:
          return current_round_points
        
      except farkle_exceptions.InvalidInputError:
        print('Invalid input. Try again.')
        
      except farkle_exceptions.InvalidSelectionError:
        print('Invalid dice selected. Try again.')
 
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
      
  def clear_screen(self):
    print('\033[H\033[J')

    
if __name__ == '__main__':
  farkle_runner = FarkleRunner()
  farkle_runner.run_game()