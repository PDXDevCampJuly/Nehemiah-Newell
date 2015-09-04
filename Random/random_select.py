from random import randrange

randomlist = []

def get_random_numbers(number_of_rolls = 10, upperlimit = 100):
	for count in range(number_of_rolls):
		randomlist.append(randrange(upperlimit))
get_random_numbers()
print(randomlist)