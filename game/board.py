from .constants import EMPTY_SLOT

class Board:

    def __init__(self):
        self.positions = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
        self.winning_possibilities = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

    def print_board(self):
        print(self.positions[0] + "|" + self.positions[1] + "|" + self.positions[2])
        print("-+-+-")
        print(self.positions[3] + "|" + self.positions[4] + "|" + self.positions[5])
        print("-+-+-")
        print(self.positions[6] + "|" + self.positions[7] + "|" + self.positions[8])


    # Define a function to check if a given player has won the game
    def check_win(self, player):
        for possibility in self.winning_possibilities:
            if (
                self.positions[possibility[0]] == player
                and self.positions[possibility[1]] == player
                and self.positions[possibility[2]] == player
            ):
                return True
        return False

