__author__ = 'Nehemiah'

import unittest
from Monster import Monster

class Test_Attack(unittest.TestCase):
    """Test if the mosnter can be attacked and checks for damage correctly"""
    def setUp(self):
        self.pawn = Monster("pawn")
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.pawn


    def test_scores_points(self):
        """Test if victory points goes up"""
        self.pawn.victory_points = 10
        self.assertEqual(self.pawn.score(5), 15)

    def test_winning(self):
        """Tests if Status Changes to WINNING"""
        self.pawn.victory_points = 5
        self.pawn.score(15)
        self.assertEqual(self.pawn.status, "WINNING")

    def test_junk_score(self):
        """Test if it doesn't crash on bad data"""
        self.pawn.victory_points = 10
        self.assertEqual(self.pawn.score("adf"), 10)




if __name__ == '__main__':
    unittest.main()
