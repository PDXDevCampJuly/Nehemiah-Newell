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

def save_primes(primeNumbers ,pathName = "factorial.txt"):
		with open(pathName,'w') as f:
			for number in primeNumbers:
				f.write(str(number) + "\n")
def main():
		argue = len(argv)

		if argue <= 1 or argue > 3:
			print("Usage: primeFact.py number <filename>")
			quit()
		elif argue == 2:
			primeFound = fact_search(int(argv[1]))
			save_primes(primeFound)
		elif argue == 3:
			primeFound = fact_search(int(argv[1]))
			save_primes(primeFound, argv[3])

if __name__ == '__main__':
	main()