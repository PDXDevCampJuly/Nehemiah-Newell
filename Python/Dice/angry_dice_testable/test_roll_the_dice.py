__author__ = 'Nehemiah'

import unittest
import angry_dice_testable

class test_roll_the_dice(unittest.TestCase):
    """Test the functionality of the angry dice roll the dice function"""

    def setUp(self):
        self.game = angry_dice_testable.Angry_Dice()
        print(self.shortDescription())

    def tearDown(self):
        print("Just ran: ")
        print(self._testMethodName)
        print()
        del self.game

    def test_roll_A(self):
        """Can it roll A"""
        holding_value = self.game.angryDieA.currentValue
        for i in range(10):
            self.game.roll_the_dice("a")
            if self.game.angryDieA.currentValue != holding_value:
                self.assertTrue(True)
                print("Die A can be rolled")
                return
        self.assertTrue(False,"Die value did not change from holding value for 10 rolls.")

    def test_roll_B(self):
        """Can it roll B"""
        holding_value = self.game.angryDieB.currentValue
        for i in range(10):
            self.game.roll_the_dice("b")
            if self.game.angryDieB.currentValue != holding_value:
                self.assertTrue(True)
                print("Die B can be rolled")
                return
        self.assertTrue(False,"Die value did not change from holding value for 10 rolls.")

    def test_leaves_invalid_flag_A(self):
        """Does it set invalidFlag A properly"""
        self.game.invalidFlagA = False
        self.game.roll_the_dice("a")
        self.assertEqual(False,self.game.invalidFlagA,"Changed a flag it shouldn't have.")
        print("Correctly, it didn't set an unset flag")

    def test_changes_invalid_flag_A(self):
        """Does it set invalidFlag A properly"""
        self.game.invalidFlagA = True
        self.game.roll_the_dice("a")
        self.assertEqual(False,self.game.invalidFlagA,"Didn't changed a flag it should have.")
        print("Correctly, it unset a set flag")

    def test_leaves_invalid_flag_B(self):
        """Does it set invalidFlag B properly"""
        self.game.invalidFlagB = False
        self.game.roll_the_dice("b")
        self.assertEqual(False,self.game.invalidFlagB,"Changed a flag it shouldn't have.")
        print("Correctly, it didn't set an unset flag")

    def test_changes_invalid_flag_B(self):
        """Does it set invalidFlag B properly"""
        self.game.invalidFlagB = True
        self.game.roll_the_dice("b")
        self.assertEqual(False,self.game.invalidFlagB,"Didn't changed a flag it should have.")
        print("Correctly, it unset a set flag")

    def test_invalid_input(self):
        """Can it deal with invalid input"""
        self.game.invalidFlagB = True
        self.game.invalidFlagA = True
        holding_valueA = self.game.angryDieA.currentValue
        holding_valueB = self.game.angryDieB.currentValue
        self.game.roll_the_dice("dfjkf")
        self.assertEqual(True,self.game.invalidFlagB,"It unset B flag when it shouldn't have.")
        self.assertEqual(True,self.game.invalidFlagA,"It unset A flag when it shouldn't have.")
        self.assertEqual(holding_valueB,self.game.angryDieB.currentValue,"It unset B flag when it shouldn't have.")
        self.assertEqual(holding_valueA,self.game.angryDieA.currentValue,"It unset A flag when it shouldn't have.")
        print("Invalid input was correctly handled.")

    def test_no_input(self):
        """Can it deal with no input"""
        self.game.invalidFlagB = True
        self.game.invalidFlagA = True
        holding_valueA = self.game.angryDieA.currentValue
        holding_valueB = self.game.angryDieB.currentValue
        self.game.roll_the_dice("")
        self.assertEqual(True,self.game.invalidFlagB,"It unset B flag when it shouldn't have.")
        self.assertEqual(True,self.game.invalidFlagA,"It unset A flag when it shouldn't have.")
        self.assertEqual(holding_valueB,self.game.angryDieB.currentValue,"It unset B flag when it shouldn't have.")
        self.assertEqual(holding_valueA,self.game.angryDieA.currentValue,"It unset A flag when it shouldn't have.")
        print("No input was correctly handled.")

    def test_input_noise(self):
        """Can it deal with noise in input"""
        self.game.invalidFlagB = True
        self.game.invalidFlagA = True
        self.game.roll_the_dice("   nfk li  iii ibi")
        self.assertEqual(False,self.game.invalidFlagB,"It failed to roll B Die when it should have.")
        self.assertEqual(True,self.game.invalidFlagA,"It rolled A Die when it shouldn't have.")
        print("It correctly filtered out noise and rolled B Die.")

if __name__ == '__main__':
    unittest.main()
