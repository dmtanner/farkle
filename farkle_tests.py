import unittest
from farkle.game import FarkleGame
from farkle.players import HumanPlayer
from farkle.farkle_exceptions import *
from farkle.utilities import DiceCalculator

class TestFarkleGame(unittest.TestCase):
  def setUp(self):
    self.farkle = FarkleGame()
    self.farkle.add_player(HumanPlayer('Human Player'))
    
  def test_roll(self):
    dice = self.farkle.roll_dice(6)
    self.assertEqual(len(dice), 6)
    for die in dice:
      self.assertGreaterEqual(die, 1)
      self.assertLessEqual(die, 6)
      
    dice = self.farkle.roll_dice(3)
    self.assertEqual(len(dice), 3)
      
  def test_player_score(self):
    self.farkle.add_to_score(0, 300)
    self.assertEqual(self.farkle.get_player_score(0), 300)
    
  def test_gameplay_output(self):
    return 0
    


class TestFarkleUtilities(unittest.TestCase):
    
  def test_straight(self):
    dice = (1,2,3,4,5,6)
    self.assertTrue(DiceCalculator.has_straight(dice))
    self.assertEqual(DiceCalculator.has_straight(dice), dice)
    dice = (1,1,1,6,6,6)
    self.assertFalse(DiceCalculator.has_straight(dice))
    dice = (1,2,3,4)
    self.assertFalse(DiceCalculator.has_straight(dice))
    dice = (1,)
    self.assertFalse(DiceCalculator.has_straight(dice))
    
  def test_three_pair(self):
    dice = (1,1,2,2,3,3)
    self.assertTrue(DiceCalculator.has_three_pair(dice))
    self.assertEqual(DiceCalculator.has_three_pair(dice), dice)
    dice = (1,1,1,1,3,3)
    self.assertTrue(DiceCalculator.has_three_pair(dice))
    self.assertEqual(DiceCalculator.has_three_pair(dice), dice)
    dice = (1,1,1,1,1,1)
    self.assertTrue(DiceCalculator.has_three_pair(dice))
    self.assertEqual(DiceCalculator.has_three_pair(dice), dice)
    dice = (1,1,2,2,3,4)
    self.assertFalse(DiceCalculator.has_three_pair(dice))
    dice = (1,1,2,2)
    self.assertFalse(DiceCalculator.has_three_pair(dice))
    dice = (1,)
    self.assertFalse(DiceCalculator.has_three_pair(dice))
    
  def test_three_of_a_kind(self):
    dice = (1,1,1,2,3,4)
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice))
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,1,1,1,1)
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice))
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,1,2,2,2)
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice))
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,1)
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice))
    self.assertTrue(DiceCalculator.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,2,2,3,4)
    self.assertFalse(DiceCalculator.has_three_of_a_kind(dice))
    dice = (1,)
    self.assertFalse(DiceCalculator.has_three_of_a_kind(dice))
  
  def test_one(self):
    dice = (1,1,1,2,3,4)
    self.assertTrue(DiceCalculator.has_one(dice))
    dice = (1,)
    self.assertTrue(DiceCalculator.has_one(dice))
    self.assertEqual(DiceCalculator.has_one(dice), (1,))
    dice = (2,3,4,5,6,6)
    self.assertFalse(DiceCalculator.has_one(dice))
    
  def test_five(self):
    dice = (1,2,3,4,5,6)
    self.assertTrue(DiceCalculator.has_five(dice))
    self.assertEqual(DiceCalculator.has_five(dice), (5,))
    dice = (1,2,5,5,5,6)
    self.assertTrue(DiceCalculator.has_five(dice))
    self.assertEqual(DiceCalculator.has_five(dice), (5,))
    dice = (5,)
    self.assertTrue(DiceCalculator.has_five(dice))
    self.assertEqual(DiceCalculator.has_five(dice), (5,))
    dice = (1,2,3,4,6,6)
    self.assertFalse(DiceCalculator.has_five(dice))
    
  def test_max_dice_combination(self):
    dice = (1,5)
    combination = DiceCalculator.get_max_dice_combination(dice)
    self.assertTrue(set((1,5)).issubset(combination))
    
    dice = (1,1,3,3,5,5)
    combination = DiceCalculator.get_max_dice_combination(dice)
    self.assertTrue(set((1,1,3,3,5,5)).issubset(combination))
    
    dice = (1,1,1,2,3,4)
    combination = DiceCalculator.get_max_dice_combination(dice)
    self.assertTrue(set((1,1,1)).issubset(combination))
    
    dice = (3,3,3,4,5,6)
    combination = DiceCalculator.get_max_dice_combination(dice)
    self.assertTrue(set((3,3,3,5)).issubset(combination))
    
    dice = (1,2,3,4,5,6)
    combination = DiceCalculator.get_max_dice_combination(dice)
    self.assertTrue(set((1,2,3,4,5,6)).issubset(combination))
    
    dice = (1,1,1,3,3,3)
    combination = DiceCalculator.get_max_dice_combination(dice)
    self.assertTrue(set((1,1,1,3,3,3)).issubset(combination))
    
    dice = (1,1,3,3,3,5)
    combination = DiceCalculator.get_max_dice_combination(dice)
    self.assertTrue(set((1,1,3,3,3,5)).issubset(combination))
  
  def test_points_calculation(self):
    dice = (1,2,3,4,5,6)
    points = DiceCalculator.calculate_dice_points(dice)
    self.assertEqual(points, 3000)
    
    dice = (1,1,3,3,4,4)
    points = DiceCalculator.calculate_dice_points(dice)
    self.assertEqual(points, 1500)
    
    dice = (6,6,6,1,1,1)
    points = DiceCalculator.calculate_dice_points(dice)
    self.assertEqual(points, 1600)
    
    dice = (1,5)
    points = DiceCalculator.calculate_dice_points(dice)
    self.assertEqual(points, 150)
  
    dice = (1,1,1,1,5)
    points = DiceCalculator.calculate_dice_points(dice)
    self.assertEqual(points, 1150)
    
    dice = (5,5,5,1)
    points = DiceCalculator.calculate_dice_points(dice)
    self.assertEqual(points, 600)
      
    dice = ()
    with self.assertRaises(InvalidSelectionError):
      DiceCalculator.calculate_dice_points(dice)
    
  def test_dice_removal(self):
    dice = (1,1,1,3,4,4)
    selected_dice = (1,1,1)
    remaining_dice = DiceCalculator.remove_selected_dice(dice, selected_dice)
    self.assertEqual((3,4,4), remaining_dice)
    
  def test_farkle(self):
    dice = (2,2,3,4,6,6)
    self.assertTrue(DiceCalculator.is_farkle(dice))
    
    dice = (1,2,3,4,6,6)
    self.assertFalse(DiceCalculator.is_farkle(dice))
    
    
if __name__ == '__main__':
  unittest.main()