__author__ = 'jbroxton'

import unittest
from connect_4_model import Connect_Four_Model


class test_flip_current_player(unittest.TestCase):
    """Testing the flip_current_player() function"""

    def setUp(self):
        self.model = Connect_Four_Model()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.model

    def test_flip_player(self):
        """Testing that flip_current_player() returns a player"""

        #create a variable to hold the previous player
        previous_player = self.model.player

        #compare the current player to the previous player after calling the
        #flip_current_player() function
        self.model.flip_current_player()
        self.assertNotEqual(self.model.player, previous_player)

    def test_flip_returns(self):
        """Test that the flip_current_player() flips the player """

        #Player 1 and Player 2 are represented by 1 and -1
        #Multiplying current_player by -1 will flip them
        current_player = self.model.player * -1

        #after running flip_current_player function, test current player
        self.assertEqual(self.model.flip_current_player(), current_player)


if __name__ == '__main__':
    unittest.main()





