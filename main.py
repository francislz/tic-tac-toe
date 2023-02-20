import random

EMPTY_SLOT = " "

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

class TicTacToe:
    def __init__(self):
        self.board = Board()

    # Define a function to get the player's move
    def player_move(self, player):
        if player == "X":
            bot_player = "O"
        else:
            bot_player = "X"
        # Check if player can win in the next move
        for i in range(9):
            if self.board.positions[i] == EMPTY_SLOT:
                self.board.positions[i] = bot_player
                if self.board.check_win(bot_player):
                    return i
                self.board.positions[i] = EMPTY_SLOT
        # Check if player can win in the next move
        for i in range(9):
            if self.board.positions[i] == EMPTY_SLOT:
                self.board.positions[i] = player
                if self.board.check_win(player):
                    return i
                self.board.positions[i] = EMPTY_SLOT
        # Choose a random empty square
        while True:
            i = random.randint(0, 8)
            if self.board.positions[i] == EMPTY_SLOT:
                return i

    # Define a function to play the game
    def play_game(self):
        count = 0
        player = "X"
        while True:
            count += 1
            print("Move number " + str(count))
            if EMPTY_SLOT not in self.board.positions:
                self.board.print_board()
                print("Tie game!")
                return
            self.board.print_board()
            if player == "X":
                # player X's turn
                print("Bot X's turn")
                move = self.player_move(player)
            else:
                # player O's turn
                print("Bot O's turn")
                move = self.player_move(player)
            self.board.positions[move] = player
            if self.board.check_win(player):
                self.board.print_board()
                print(player + " wins!")
                return
            if player == "X":
                player = "O"
            else:
                player = "X"

# Play the game
if __name__ == "__main__":
    TicTacToe().play_game()

