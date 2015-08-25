__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_print_win(unittest.TestCase):
    """Check that it prints correctly when"""

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view

    @patch("sys.stdout",new_callable=StringIO)
    def test_print_congratulations(self,mock_stdout):
        """Test for congratulatory message for the correct player"""
        fake_player = "Red"
        prompt_string = "Congratulations {}! A Winner is You ".\
            format(fake_player)
        self.view.print_win(fake_player)
        self.assertEqual("Congratulations Red! A Winner is You "
                         "\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()