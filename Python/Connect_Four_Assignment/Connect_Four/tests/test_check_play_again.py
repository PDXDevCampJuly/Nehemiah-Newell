__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_controller import Connect_Four_Controller


class test_ask_for_play_again(unittest.TestCase):
    """Check that the correct message prints for a tie"""

    def setUp(self):
        self.controller = Connect_Four_Controller()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.controller


    @patch('builtins.input', return_value=('y'))
    @patch("sys.stdout",new_callable=StringIO)
    def test_reset_yes(self, mock_output, inputvalue):
        """Test if the player returns yes on play again input"""

        self.controller.game_state.player = 1

        self.controller.check_play_again()

        self.assertEqual(self.controller.game_state.player, -1)

    #
    # @patch('builtins.input', side_effects=['n', 'n'])
    # @patch("sys.stdout",new_callable=StringIO)
    # def test_reset_no(self, mock_output, inputvalue):
    #     """Test if the player returns no on play again input"""
    #
    #     self.controller.check_play_again()
    #     self.assertEqual("Would you care to play again? Yes or No (Y / N) \n"
    #                      "\n", mock_output.getvalue())

if __name__ == '__main__':
    unittest.main()