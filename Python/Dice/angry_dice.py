# Create and run a game of angry dice
from dieClass import Die

#Create an Angry Dice object
class Angry_Dice:
	#Set up a game, taking no parameters
	def __init__(self,):
		# Declare a master list of die values
		self.masterlist = ["1","2","ANGRY","4","5","6"]
		# Declare the dice
		self.angryDieA = Die(self.masterlist)
		self.angryDieB = Die(self.masterlist)
		# set stage to 1
		self.currentStage = 1
		# set six watchflags to false
		self.invalidFlagA = False
		self.invalidFlagB = False

	#Roll the angry dice
	def roll_the_dice(self, rollString):
		returnString = ""
		# if A in string, roll the A die.
		if 'a' in rollString.lower():
			self.angryDieA.roll_die()
			#A hasn't been held
			self.invalidFlagA = False
			returnString = returnString + 'a'
		# if B in string, roll the B die.
		if 'b' in rollString.lower():
			self.angryDieB.roll_die()
			#B hasn't been held
			self.invalidFlagB = False
			returnString = returnString + 'b'
		#return the returnString
		return returnString

	#Print round status
	def print_round(self):
		print("You rolled:\n   a =[ {} ]\n   b =[ {} ]\n".format(self.angryDieA.__repr__(),self.angryDieB.__repr__()))

	#Check and advance through stages
	def stage_check(self):
		# get the current dice values into a string
		currentValues = self.angryDieA.__repr__() + self.angryDieB.__repr__()
		# if two angrys, recent to stage one
		if "ANGRYANGRY" == currentValues:
			self.currentStage = 1
			print("WOW, you're ANRGY!\nTime to go back to Stage 1!")
		#else stage one logic
		elif self.currentStage == 1:
			if "1" in currentValues and "2" in currentValues:
				self.currentStage = 2
		#else stage two logic
		elif self.currentStage == 2:
			if "ANGRY" in currentValues and "4" in currentValues:
				self.currentStage = 3
		#else stage three logic
		if self.currentStage == 3:
			if "5" in currentValues and "6" in currentValues:
				print("You'be won! Calm down!")
				exit()
		#print current stage
		print("You are in Stage {}".format(str(self.currentStage)))

	#Make sure only valid dice are held
	def valid_check(self):
		if self.currentStage == 1:
			if self.angryDieA.__repr__() not in '1' and self.angryDieA.__repr__() not in '2':
				self.invalidFlagA = True
			if self.angryDieB.__repr__() not in '1' and self.angryDieB.__repr__() not in '2':
				self.invalidFlagB = True
		if self.currentStage == 2:
			if self.angryDieA.__repr__() not in 'ANGRY' and self.angryDieA.__repr__() not in '4':
				self.invalidFlagA = True
			if self.angryDieB.__repr__() not in 'ANGRY' and self.angryDieB.__repr__() not in '4':
				self.invalidFlagB = True
		if self.currentStage == 3:
			if self.angryDieA.__repr__() not in '5':
				self.invalidFlagA = True
			if self.angryDieB.__repr__() not in '5':
				self.invalidFlagB = True

	#Play the game
	def play(self):
		#set the roll string to roll both dice
		rollString = 'ab'
		#Great the player
		input("Welcome to Angry Dice! Roll the two dice until you get thru the 3 Stages!\nStage 1 you need to roll 1 & 2\nStage 2 you need to roll ANGRY & 4\nStage 3 you need to roll 5 & 6\nYou can lock a die needed for your current stage and just roll the other one, but beware!\nIf you ever get 2 ANGRY's at once, you have to restart to Stage 1!\nAlso, you can never lock a 6! That's cheating!\nTo roll the dice, simply input the name of the die you want to roll.\nTheir names are a and b.\nTo roll the dice, simply input the name of the die you want to roll.\nTheir names are a and b.\n\nPress ENTER to start.\n")
		#Roll the dice
		self.roll_the_dice(rollString)
		#Enter body of game
		while True:
			#as long as they aren't holding a six, coninue the game
			if self.invalidFlagA == False and self.invalidFlagB == False:
				#print out round
				self.print_round()
				#check the stage conditons to advance the game
				self.stage_check()
			else:
				#Tell them they are cheating
				if self.invalidFlagA == True and self.invalidFlagB == True:
					print("You're cheating! You cannot lock both of those dice! you cannot\nwin until you reroll it!")
				elif self.invalidFlagA == True:
					print("You're cheating! You cannot lock a {}! you cannot\nwin until you reroll it!".format(self.angryDieA.__repr__()))
				else:
					print("You're cheating! You cannot lock a {}! you cannot\nwin until you reroll it!".format(self.angryDieB.__repr__()))
				#print out round
				self.print_round()
			#check for held sixes
			self.valid_check()
			#get the input
			rollString = input("Roll dice: ")
			#roll the dice
			self.roll_the_dice(rollString)

if __name__ == '__main__':
	game = Angry_Dice()
	game.play()