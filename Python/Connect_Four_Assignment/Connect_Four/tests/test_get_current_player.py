__author__ = 'jbroxton'

import unittest
from connect_4_model import Connect_Four_Model


class test_get_current_player(unittest.TestCase):
    """Testing the get_current_player() function"""

    def setUp(self):
        self.model = Connect_Four_Model()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.model

    def test_get_player(self):
        """Testing that get_current_player() returns a player"""
        self.assertEqual(self.model.get_current_player(), self.model.player)


if __name__ == '__main__':
    unittest.main()





