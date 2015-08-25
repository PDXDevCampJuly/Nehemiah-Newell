__author__ = 'jbroxton'


class Connect_Four_View:
    """This object controls game play for the Connect 4 game"""


    def print_greeting(self):
        """This greets the player with a print statement"""

        print("Greetings! Welcome to Connect Four!\n")


    def print_rules(self):
        """This function prints the rules that govern gameplay"""

        print("Connect Four is a two-player connection game in which "
             "the players take turns dropping pieces from the top "
             "into a seven-column, six-row vertically suspended "
             "grid. The pieces fall straight down, occupying the "
             "next available space within the column. The objective "
             "of the game is to connect four of one's own pieces of "
             "the same color next to each other vertically, "
             "horizontally, or diagonally before your opponent.\n")


    def print_board(self, board):
        """This function prints the board"""

        for column in reversed(range(0, 6)):
            try:
                if board[0][column] == 1:
                    print('|' + u"\u25EF", end="")
                else:
                    print('|' + u"\u25CF", end="")
            except IndexError:
                print("| ", end="")

            try:
                if board[1][column] == 1:
                    print('|' + u"\u25EF", end="")
                else:
                    print('|' + u"\u25CF", end="")
            except IndexError:
                print("| ", end="")

            try:
                if board[2][column] == 1:
                    print('|' + u"\u25EF", end="")
                else:
                    print('|' + u"\u25CF", end="")
            except IndexError:
                print("| ", end="")

            try:
                if board[3][column] == 1:
                    print('|' + u"\u25EF", end="")
                else:
                    print('|' + u"\u25CF", end="")
            except IndexError:
                print("| ", end="")

            try:
                if board[4][column] == 1:
                    print('|' + u"\u25EF", end="")
                else:
                    print('|' + u"\u25CF", end="")
            except IndexError:
                print("| ", end="")

            try:
                if board[5][column] == 1:
                    print('|' + u"\u25EF", end="")
                else:
                    print('|' + u"\u25CF", end="")
            except IndexError:
                print("| ", end="")

            try:
                if board[6][column] == 1:
                    print('|' + u"\u25EF", end="")
                else:
                    print('|' + u"\u25CF", end="")
            except IndexError:
                print("| ", end="")

            print("|")

        print("===============")
        print("[]           []\n")



    def prompt_turn(self, player):
        """Prompts the player to take a turn"""

        print("{} Player: Please select the column for this turn ".
            format(player))


    def prompt_play_again(self):
        """Asks the player if they would like to play another game"""

        print("Would you care to play again? Yes or No (Y / N) \n")


    def print_win(self, player):
        """This congratulates the player via a print statement"""

        print("Congratulations {}! A Winner is You ".format(player))



    def print_tie(self):
        """This function prints that the game ends in a tie"""

        print("You tied - and playing is half the battle! "
              "(The other is strategy.)\n")


    def print_goodbye(self):
        """This is a farewell print statement"""

        print("Thanks for playing! Come back soon!\n")











