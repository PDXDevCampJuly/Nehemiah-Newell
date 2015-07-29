#Largest palindrome product of two 3 digit numbers

def palindrome_seeker(lowerBound, upperBound):
	found = []
	for x in range(lowerBound, upperBound + 1):
		for y in range(x+1, upperBound + 1):
			checkThis = str(x*y)
			if checkThis == checkThis[::-1]:
				found.append(int(checkThis))
	found.sort()
	return found[-1]


def main():
	print(palindrome_seeker(100,999))

if __name__ == '__main__':
	main()