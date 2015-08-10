#This should encode a text file.

from sys import argv

def detransform(pathName):
	returnString = ""
	with open(pathName,'r') as f:
		message = f.read()
	if len(message.split()[0]) <= 3:
		for word in message.split(" "):
			thisWord = int(word)
			returnString += chr(thisWord)
		return returnString
	else:
		for word in message.split(" "):
			astiLength = int(word[0])
			thisWord = int(word[3:3+astiLength])
			returnString += chr(thisWord)
		return returnString
def make_public(privateString,pathName = "open.txt"):
	with open(pathName,'w') as f:
		f.write(privateString)
def main():
	numberOfArguments = len(argv)

	if numberOfArguments == 1:
		message = input("What file would you like to decrypt >> ")
		publicText = detransform(message)
		make_public(publicText)
	elif numberOfArguments == 2:
		publicText = detransform(argv[1])
		make_public(publicText)
	elif numberOfArguments == 3:
		publicText = detransform(argv[1])
		make_public(publicText, argv[2])
	else:
		print("Usage: decode.py <sourcename> <filename")


if __name__ == '__main__':
	main()