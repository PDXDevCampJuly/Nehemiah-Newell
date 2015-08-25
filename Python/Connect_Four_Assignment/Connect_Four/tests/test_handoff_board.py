__author__ = 'jbroxton'

import unittest
from connect_4_controller import Connect_Four_Controller


class test_pass_on_board(unittest.TestCase):
    """Testing the handoff of the board from one player to the other"""

    def setUp(self):
        self.game = Connect_Four_Controller()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.game

    def test_handoff_board(self):
        """Testing that the board handoff function is working correctly"""
        self.assertEqual(self.game.handoff_board(), self.game.game_state.board)


if __name__ == '__main__':
    unittest.main()





