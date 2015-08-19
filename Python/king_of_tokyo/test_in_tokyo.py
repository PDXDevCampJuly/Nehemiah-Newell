__author__ = 'Nehemiah'

import unittest
from Monster import Monster

class Test_In_Tokyo(unittest.TestCase):
    """Test the in_tokyo function to see if it responds correctly"""
    def setUp(self):
        self.pawn = Monster("pawn")
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.pawn

    def test_is_in_tokyo(self):
        """Can it see if the monsster is in tokyo"""
        self.pawn.status = "In Tokyo"
        self.assertEqual(self.pawn.in_tokyo(), True)

    def test_isnt_in_tokyo(self):
        """Can it see if the monster isn't in tokyo"""
        self.pawn.status = "Sleeping"
        self.assertEqual(self.pawn.in_tokyo(), False)

    def test_isnt_a_string(self):
        """Can it not break if the value is miss set"""
        self.pawn.status = 321
        self.assertEqual(self.pawn.in_tokyo(), False)

if __name__ == '__main__':
    unittest.main()
