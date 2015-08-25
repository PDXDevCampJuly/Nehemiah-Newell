__author__ = 'jbroxton'

import unittest
from connect_4_model import Connect_Four_Model


class test_reset_game_state(unittest.TestCase):
    """Testing the board after a player turn updates it"""

    def setUp(self):
        self.model = Connect_Four_Model()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.model

    def test_reset_board_state(self):
        """Testing the reset game function returns a clean board"""

        #create a valid board
        good_col = [-1,1,1,-1,1,1]
        good_board = [good_col, good_col, good_col, good_col, good_col, good_col,
                      good_col]


        empty_board = [[],[],[],[],[],[],[]]

        #testing that valid board == a valid board after calling the update
        #board function

        self.model.board = good_board

        self.model.reset_state()
        self.assertEqual(empty_board, self.model.board)

    def test_reset_player(self):
        """"""

        self.model.player = 1

        self.model.reset_state()

        self.assertEqual(-1, self.model.player)


if __name__ == '__main__':
    unittest.main()





