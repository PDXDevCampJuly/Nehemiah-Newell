# This will fake a die
from random import randint

def roll(max):
	r = randint(1,max)
	return r

def roll_a_bunch(max, numOfDice=4):
	rolls = []
	for i in range(numOfDice):
		rolls.append(roll(max))

	return rolls

def roll_distro(max, numOfDice=4):
	#Roll a bunch of dice
	rolls = roll_a_bunch(max,numOfDice)

	distribution = {}

	#count what's rolled
	for each in rolls:
		currentCount = distribution.get(each, 0)
		print("Current count of", currentCount)
		currentCount += 1
		distribution[each] = currentCount

	output = ""
	for roll in distribution:
		output += "Number " + str(roll) + " was rolled " + str(distribution[roll]) + " times\n"

	print(output)
#The dice hate you
def storyteller(numOfDice):
	success = 0
	failure = 0
	for i in range(numOfDice):
		r = randint(-3, 10)
		if r <= 0:
			r = 1
		if r < 7:
			print(r, end = " ")
			failure += 1
		if r >= 7:
			print(r, end = " ")
			success += 1
	print("\n", success, " Success", failure, " Failures")