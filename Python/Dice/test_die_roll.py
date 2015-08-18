__author__ = 'Nehemiah'

import unittest
from dieClass import Die

class die_roll_test(unittest.TestCase):
    """Test the functionality of the die class roll function"""

    def setUp(self):
        self.possible_values = [1,2,3,"Dog",'Cat','Hippo']
        self.new_die = Die(self.possible_values)
        print(self.shortDescription())

    def test_roll_once(self):
        """Roll the die once and make sure that the return value is in possible values"""
        self.assertIn(self.new_die.roll_die(),self.possible_values,
                      "Rolled value was not in possible values of Die")
        print("Value in possible values")

    def test_rolled_value_changes(self):
        """Roll the a number of times to make sure it changes value"""

        holding_value = self.new_die.roll_die()
        for i in range(10):
            if self.new_die.roll_die() != holding_value:
                print("Rolled Die Value {} is different from Holding Value {}"
                      .format(self.new_die.currentValue,holding_value))
                self.assertTrue(True)
                return
        self.assertTrue(False,"Die value did not change from holding value for 10 rolls.")

    def test_current_value_is_updated_to_rolled_value(self):
        """Test that current value is updated to rolled value."""
        self.new_die.currentValue = "A random string."
        thisValue = self.new_die.roll_die()
        self.assertEqual(thisValue,self.new_die.currentValue,
                         "Current and return value differ")
        print("The current value was updated to the rolled value")

    def tearDown(self):
        print("Just ran: ")
        print(self._testMethodName)
        print
if __name__ == '__main__':
    unittest.main()
