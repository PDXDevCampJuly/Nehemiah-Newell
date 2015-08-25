__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_board_instantiation(unittest.TestCase):
    """Check that the print board function returns a board"""

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " +
              str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view


    @patch("sys.stdout",new_callable=StringIO)
    def test_print_board(self, mock_stdout):
        """Test if the print board function prints a connect 4 board"""

        #create a dummy board from scratch to compare to the board with list
        #values
        dummyboard = ('|' + ' ' + '|' + ' ' + '|' + ' ' +
              '|' + ' ' + '|' + ' ' + '|' + u"\u25EF" +
              '|' + ' ' + '|' + '\n' + '|' + ' ' + '|' + ' ' + '|' + ' ' +
              '|' + ' ' + '|' + ' ' + '|' + u"\u25EF" +
              '|' + ' ' + '|' + '\n' + '|' + ' ' + '|' + ' ' + '|' + ' ' +
              '|' + ' ' + '|' + ' ' + '|' + u"\u25EF" +
              '|' + ' ' + '|'+ '\n' + '|' + ' ' + '|' + ' ' + '|' + ' ' +
              '|' + ' ' + '|' + ' ' + '|' + u"\u25EF" +
              '|' + ' ' + '|'+ '\n' + '|' + ' ' + '|' + ' ' + '|' + ' ' +
              '|' + ' ' + '|' + ' ' + '|' + u'\u25CF' +
              '|' + ' ' + '|'+ '\n' + '|' + u"\u25EF" + '|' + u'\u25CF' +
              '|' + u"\u25EF" +
              '|' + u"\u25EF" + '|' + u'\u25CF' + '|' + u"\u25EF" +
              '|' + u'\u25CF' + '|'+ '\n' + "===============\n"
                      + "[]           []\n\n")

        #create good columns using list values
        good_col_1 = [1]
        good_col_2 = [-1]
        good_col_3 = [1]
        good_col_4 = [1]
        good_col_5 = [-1]
        good_col_6 = [1, -1, 1, 1, 1, 1]
        good_col_7 = [-1]

        #create a good board using good columns
        good_board = [good_col_1, good_col_2, good_col_3, good_col_4,
                      good_col_5, good_col_6, good_col_7]

        #compare the dummy board to the good board that's the been run through
        #the print board function
        self.view.print_board(good_board)
        self.assertEqual(mock_stdout.getvalue(), dummyboard)

if __name__ == '__main__':
    unittest.main()

