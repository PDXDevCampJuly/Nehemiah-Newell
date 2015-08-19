__author__ = 'Nehemiah'

import unittest
from Monster import Monster
from unittest.mock import patch
from io import StringIO

class MyTestCase(unittest.TestCase):
    """Tests the flee function"""

    def setUp(self):
        self.pawn = Monster("pawn")
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.pawn

    @patch('builtins.input', return_value=('y'))
    def test_flee_lower_y(self,inputvalue):
        """Flees for Lower y"""
        self.assertEqual(self.pawn.flee(), True)

    @patch('builtins.input', return_value=('Y'))
    def test_flee_upper_y(self,inputvalue):
        """Flees for Upper Y"""
        self.assertEqual(self.pawn.flee(), True)

    @patch('builtins.input', return_value=('n'))
    def test_flee_lower_n(self,inputvalue):
        """Doesn't flee for Lower n"""
        self.assertEqual(self.pawn.flee(), False)

    @patch('builtins.input', return_value=('N'))
    def test_flee_upper_n(self,inputvalue):
        """Doesn't flee for Upper N"""
        self.assertEqual(self.pawn.flee(), False)

    #I think side effect is getting called on both patches, so it needs an extra
    #entry to not 'run out'
    @patch('builtins.input', side_effect=['af','n', 'n'])
    @patch("sys.stdout",new_callable=StringIO)
    def test_flee_junk(self, mock_output, inputvalue):
        """Loops on junk"""
        self.pawn.flee()
        fleestring = "I don't understand.\n"
        self.assertEqual(fleestring, mock_output.getvalue())
        self.assertEqual(self.pawn.flee(), False)


if __name__ == '__main__':
    unittest.main()
