__author__ = 'jbroxton'

import unittest

from connect_4_controller import Connect_Four_Controller



class test_alternating_players(unittest.TestCase):
    """Check that the game correctly flips the player back and forth"""

    def setUp(self):
        self.controller = Connect_Four_Controller()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.controller


    def test_switch_player(self):
        """Test if the players are switched"""

        previous_player = self.controller.game_state.player

        #compare the current player to the previous player after calling the
        #flip_current_player() function
        self.controller.game_state.flip_current_player()
        self.assertNotEqual(self.controller.game_state.player, previous_player)

    def test_switch_returns(self):
        """Test that the switch player function returns a player """

        #Player 1 and Player 2 are represented by 1 and -1
        #Multiplying current_player by -1 will flip them
        current_player = self.controller.game_state.player * -1

        #after running flip_current_player function in the controller,
        # test current player
        self.assertEqual(self.controller.game_state.flip_current_player(),
                         current_player)

if __name__ == '__main__':
    unittest.main()