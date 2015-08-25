__author__ = 'jbroxton'

class Connect_Four_Model:
    """This object will keep track of persistent data for Connect 4 game"""
    def __init__(self):
        """This sets the initial conditions for the Connect 4 game"""

        #This will be a game board represented by a list of a list of seven
        # buckets of up to six items
        self.board = [[],[],[],[],[],[],[]]
        #Key : player 1 = 1 , player 2 = -1
        self.player = -1

    def get_board(self):
        """Return the current game board"""

        return self.board

    def update_board(self, board):
        """Change the current game board to reflect conditions"""

        #start if statement with accurate number of columns

        if len(board) == 7:
            #iterating through the board
            for column in board:
                #if the height of the column > 6, then the column is invalid
                if len(column) > 6:
                    return
                #if a value in the column is not either a 1 or -1, then the
                #column and board are invalid
                for row in column:
                    if row != 1 and row != -1:
                        return
            #if we make it past the checks, the board is valid
            self.board = board[:]


    def get_current_player(self):
        """Return the current player"""

        return self.player

    def flip_current_player(self):
        """Flip and return the current player"""

        self.player *= -1
        return self.player

    def reset_state(self):
        """Resets game to initial conditions"""

        self.board = [[],[],[],[],[],[],[]]
        self.player = -1



