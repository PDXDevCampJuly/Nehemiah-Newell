__author__ = 'Nehemiah'
__author__ = 'Nehemiah'

import unittest
from unittest.mock import patch
from io import StringIO
import angry_dice_testable


class test_can_play(unittest.TestCase):
    """Checks if the game is in a state where it can advance"""
    def setUp(self):
        self.game = angry_dice_testable.Angry_Dice()
        print(self.shortDescription())

    def tearDown(self):
        print("Just ran: ")
        print(self._testMethodName)
        del self.game


    @patch("sys.stdout",new_callable=StringIO)
    def test_game_can_advance(self, mock_stdout):
        junk_string = "You rolled:\n   a =[ 1 ]\n   b =[ 1 ]\n\nYou are in " \
                      "Stage 1\n"
        self.game.can_play()

        self.assertEqual(junk_string,mock_stdout.getvalue())

    @patch("sys.stdout",new_callable=StringIO)
    def test_A_die_is_cheating(self, mock_stdout):
        self.game.invalidFlagA = True
        junk_string = "You're cheating! You cannot lock a 1! you cannot\nwin until you reroll it!\nYou rolled:\n   a =[ 1 ]\n   b =[ 1 ]\n\n"
        self.game.can_play()

        self.assertEqual(junk_string,mock_stdout.getvalue())

    @patch("sys.stdout",new_callable=StringIO)
    def test_B_die_is_cheating(self, mock_stdout):
        self.game.invalidFlagB = True
        junk_string = "You're cheating! You cannot lock a 1! you cannot\nwin until you reroll it!\nYou rolled:\n   a =[ 1 ]\n   b =[ 1 ]\n\n"
        self.game.can_play()

        self.assertEqual(junk_string,mock_stdout.getvalue())

    @patch("sys.stdout",new_callable=StringIO)
    def test_dice_are_cheating(self, mock_stdout):
        self.game.invalidFlagB = True
        self.game.invalidFlagA = True
        junk_string = "You're cheating! You cannot lock both of those dice! you cannot\nwin until you reroll it!\nYou rolled:\n   a =[ 1 ]\n   b =[ 1 ]\n\n"
        self.game.can_play()

        self.assertEqual(junk_string,mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()

