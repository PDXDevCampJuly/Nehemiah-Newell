__author__ = 'jbroxton'

import unittest
from connect_4_model import Connect_Four_Model


class test_model_board(unittest.TestCase):
    """Testing the get board function"""

    def setUp(self):
        self.model = Connect_Four_Model()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.model

    def test_return_board(self):
        """Testing that get_board() returns the connect 4 board"""
        self.assertEqual(self.model.get_board(), self.model.board)


if __name__ == '__main__':
    unittest.main()





