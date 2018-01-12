import random
from farkle.utilities import DiceCalculator
from farkle.players import *

class FarkleGame():
  def __init__(self):
    self.players = []
    self.current_player_turn = 0
    self.round = 1
    self.WINNING_SCORE = 10000
    
  def add_player(self, player):
    self.players.append(player)
    
  def add_computer_player(self, id):
    self.add_player(ComputerPlayer(id))
    
  def add_human_player(self, id):
    self.add_player(HumanPlayer(id))
    
  def get_current_player(self):
    return self.players[self.current_player_turn]
  
  def end_turn(self):
    self.current_player_turn += 1
    if(self.current_player_turn >= len(self.players)):
      self.current_player_turn = 0
      self.round += 1
    
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
  
  def get_selected_dice(self, dice):
    return self.get_current_player().select_dice(dice)
  
  def get_roll_again(self, current_round_points, num_remaining_dice):
    return self.get_current_player().roll_again(current_round_points, num_remaining_dice)
    
  def selection_valid(self, selected_dice, all_dice):
    for die in selected_dice:
      if(die not in all_dice):
        return False
    return True
    
  def has_winner(self):
    for player in self.players:
      if(player.score >= self.WINNING_SCORE):
        return True
        
  def get_winner(self):
    for player in self.players:
      if(player.score >= self.WINNING_SCORE):
        return player
        
  def is_farkle(self, dice):
    return DiceCalculator.is_farkle(dice)
    
  def calculate_dice_points(self, selected_dice):
    return DiceCalculator.calculate_dice_points(selected_dice)