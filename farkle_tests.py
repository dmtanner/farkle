import unittest
import farkle

class TestFarkle(unittest.TestCase):
  def setUp(self):
    self.farkle = farkle.FarkleGame()
    
  def test_roll_is_valid(self):
    dice = self.farkle.roll_dice()
    self.assertEqual(len(dice), 6)
    for die in dice:
      self.assertGreaterEqual(die, 1)
      self.assertLessEqual(die, 6)
      
  def test_player_score(self):
    self.farkle.add_to_score(0, 300)
    self.assertEqual(self.farkle.get_player_score(0), 300)
    
  def test_straight(self):
    dice = (1,2,3,4,5,6)
    self.assertTrue(self.farkle.has_straight(dice))
    self.assertEqual(self.farkle.has_straight(dice), dice)
    dice = (1,1,1,6,6,6)
    self.assertFalse(self.farkle.has_straight(dice))
    dice = (1,2,3,4)
    self.assertFalse(self.farkle.has_straight(dice))
    dice = (1,)
    self.assertFalse(self.farkle.has_straight(dice))
    
  def test_three_pair(self):
    dice = (1,1,2,2,3,3)
    self.assertTrue(self.farkle.has_three_pair(dice))
    self.assertEqual(self.farkle.has_three_pair(dice), dice)
    dice = (1,1,1,1,3,3)
    self.assertTrue(self.farkle.has_three_pair(dice))
    self.assertEqual(self.farkle.has_three_pair(dice), dice)
    dice = (1,1,1,1,1,1)
    self.assertTrue(self.farkle.has_three_pair(dice))
    self.assertEqual(self.farkle.has_three_pair(dice), dice)
    dice = (1,1,2,2,3,4)
    self.assertFalse(self.farkle.has_three_pair(dice))
    dice = (1,1,2,2)
    self.assertFalse(self.farkle.has_three_pair(dice))
    dice = (1,)
    self.assertFalse(self.farkle.has_three_pair(dice))
    
  def test_three_of_a_kind(self):
    dice = (1,1,1,2,3,4)
    self.assertTrue(self.farkle.has_three_of_a_kind(dice))
    self.assertTrue(self.farkle.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,1,1,1,1)
    self.assertTrue(self.farkle.has_three_of_a_kind(dice))
    self.assertTrue(self.farkle.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,1,2,2,2)
    self.assertTrue(self.farkle.has_three_of_a_kind(dice))
    self.assertTrue(self.farkle.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,1)
    self.assertTrue(self.farkle.has_three_of_a_kind(dice))
    self.assertTrue(self.farkle.has_three_of_a_kind(dice), (1,1,1))
    dice = (1,1,2,2,3,4)
    self.assertFalse(self.farkle.has_three_of_a_kind(dice))
    dice = (1,)
    self.assertFalse(self.farkle.has_three_of_a_kind(dice))
  
  def test_one(self):
    dice = (1,1,1,2,3,4)
    self.assertTrue(self.farkle.has_one(dice))
    dice = (1,)
    self.assertTrue(self.farkle.has_one(dice))
    self.assertEqual(self.farkle.has_one(dice), (1,))
    dice = (2,3,4,5,6,6)
    self.assertFalse(self.farkle.has_one(dice))
    
  def test_five(self):
    dice = (1,2,3,4,5,6)
    self.assertTrue(self.farkle.has_five(dice))
    self.assertEqual(self.farkle.has_five(dice), (5,))
    dice = (1,2,5,5,5,6)
    self.assertTrue(self.farkle.has_five(dice))
    self.assertEqual(self.farkle.has_five(dice), (5,))
    dice = (5,)
    self.assertTrue(self.farkle.has_five(dice))
    self.assertEqual(self.farkle.has_five(dice), (5,))
    dice = (1,2,3,4,6,6)
    self.assertFalse(self.farkle.has_five(dice))
    
  def test_dice_combinations(self):
    dice = (1,5)
    combinations = self.farkle.get_dice_combinations(dice)
    self.assertTrue((1,) in combinations.keys())
    self.assertEqual(combinations[(1,)], 100)
    self.assertTrue((5,) in combinations.keys())
    self.assertEqual(combinations[(5,)], 50)
    
    dice = (1,1,3,3,5,5)
    combinations = self.farkle.get_dice_combinations(dice)
    self.assertTrue((1,1,3,3,5,5) in combinations.keys())
    self.assertEqual(combinations[(1,1,3,3,5,5)], 1500)
    self.assertTrue((1,) in combinations.keys())
    self.assertTrue((5,) in combinations.keys())
    
    dice = (1,1,1,2,3,4)
    combinations = self.farkle.get_dice_combinations(dice)
    self.assertTrue((1,1,1) in combinations.keys())
    self.assertEqual(combinations[(1,1,1)], 1000)
    self.assertTrue((1,) in combinations.keys())
    
    dice = (3,3,3,4,5,6)
    combinations = self.farkle.get_dice_combinations(dice)
    self.assertTrue((3,3,3) in combinations.keys())
    self.assertEqual(combinations[(3,3,3)], 300)
    self.assertTrue((5,) in combinations.keys())
    
    dice = (1,2,3,4,5,6)
    combinations = self.farkle.get_dice_combinations(dice)
    self.assertTrue((1,2,3,4,5,6) in combinations.keys())
    self.assertTrue((1,) in combinations.keys())
    self.assertTrue((5,) in combinations.keys())
  
  def test_dice_removal(self):
    dice = (1,1,1,3,4,4)
    combinations = self.farkle.get_dice_combinations(dice)
    selected_dice = (1,1,1)
    remaining_dice = self.farkle.remove_selected_dice(dice, selected_dice)
    self.assertEqual((3,4,4), remaining_dice)
    
  def test_gameplay_output(self):
    return 0
    
    
    
if __name__ == '__main__':
  unittest.main()