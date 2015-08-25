__author__ = 'jbroxton'

from connect_4_model import Connect_Four_Model
from connect_4_view import Connect_Four_View

class Connect_Four_Controller:
    """This object controls game play for the Connect 4 game"""

    def __init__(self):
        """Initializes a new game of Connect 4"""

        #This holds the game's model
        self.game_state = Connect_Four_Model()

        #This is the current display
        self.game_display = Connect_Four_View()

    def handoff_board(self):
        """Hands off the board to the current player """

        return self.game_state.get_board()

    def play_turn(self):
        """This is where the player plays a turn"""


        current_board = self.handoff_board()

        now_playing = self.switch_player()

        self.game_display.print_board(current_board)

        self.game_display.prompt_turn(self.mask_player(now_playing))

        try:
            move = int(input()) -1
        except ValueError:
            move = 10

        while not self.check_move_validity(current_board,move):
            try:
                move = int(input()) -1
            except ValueError:
                move = 10

        current_board[move].append(now_playing)
        self.game_state.update_board(current_board)


    def mask_player(self, player_value):

        if player_value == -1:
            return "Black"
        else:
            return "Red"

    def check_game_status(self, board):
        """Verifies if a player has won, if the game is tied, or if the
        game play switches turns
        :param board: A list of lists that represents the board
        :return: An int, 42 means win, anything else means no winner
        """

        #declare column height variables
        column_height = [len(board[0][:]), len(board[1][:]), len(board[2][:]),
                len(board[3][:]), len(board[4][:]), len(board[5][:]),
                len(board[6][:])]

        #check for vertical win by comparing values in each column
        for count, column in enumerate(board):
            if (column_height[count] >= 4 and column[0] == column[1] and
                        column[1] == column[2] and column[2] == column[3]):
                return 42
            elif (column_height[count] >= 5 and column[1] == column[2] and
                          column[2] == column[3] and column[3] == column[4]):
                return 42
            elif (column_height[count] >= 6 and column[2] == column[3] and
                          column[3] == column[4] and column[4] == column[5]):
                return 42


        #check for the correct minimum number of pieces in each column
        #compare values in each adjacent column for 4 pieces in a diagonal up
        for column in range(4):
            if (column_height[column] >= 1 and column_height[column+ 1] >= 2
                        and column_height[column+ 2] >= 3 and
                        column_height[column+ 3] >= 4 and board[column][0] ==
                        board[column + 1 ][1] and board[column + 1][1] ==
                        board[column + 2][2] and board[column + 2 ][2] ==
                        board[column + 3][3]):
                return 42

            elif (column_height[column] >= 2 and column_height[column+ 1] >= 3
                        and column_height[column+ 2] >= 4 and
                        column_height[column+ 3] >= 5 and board[column][1] ==
                        board[column + 1 ][2] and board[column + 1][2] ==
                        board[column + 2][3] and board[column + 2 ][3] ==
                        board[column + 3][4]):
                return 42

            elif (column_height[column] >= 3 and column_height[column+ 1] >= 4
                        and column_height[column+ 2] >= 5 and
                        column_height[column+ 3] >= 6 and board[column][2] ==
                        board[column + 1 ][3] and board[column + 1][3] ==
                        board[column + 2][4] and board[column + 2 ][4] ==
                        board[column + 3][5]):
                return 42

        #check for the correct minimum number of pieces in each column
        #compare values in each adjacent column for 4 pieces in a diagonal down
        for column in range(4):
            if (column_height[column] >= 4 and column_height[column+ 1] >= 3
                        and column_height[column+ 2] >= 2 and
                        column_height[column+ 3] >= 1 and board[column][3] ==
                        board[column + 1 ][2] and board[column + 1][2] ==
                        board[column + 2][1] and board[column + 2 ][1] ==
                        board[column + 3][0]):
                return 42


            elif (column_height[column] >= 5 and column_height[column+ 1] >= 4
                        and column_height[column+ 2] >= 3 and
                        column_height[column+ 3] >= 2 and board[column][4] ==
                        board[column + 1 ][3] and board[column + 1][3] ==
                        board[column + 2][2] and board[column + 2 ][2] ==
                        board[column + 3][1]):
                return 42

            elif (column_height[column] >= 6 and column_height[column+ 1] >= 5
                        and column_height[column+ 2] >= 4 and
                        column_height[column+ 3] >= 3 and board[column][5] ==
                        board[column + 1 ][4] and board[column + 1][4] ==
                        board[column + 2][3] and board[column + 2 ][3] ==
                        board[column + 3][2]):
                return 42


        for row in range(6):
            for column in range(4):
                if (column_height[column - 1] >= row and column_height[column]
                    >= row and column_height[column + 1] >= row and
                    column_height[column + 2] >= row):
                    try:
                        if (board[column][row] == board[column + 1][row] and
                            board[column + 1][row] == board[column + 2][row]
                            and board[column + 2][row] ==
                            board[column + 3][row]):
                            return 42
                    except IndexError:
                        break
        # if the sum of the values of the board == 42, the game ends in a tie
        if (len(board[0][:]) + len(board[1][:]) + len(board[2][:]) +
                len(board[3][:]) + len(board[4][:]) + len(board[5][:]) +
                len(board[6][:]) == 42):
            return 1



        #if none of these conditions are true: no winner, no tie - return 0
        return 0


    def switch_player(self):
        """Tells the model to switch the current player"""

        return self.game_state.flip_current_player()


    def close_game(self):
        """Exits the game with a fond farewell """

        self.game_display.print_goodbye()
        exit()


    def check_move_validity(self, board, move):
        """Verifies if a move is valid or invalid"""
        try:
            if len(board[move][:]) < 6:
                return True
            else:
                return False
        except IndexError:
            return False

    def check_play_again(self):
        """Asks the player if they would like to play again"""

        self.game_display.prompt_play_again()

        play_again_prompt = input()

        if play_again_prompt == 'y':
            self.game_state.reset_state()
        else:
            self.close_game()

    def main(self):

        self.game_display.print_greeting()

        self.game_display.print_rules()

        flag = 0

        while True:
            while flag == 0:
                self.play_turn()
                flag = self.check_game_status(self.handoff_board())
            self.game_display.print_board(self.handoff_board())
            if flag == 1:
                self.game_display.print_tie()
            elif flag == 42:
                self.game_display.print_win(self.mask_player(self.game_state.get_current_player()))
            self.check_play_again()
            flag = 0



if __name__ == '__main__':
	game = Connect_Four_Controller()
	game.main()







