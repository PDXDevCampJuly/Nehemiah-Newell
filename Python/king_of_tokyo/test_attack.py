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


    def test_takes_damage(self):
        """Test if health goes down"""
        self.pawn.health = 10
        self.assertEqual(self.pawn.attack(3), 7)

    def test_is_k_o_d(self):
        """Tests if Status Changes"""
        self.pawn.health = 5
        self.pawn.attack(5)
        self.assertEqual(self.pawn.status, "K.O.'d")

    def test_junk_damage(self):
        """Test if it doesn't crash"""
        self.pawn.health = 10
        self.assertEqual(self.pawn.attack("adf"), 10)




if __name__ == '__main__':
    unittest.main()
