# Define a die class
from sys import argv
from random import choice

class Die:
	"""docstring for Die"""
	def __init__(self, list_of_sides = argv):
		self.possibleValues = list_of_sides[:]
		self.currentValue = self.possibleValues[0]

	def roll_die(self):
		self.currentValue = choice(self.possibleValues)
		return str(self.currentValue)

	def __repr__(self):
		return str(self.currentValue)