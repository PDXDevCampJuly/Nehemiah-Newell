__author__ = 'jbroxton'

import unittest
from unittest.mock import patch
from io import StringIO
from connect_4_view import Connect_Four_View



class test_print_stage(unittest.TestCase):
    """Check that it prints correctly when"""

    def setUp(self):
        self.view = Connect_Four_View()
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.view


    @patch("sys.stdout",new_callable=StringIO)
    def test_print_greeting(self,mock_stdout):
        """Test if the greeting prints correctly"""

        self.view.print_greeting()
        self.assertEqual("Greetings! Welcome to Connect Four!\n"
                         "\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()