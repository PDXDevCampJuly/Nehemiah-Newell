__author__ = 'jbroxton'

import unittest
from connect_4_controller import Connect_Four_Controller



class test_check_win_loss_tie(unittest.TestCase):
    """Check that the print board function returns a board"""

    def setUp(self):
        self.controller = Connect_Four_Controller()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.controller


    def test_check_no_win(self):
        """Test if check status does not declare a winner if no one wins"""

        #create good columns that do not have a winner
        no_win_col_1 = [ 1 , 1,-1,-1]
        no_win_col_2 = [-1, -1, 1,-1]
        no_win_col_3 = [ 1,  1,-1, 1]
        no_win_col_4 = [ 1,  1,-1, 1]
        no_win_col_5 = [-1, -1, 1,-1]
        no_win_col_6 = [ 1,  1,-1,-1]
        no_win_col_7 = [-1, -1, 1,-1]

        #create a no_win board using no_win columns with no winner
        no_win_board = [no_win_col_1, no_win_col_2, no_win_col_3, no_win_col_4,
                      no_win_col_5, no_win_col_6, no_win_col_7]

        #check the no_win board for no win
        #key for no_win == 0

        self.assertEqual(self.controller.check_game_status(no_win_board), 0)

    def test_check_tie_game(self):
        """Test if check status does not declare a winner if the game is tied"""

        #create tie game columns that do not have a winner
        tie_col_1 = [1,  -1,  -1,  1,  1, -1]
        tie_col_2 = [1,   1,  -1, -1,  1,  1]
        tie_col_3 = [-1, -1,  -1,  1,  1,  1]
        tie_col_4 = [-1,  1,   1,  1, -1, -1]
        tie_col_5 = [1,  -1,  -1, -1,  1, -1]
        tie_col_6 = [1,   1,  -1, -1,  1, -1]
        tie_col_7 = [-1,  1,   1,  1, -1,  1]

        #create a tie board using tie columns with no winner
        tie_board = [tie_col_1, tie_col_2, tie_col_3, tie_col_4,
                      tie_col_5, tie_col_6, tie_col_7]
        
        #check the status of the tie board for a tie
        #key for tie == 1

        self.assertEqual(self.controller.check_game_status(tie_board), 1)
        
    def test_check_horizontal_win(self):
        """Test if check status declares winner for horizontal win"""

        #create horizontal win game columns that have a winner
        horiz_win_col_1 = [1]
        horiz_win_col_2 = [1]
        horiz_win_col_3 = [1]
        horiz_win_col_4 = [1]
        horiz_win_col_5 = []
        horiz_win_col_6 = []
        horiz_win_col_7 = []

        #create a horizontal win board using horiz_win columns
        horiz_win_board = [horiz_win_col_1, horiz_win_col_2, horiz_win_col_3,
                     horiz_win_col_4, horiz_win_col_5, horiz_win_col_6, 
                     horiz_win_col_7]
        
        #check the status of the horizontal win board for a win
        #key for win == 42

        self.assertEqual(self.controller.check_game_status(horiz_win_board), 42)


    def test_check_vertical_win(self):
        """Test if check status declares winner for vertical win"""

        #create vertical win game columns
        vert_win_col_1 = [1, 1, 1, 1]
        vert_win_col_2 = []
        vert_win_col_3 = []
        vert_win_col_4 = []
        vert_win_col_5 = []
        vert_win_col_6 = []
        vert_win_col_7 = []

        #create a vertical win board using vert_win columns
        vert_win_board = [vert_win_col_1, vert_win_col_2, vert_win_col_3,
                     vert_win_col_4, vert_win_col_5, vert_win_col_6, 
                     vert_win_col_7]
        
        #check the status of the vertical win board for a win
        #key for win == 42

        self.assertEqual(self.controller.check_game_status(vert_win_board), 42)
        
    def test_check_up_diagonal_win(self):
        """Test if check status declares winner for vertical win"""

        #create diagonal win game columns
        upward_diagonal_win_col_1 = [1]
        upward_diagonal_win_col_2 = [-1,1]
        upward_diagonal_win_col_3 = [1,-1,1]
        upward_diagonal_win_col_4 = [-1,1,-1,1]
        upward_diagonal_win_col_5 = []
        upward_diagonal_win_col_6 = []
        upward_diagonal_win_col_7 = []

        #create a upward diagonal win board using 
        # upward_diagonal_win columns
        upward_diagonal_win_board = \
            [upward_diagonal_win_col_1, upward_diagonal_win_col_2, 
                     upward_diagonal_win_col_3, upward_diagonal_win_col_4, 
                     upward_diagonal_win_col_5, upward_diagonal_win_col_6, 
                     upward_diagonal_win_col_7]
        
        #check the status of the upward diagonal win board for a win
        #key for win == 42

        self.assertEqual(self.controller.check_game_status(upward_diagonal_win_board), 42)

    def test_check_down_diagonal_win(self):
        """Test if check status declares winner for vertical win"""

        #create diagonal win game columns
        downward_diagonal_win_col_1 = [-1,1,-1, 1]
        downward_diagonal_win_col_2 = [1,-1,1]
        downward_diagonal_win_col_3 = [-1,1]
        downward_diagonal_win_col_4 = [1]
        downward_diagonal_win_col_5 = []
        downward_diagonal_win_col_6 = []
        downward_diagonal_win_col_7 = []

        #create a downward diagonal win board using 
        # downward_diagonal_win columns
        downward_diagonal_win_board = \
            [downward_diagonal_win_col_1, downward_diagonal_win_col_2, 
                     downward_diagonal_win_col_3, downward_diagonal_win_col_4, 
                     downward_diagonal_win_col_5, downward_diagonal_win_col_6, 
                     downward_diagonal_win_col_7]
        
        #check the status of the downward diagonal win board for a win
        #key for win == 42

        self.assertEqual(self.controller.check_game_status(downward_diagonal_win_board), 42)


if __name__ == '__main__':
    unittest.main()

