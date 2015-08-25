__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_message_for_end_of_game(unittest.TestCase):
    """Test for the message that concludes the game"""

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view


    @patch("sys.stdout",new_callable=StringIO)
    def test_print_goodbye(self,mock_stdout):
        """Test the correct message prints at the end of the game"""

        self.view.print_goodbye()
        self.assertEqual("Thanks for playing! Come back soon!\n"
                         "\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()