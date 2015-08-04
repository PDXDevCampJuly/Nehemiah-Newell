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

	def remove_customer(self, name):
		del self.customers[name]

	def show_customer_info(self, name):
		self.customers[name].banking()

	def customer_deposit(self, name, accountNumber, amount):
		self.customers[name].accounts[accountNumber].deposit(amount)

	def customer_withdraw(self, name, accountNumber, amount):
		self.customers[name].accounts[accountNumber].withdraw(amount)

	def make_customer_account(self, name, amount, accountType="Checking Account"):
		self.customers[name].open_account(amount, accountType)

	def remove_customer_account(self, name, accountNumber):
		self.customers[name].close_account(accountNumber)

	def monthly_interest(self):
		for customer in self.customers:
			for saving in self.customers[customer].accounts:
				saving.interest(self.savings_interest)