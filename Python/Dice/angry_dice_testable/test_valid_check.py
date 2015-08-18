__author__ = 'Nehemiah'

import unittest
import angry_dice_testable


class test_valid_check(unittest.TestCase):
    """Test that the user isn't cheating"""

    def setUp(self):
        self.game = angry_dice_testable.Angry_Dice()
        print(self.shortDescription())

    def tearDown(self):
        print("Just ran: ")
        print(self._testMethodName)
        print()
        del self.game

    def test_stage_one_die_flag(self):
        """test if stage one sets the A die correctly"""
        self.game.currentStage = 1
        for roll in ["ANGRY","4","5","6"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = roll
                self.game.invalidFlagA = False
                self.game.invalidFlagB = False
                self.game.valid_check()
                self.assertTrue(self.game.invalidFlagA,"Cheating flag for die A wasn't set")
                self.assertTrue(self.game.invalidFlagB, "Cheating flag for die B wasn't set")

    def test_stage_two_die_flag(self):
        """test if stage two sets the A die correctly"""
        self.game.currentStage = 2
        for roll in ["1","2","5","6"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = roll
                self.game.invalidFlagA = False
                self.game.invalidFlagB = False
                self.game.valid_check()
                self.assertTrue(self.game.invalidFlagA,"Cheating flag for die A wasn't set")
                self.assertTrue(self.game.invalidFlagB, "Cheating flag for die B wasn't set")

    def test_stage_three_die_flag(self):
        """test if stage three sets the A die correctly"""
        self.game.currentStage = 3
        for roll in ["1","2","3","4","6"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = roll
                self.game.invalidFlagA = False
                self.game.invalidFlagB = False
                self.game.valid_check()
                self.assertTrue(self.game.invalidFlagA,"Cheating flag for die A wasn't set")
                self.assertTrue(self.game.invalidFlagB, "Cheating flag for die B wasn't set")

    def test_stage_one_die_pass(self):
        """test if stage one avoids setting the A die correctly"""
        self.game.currentStage = 1
        for roll in ["1","2"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = roll
                self.game.invalidFlagA = False
                self.game.invalidFlagB = False
                self.game.valid_check()
                self.assertFalse(self.game.invalidFlagA,"Cheating flag for die A was set")
                self.assertFalse(self.game.invalidFlagB, "Cheating flag for die B was set")

    def test_stage_two_die_pass(self):
        """test if stage two avoids setting the A die correctly"""
        self.game.currentStage = 2
        for roll in ["ANGRY","4"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = roll
                self.game.invalidFlagA = False
                self.game.invalidFlagB = False
                self.game.valid_check()
                self.assertFalse(self.game.invalidFlagA,"Cheating flag for die A was set")
                self.assertFalse(self.game.invalidFlagB, "Cheating flag for die B was set")

    def test_stage_three_die_pass(self):
        """test if stage three avoids setting the A die correctly"""
        self.game.currentStage = 3
        self.game.angryDieA.currentValue = "5"
        self.game.angryDieB.currentValue = "5"
        self.game.invalidFlagA = False
        self.game.invalidFlagB = False
        self.game.valid_check()
        self.assertFalse(self.game.invalidFlagA,"Cheating flag for die A was set")
        self.assertFalse(self.game.invalidFlagB, "Cheating flag for die B was set")


if __name__ == '__main__':
    unittest.main()
