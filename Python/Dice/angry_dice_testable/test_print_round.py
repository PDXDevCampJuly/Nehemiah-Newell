__author__ = 'Nehemiah'

import unittest
from unittest.mock import patch
from io import StringIO
import angry_dice_testable



class test_print_round(unittest.TestCase):
    """Check that it prints correctly when"""

    def setUp(self):
        self.game = angry_dice_testable.Angry_Dice()
        print(self.shortDescription())

    def tearDown(self):
        print("Just ran: ")
        print(self._testMethodName)
        print()
        del self.game


    @patch("sys.stdout",new_callable=StringIO)
    def test_print_round(self,mock_stdout):
        """Test if print round outputs correctly"""
        self.game.print_round()
        self.assertEqual("You rolled:\n   a =[ 1 ]\n   b =[ 1 ]\n\n", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
