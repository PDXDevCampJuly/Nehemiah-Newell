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
		self.customers[email] = Person(name, email)

	def remove_customer(self, email):
		del self.customers[email]

	def show_customer_info(self, email):
		self.customers[email].banking()

	def show_all_customers(self):
		for customer in self.customers:
			print("{}.\n email: {}\n".format(self.customers[customer].first_name + " " + self.customers[customer].last_name, customer))

	def customer_deposit(self, email, accountNumber, amount):
		self.customers[email].accounts[accountNumber].deposit(amount)

	def customer_withdraw(self, email, accountNumber, amount):
		self.customers[email].accounts[accountNumber].withdraw(amount)

	def make_customer_account(self, email, amount, accountType="Checking Account"):
		self.customers[email].open_account(amount, accountType)

	def remove_customer_account(self, email, accountNumber):
		self.customers[email].close_account(accountNumber)

	def monthly_interest(self):
		for customer in self.customers:
			for saving in self.customers[customer].accounts:
				saving.interest(self.savings_interest)
	
	def customer_worth(self,email):
		value = 0.0
		for saving in self.customers[email].accounts:
			value += saving.check_balance()
		print("{} is worth ${:,.2f}".format(self.customers[email].first_name + " " + self.customers[email].last_name, value))

#	def menu(self):
#		article = "Wecome to Banking Services! \nWould you like to (a)dd a customer \n(r)emove a customer \na(d)d a account \n(c)lose a account \ncalculate the (w)orth of a customer \nget customer (i)nfo \n dep(o)set or withdraw."
#		flag = True
#		while flag == True:
#			theInput = input("Please enter the desired service: ")
#
#			if theInput.lower() == 'a':
#
#			elif theInput.lower() == 'r':
#
#			elif theInput.lower() == 'd':
#
#			elif theInput.lower() == 'c':
#
#			elif theInput.lower() == 'w':
#
#			elif theInput.lower() == 'i':
#
#			elif theInput.lower() == 'o':

		# start asking for information from the user
		theInput = input("Please enter a action ")
		# and concantitate it.
		article += theInput + "."

		# and output
		print("\n\n")
		print(article)
		print("\n\n")