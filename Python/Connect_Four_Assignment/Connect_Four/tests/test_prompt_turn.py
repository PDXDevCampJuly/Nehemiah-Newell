__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_prompt_turn(unittest.TestCase):
    """Check that the game correctly prompts the player for a turn"""

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view


    @patch("sys.stdout",new_callable=StringIO)
    def test_prompt_turn(self,mock_stdout):
        """Test if the player is prompted for their turn"""
        fake_player = "Red"
        prompt_string = "Red Player: Please select the column for this turn ".\
            format(fake_player)
        self.view.prompt_turn(fake_player)
        self.assertEqual("Red Player: Please select the column for this turn "
                         "\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()