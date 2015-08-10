from sys import argv
from math import sqrt
from primeSearch import prime_search

class breakIt(Exception):
	"""Breaks you out a loop"""
	pass

def fact_search(seek):
		squareRoot = sqrt(seek)
		newNum = seek
		primes = prime_search(seek)
		facts = []
		while newNum != 1:
			for num in range(0, seek):	
				while newNum % primes[num] == 0:
					facts.append(primes[num])
					newNum = newNum//primes[num]
				if newNum == 1:
					break

		return facts

def save_primes(primeNumbers, originalNumber, pathName = "factorial.txt"):
		distinct = set(primeNumbers)
		outString = []
		for num in distinct:
			counting = primeNumbers.count(num)
			if counting == 1:
				outString.append(str(num))
			else:
				outString.append(str(num) + "^" + str(counting))
		output = str(originalNumber) + " = " + " * ".join(outString)


		with open(pathName,'w') as f:
			f.write(output)
def main():
		argue = len(argv)

		if argue <= 1 or argue > 3:
			print("Usage: primeFact.py number <filename>")
			quit()
		elif argue == 2:
			primeFound = fact_search(int(argv[1]))
			save_primes(primeFound, argv[1])
		elif argue == 3:
			primeFound = fact_search(int(argv[1]))
			save_primes(primeFound, argv[1], argv[2])

if __name__ == '__main__':
	main()