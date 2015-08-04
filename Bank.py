###
# Defines the Bank
###
from Person import Person

class Bank(object):
	"""Bank information stored here"""
	def __init__(self):
		self.customers = {}
		self.vault = -10.00
		self.savings_interest = .3

	def new_customer(self, name, email):
		self.customers[name] = Person(name, email)

	def monthly_interest(self):
		for customer in self.customers:
			for saving in self.customers[customer].accounts:
				saving.interest(self.savings_interest)