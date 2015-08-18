__author__ = 'Nehemiah'

import unittest
from unittest.mock import patch
from io import StringIO
import angry_dice_testable



class test_print_stage(unittest.TestCase):
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
    def test_print_stage(self,mock_stdout):
        """Test if print stage outputs correctly"""
        self.game.print_stage()
        self.assertEqual("You are in Stage 1\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
