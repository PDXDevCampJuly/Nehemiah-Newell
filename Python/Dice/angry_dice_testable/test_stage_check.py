__author__ = 'Nehemiah'

import unittest
from unittest.mock import patch
from io import StringIO
import angry_dice_testable


class test_stage_check(unittest.TestCase):
    """Test the stage movement controls"""
    def setUp(self):
        self.game = angry_dice_testable.Angry_Dice()
        print(self.shortDescription())

    def tearDown(self):
        print("Just ran: ")
        print(self._testMethodName)
        print()
        del self.game


    @patch("sys.stdout",new_callable=StringIO)
    def test_if_angry(self, mock_stdout):
        """Does the game reset and print a message when angry"""
        self.game.currentStage = 1
        self.game.angryDieA.currentValue = "ANGRY"
        self.game.angryDieB.currentValue = "ANGRY"
        self.game.stage_check()
        self.assertEqual(1, self.game.currentStage,"ANGRYANGRY moved the stage incorrectly at stage 1")
        self.assertEqual("WOW, you're ANRGY!\nTime to go back to Stage 1!\n", mock_stdout.getvalue(),"ANGRYANGRY didn't print")
        mock_stdout.seek(0)
        mock_stdout.truncate(0)
        self.game.currentStage = 2
        self.game.stage_check()
        self.assertEqual(1, self.game.currentStage,"ANGRYANGRY moved the stage incorrectly at stage 2")
        self.assertEqual("WOW, you're ANRGY!\nTime to go back to Stage 1!\n", mock_stdout.getvalue(),"ANGRYANGRY didn't print")
        mock_stdout.seek(0)
        mock_stdout.truncate(0)
        self.game.currentStage = 3
        self.game.stage_check()
        self.assertEqual(1, self.game.currentStage,"ANGRYANGRY moved the stage incorrectly at stage 3")
        self.assertEqual("WOW, you're ANRGY!\nTime to go back to Stage 1!\n", mock_stdout.getvalue(),"ANGRYANGRY didn't print")


    def test_dont_advance_stage_one(self):
        """Does the game not advance for the wrong roll at stage one"""
        self.game.currentStage = 1
        for roll in ["ANGRY","4","5","6"]:
            for combo in ["4","5","6"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = combo
                self.game.stage_check()
                self.assertEqual(1, self.game.currentStage,"Stage advanced when it shouldn't have")

    def test_dont_advance_stage_two(self):
        """Does the game not advance for the wrong roll at stage two"""
        self.game.currentStage = 2
        for roll in ["1","2","5","6"]:
            for combo in ["1","2","5","6"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = combo
                self.game.stage_check()
                self.assertEqual(2, self.game.currentStage,"Stage advanced when it shouldn't have")

    def test_dont_advance_stage_three(self):
        """Does the game not advance for the wrong roll at stage three"""
        self.game.currentStage = 3
        for roll in ["1","2","ANGRY","4"]:
            for combo in ["1","2","4"]:
                self.game.angryDieA.currentValue = roll
                self.game.angryDieB.currentValue = combo
                self.game.stage_check()
                self.assertEqual(3, self.game.currentStage,"Stage changed when it shouldn't have")

    def test_advance_stage_one(self):
        """Does the game advance for the right rolls at stage one"""
        self.game.currentStage = 1
        self.game.angryDieA.currentValue = "1"
        self.game.angryDieB.currentValue = "2"
        self.game.stage_check()
        self.assertEqual(2, self.game.currentStage,"Stage didn't advanced when it should.")
        self.game.currentStage = 1
        self.game.angryDieA.currentValue = "2"
        self.game.angryDieB.currentValue = "1"
        self.game.stage_check()
        self.assertEqual(2, self.game.currentStage,"Stage didn't advanced when it should.")

    def test_advance_stage_two(self):
        """Does the game advance for the right rolls at stage two"""
        self.game.currentStage = 2
        self.game.angryDieA.currentValue = "ANGRY"
        self.game.angryDieB.currentValue = "4"
        self.game.stage_check()
        self.assertEqual(3, self.game.currentStage,"Stage didn't advanced when it should.")
        self.game.currentStage = 2
        self.game.angryDieA.currentValue = "4"
        self.game.angryDieB.currentValue = "ANGRY"
        self.game.stage_check()
        self.assertEqual(3, self.game.currentStage,"Stage didn't advanced when it should.")

    def test_advance_stage_three(self):
        """Does the game advance for the right rolls at stage three"""
        self.game.currentStage = 3
        self.game.angryDieA.currentValue = "5"
        self.game.angryDieB.currentValue = "6"
        self.assertRaises(SystemExit)
        self.game.currentStage = 3
        self.game.angryDieA.currentValue = "6"
        self.game.angryDieB.currentValue = "5"
        self.assertRaises(SystemExit)


if __name__ == '__main__':
    unittest.main()
