###
#defines an Person class
###
import Account

class Person(object):
	"""Holds information on Person holding the account"""
	def __init__(self, name, email):
		fullName = name.split()
		self.first_name = fullName[0]
		self.last_name = fullName[1]
		self.email = email
		self.accounts = []

	def open_account(self, balance, accountType = "Checking Account"):
		self.accounts.append(Account.Account(balance, self, accountType))

	def close_account(self, account_number):
		self.accounts.pop(account_number)

	def banking(self):
		for inx, investments in enumerate(self.accounts):
			print("Account {} is a {}".format(inx, investments.accountType))