#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint
from copy import deepcopy

words = ["test"]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words
   # and make the randomly selected word into a list object
   list_of_words = ["hangman", "hangperson", "hangwomen", "hanging judge", "hanging rope"]
   listedWord = list(list_of_words[randint(0,4)])
   #print(listedWord)
   

   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   currentState = deepcopy(listedWord)
   guessedLetters = []

   for inx, char in enumerate(currentState):
   	  currentState[inx] = "_"
   #print(currentState)
   # Print the initial state of the game
   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:
      thisGuess = userGuess(guessedLetters)
      updateState(thisGuess,currentState)
      printHangperson(currentState)
   # Determine if the user won or lost, and then tell them accordingly
   if numWrong >= 6:
   	  print("\nYou were hung till dead!!!\n")
   else:
   	  print("\nYou proved innocent of crimes against English.\n")

# This helpful function prompts the user for a guess,
# accepting only single letters.
# DO NOT CHANGE
#
# returns a letter
def userGuess(guessedLetters):
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   while len(guess) != 1 or guessedLetters.count(guess) != 0:
       if guess == "exit":
       	  exit()
       elif guessedLetters.count(guess) != 0:
       	  guess = input("You already tried that arguement! Try something else or say 'exit' ")       	
       else:
       	  guess = input("Enter !only! one letter or say 'exit' to stop playing ")
   guessedLetters.append(guess)
   return guess


# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong
   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)
   # If it isn't, tell the user and update the numWrong var
   if numInWord == 0:
   	  numWrong += 1
   	  print("Bad guess, criminal. You're " + str(6 - numWrong) + " guesses away from a hang'n!")
   # If it is, congratulate them and update the state of the game.
   else:
   	  print("Hmm, you might have a case there. You filled in " + str(numInWord) + " facts.")
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   for index, char in enumerate(listedWord):
   	  if char == guess:
   	     currentState[index] = guess

   return currentState


# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

# This line runs the program on import of the module
hangperson()
