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
		if money <= self.balance:
			self.balance -= money
		else:
			"Bounced Check"

	def check_balance(self):
		return self.balance

	def print_balance(self):
		print('${:,.2f}'.format(self.balance))

	def interest(self, percentage):
		self.balance = round((self.balance + (self.balance * percentage)), 2)
