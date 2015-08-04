# ##
#defines an Account class
###

class Account(object):
	"""An Account that stores account information"""
	def __init__(self, balance, person, accountType = "checking"):
		self.balance = balance
		self.accountType = accountType
		self.owner = person
	
	def deposit(self, money):
		self.balance += money

	def withdraw(self, money):
		self.balance -= money

	def check_balance(self):
		return self.balance

	def interest(self, percentage):
		self.balance = self.balance + (self.balance * percentage)
