__author__ = 'Nehemiah'

import unittest
from Monster import Monster

class Test_Reset(unittest.TestCase):
    """Checks if the game is in a state where it can advance"""

    def setUp(self):
        self.pawn = Monster("pawn")
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.pawn

    def test_reset_status(self):
        """Resets Monsters status to 'Out of Tokyo'"""
        self.pawn.status = "K.O.'d"
        self.pawn.reset()
        self.assertEqual(self.pawn.status, "Out of Tokyo")

    def test_reset_health(self):
        """Resets Monsters Health to 10"""
        self.pawn.health = 10000
        self.pawn.reset()
        self.assertEqual(self.pawn.health, 10)

    def test_reset_victory(self):
        """Resets Monsters Victory Points to 0"""
        self.pawn.victory_points = -12
        self.pawn.reset()
        self.assertEqual(self.pawn.victory_points, 0)

if __name__ == '__main__':
    unittest.main()
