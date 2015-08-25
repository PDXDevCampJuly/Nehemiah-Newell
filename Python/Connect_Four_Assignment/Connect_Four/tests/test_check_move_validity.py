__author__ = 'jbroxton'

import unittest
from connect_4_controller import Connect_Four_Controller


class test_check_for_valid_moves(unittest.TestCase):
    """Check that player moves are valid"""

    def setUp(self):
        self.controller = Connect_Four_Controller()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.controller

    def test_valid_move(self):
        """Test if a move is valid"""

        #create good columns using list values
        good_col_1 = []
        good_col_2 = []
        good_col_3 = []
        good_col_4 = []
        good_col_5 = []
        good_col_6 = []
        good_col_7 = []

        #create a good board using good columns
        good_board = [good_col_1, good_col_2, good_col_3, good_col_4,
                      good_col_5, good_col_6, good_col_7]

        #passing a valid column to the check move validity function should
        #return True
        self.assertTrue(self.controller.check_move_validity(good_board, 1))


    def test_invalid_move(self):
        """Test if a player is trying to play a piece on a full column"""

        #create bad columns using list values
        bad_col_1 = [1, 1, 1, 1, 1, 1]
        bad_col_2 = [1, 1, 1, 1, 1, 1]
        bad_col_3 = [1, 1, 1, 1, 1, 1]
        bad_col_4 = [1, 1, 1, 1, 1, 1]
        bad_col_5 = [1, 1, 1, 1, 1, 1]
        bad_col_6 = [1, 1, 1, 1, 1, 1]
        bad_col_7 = [1, 1, 1, 1, 1, 1]

        #create a bad board using bad columns
        bad_board = [bad_col_1, bad_col_2, bad_col_3, bad_col_4,
                      bad_col_5, bad_col_6, bad_col_7]

        #passing an invalid column to the check move validity function should
        #return False
        self.assertFalse(self.controller.check_move_validity(bad_board, 1))

    def test_bad_position_input(self):
        """Testing for bad input"""

        #create good columns using list values
        good_col_1 = []
        good_col_2 = []
        good_col_3 = []
        good_col_4 = []
        good_col_5 = []
        good_col_6 = []
        good_col_7 = []

        #create a good board using good columns
        good_board = [good_col_1, good_col_2, good_col_3, good_col_4,
                      good_col_5, good_col_6, good_col_7]

        #passing an invalid move to the check move validity function should
        #return False
        self.assertFalse(self.controller.check_move_validity(good_board, 7))

if __name__ == '__main__':
    unittest.main()