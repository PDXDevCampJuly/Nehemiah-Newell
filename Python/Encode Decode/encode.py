#This should encode a text file.

from sys import argv
from random import randint

def transform(publicString):
	returnString = []
	strength = input("What strength of encryption do you want, (w)eak/(s)trong? \n >>> ")
	if strength.lower() == 'w':
		for char in publicString:
			returnString.append(str(ord(char)))
		return ' '.join(returnString)
	elif strength.lower() == 's':
		for char in publicString:
			tempString = ""
			stringLength = str(len(str(ord(char))))
			tempString += stringLength + str(randint(10, 99)) + str(ord(char)) + str(randint(10, 99))
			returnString.append(tempString)
		return ' '.join(returnString)
	else:
		print("Invalid input, input (w)eak or (s)trong")
def make_secret(privateString,pathName = "secret.txt"):
	with open(pathName,'w') as f:
		f.write(privateString)

def main():
	numberOfArguments = len(argv)

	if numberOfArguments == 1:
		message = input("What message would you like to send >> ")
		print(message)
		secretText = transform(message)
		print(secretText)
		make_secret(secretText)
	elif numberOfArguments == 2:
		print(argv[1])
		secretText = transform(argv[1])
		print(secretText)
		make_secret(secretText)
	elif numberOfArguments == 3:
		print(argv[1],argv[2])
		secretText = transform(argv[1])
		print(secretText)
		make_secret(secretText, argv[2])
	else:
		print("Usage: encode.py <message> <filename>")


if __name__ == '__main__':
	main()