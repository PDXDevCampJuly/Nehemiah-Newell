__author__ = 'Nehemiah'

import unittest
from Monster import Monster

class Test_Heal(unittest.TestCase):
    """Test that the heal function works"""
    def setUp(self):
        self.pawn = Monster("pawn")
        print("Running: ", str(self._testMethodName) + "\n   " + str(self.shortDescription()) + "\n")

    def tearDown(self):
        del self.pawn


    def test_heal_to_ten(self):
        """Test to see if it heals the monster"""
        self.pawn.health = 5
        self.pawn.heal(5)
        self.assertEqual(self.pawn.health, 10)

    def test_heal_to_twenty(self):
        """Test to see if it doesn't heal past 10"""
        self.pawn.health = 10
        self.pawn.heal(10)
        self.assertEqual(self.pawn.health, 10)

    def test_heal_to_junk_data(self):
        """Test to see if it doesn't crash at junk"""
        self.pawn.health = 5
        self.pawn.heal('as')
        self.assertEqual(self.pawn.health, 5)

if __name__ == '__main__':
    unittest.main()
