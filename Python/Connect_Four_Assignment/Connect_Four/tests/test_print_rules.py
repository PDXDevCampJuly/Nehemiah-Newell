__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_print_rules(unittest.TestCase):
    """Check that it prints correctly when"""

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view


    @patch("sys.stdout",new_callable=StringIO)
    def test_print_rules(self,mock_stdout):
        """Test if the rules print correctly"""

        self.view.print_rules()
        self.assertEqual("Connect Four is a two-player connection game in which "
                         "the players take turns dropping pieces from the top "
                         "into a seven-column, six-row vertically suspended "
                         "grid. The pieces fall straight down, occupying the "
                         "next available space within the column. The objective "
                         "of the game is to connect four of one's own pieces of "
                         "the same color next to each other vertically, "
                         "horizontally, or diagonally before your opponent.\n"
                         "\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()