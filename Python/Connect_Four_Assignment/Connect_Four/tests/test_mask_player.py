__author__ = 'jbroxton'

import unittest
from connect_4_controller import Connect_Four_Controller


class test_player_masking(unittest.TestCase):
    """Check that the game correctly masks the current player"""

    def setUp(self):
        self.controller = Connect_Four_Controller()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.controller


    def test_mask_player(self):
        """Test if the players integer values equal their color"""

        #set the player int to the 'Black' designation
        self.controller.game_state.player = -1

        #test the player int is equal to the player color
        self.assertEqual(self.controller.mask_player(self.controller.game_state.get_current_player()), "Black")

if __name__ == '__main__':
    unittest.main()