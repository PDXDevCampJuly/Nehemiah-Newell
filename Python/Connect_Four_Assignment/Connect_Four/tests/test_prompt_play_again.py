__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_prompt_play_again(unittest.TestCase):
    """Check that the game asks the players if they want to play again """

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view


    @patch("sys.stdout",new_callable=StringIO)
    def test_prompt_for_new_game(self,mock_stdout):
        """Test if the play again prompt prints correctly"""

        self.view.prompt_play_again()
        self.assertEqual("Would you care to play again? Yes or No (Y / N) \n"
                         "\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()