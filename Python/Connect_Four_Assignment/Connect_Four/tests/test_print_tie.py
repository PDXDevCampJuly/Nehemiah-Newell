__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_message_if_game_tied(unittest.TestCase):
    """Check that the correct message prints for a tie"""

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view


    @patch("sys.stdout",new_callable=StringIO)
    def test_print_tie(self,mock_stdout):
        """Test the correct message in the event of a tie"""

        self.view.print_tie()
        self.assertEqual("You tied - and playing is half the battle! "
                         "(The other is strategy.)\n"
                         "\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()