__author__ = 'jbroxton'

import unittest
from connect_4_model import Connect_Four_Model


class test_model_update_board(unittest.TestCase):
    """Testing the board after a player turn updates it"""

    def setUp(self):
        self.model = Connect_Four_Model()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.model

    def test_update_good_data_board(self):
        """Testing that update_board() function updates the board when
        given good data"""

        #create a valid board
        good_col = [-1,1,1,-1,1,1]
        good_board = [good_col, good_col, good_col, good_col, good_col, good_col,
                      good_col]

        #testing that valid board == a valid board after calling the update
        #board function
        self.model.update_board(good_board)
        self.assertEqual(good_board, self.model.board)

    def test_update_bad_data_board(self):
        """Testing the update_board() function when given bad column data"""

        #create a valid board
        good_col = [-1,1,1,-1,1,1]
        good_board = [good_col, good_col, good_col, good_col, good_col, good_col,
                      good_col]

        self.model.board = good_board

        #create an invalid board
        bad_col = [-1,1,1,-1,1,1]
        bad_col_board = [bad_col, bad_col, bad_col, bad_col, bad_col, bad_col,
                         bad_col, bad_col]

        #test that the update board function is not setting an invalid board
        #with too many columns
        self.model.update_board(bad_col_board)
        self.assertEqual(good_board, self.model.board)

    def test_update_bad_height_board(self):
        """Testing update_board() function does not return a board with an
        extra row"""

        #create a valid board
        good_col = [-1,1,1,-1,1,1]
        good_board = [good_col, good_col, good_col, good_col, good_col, good_col,
                      good_col]

        self.model.board = good_board

        #create an invalid board
        bad_col = [-1,1,1,-1,1,1,1]
        bad_col_board = [bad_col, bad_col, bad_col, bad_col, bad_col, bad_col,
                         bad_col]

        #test that the update board function is not setting an invalid board
        #with an incorrect height
        self.model.update_board(bad_col_board)
        self.assertEqual(good_board, self.model.board)

    def test_update_bad_value_board(self):
        """Test update_board() does not create a board with bad player values
        which are currently 1 and -1"""

        #create a valid board
        good_col = [-1,1,1,-1,1,1]
        good_board = [good_col, good_col, good_col, good_col, good_col, good_col,
                      good_col]

        self.model.board = good_board

        #create an invalid board
        bad_value = [2,2,2,2,2,2]
        bad_val_board = [bad_value, bad_value, bad_value, bad_value, bad_value,
                         bad_value, bad_value]

        #test that the update board function is not setting an invalid board
        #with incorrect values
        self.model.update_board(bad_val_board)
        self.assertEqual(good_board, self.model.board)

    def test_update_empty_board(self):
        """Test update_board() does not create a board with empty columns/
        rows"""

        #create a valid board
        good_col = [-1,1,1,-1,1,1]
        good_board = [good_col, good_col, good_col, good_col, good_col, good_col,
                      good_col]

        self.model.board = good_board

        #create an empty board
        empty_board = []

        #test that the update board function is not setting an invalid board
        #that is empty
        self.model.update_board(empty_board)
        self.assertEqual(good_board, self.model.board)


if __name__ == '__main__':
    unittest.main()





