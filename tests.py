import unittest
from game.board import Board
from game.game import TicTacToe
from game.constants import EMPTY_SLOT

class TestBoard(unittest.TestCase):
    board = Board()

    def test_horizontal_win(self):
        # Test a horizontal win on the top row
        self.board.positions = ["X", "X", "X", EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
        self.assertTrue(self.board.check_win("X"))
        
        # Test a horizontal win on the middle row
        self.board.positions = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, "O", "O", "O", EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
        self.assertTrue(self.board.check_win("O"))
        
        # Test a horizontal win on the bottom row
        self.board.positions = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, "X", "X", "X"]
        self.assertTrue(self.board.check_win("X"))
        
    def test_vertical_win(self):
        # Test a vertical win on the left column
        self.board.positions = ["O", EMPTY_SLOT, EMPTY_SLOT, "O", EMPTY_SLOT, EMPTY_SLOT, "O", EMPTY_SLOT, EMPTY_SLOT]
        self.assertTrue(self.board.check_win("O"))
        
        # Test a vertical win on the middle column
        self.board.positions = [EMPTY_SLOT, "X", EMPTY_SLOT, EMPTY_SLOT, "X", EMPTY_SLOT, EMPTY_SLOT, "X", EMPTY_SLOT]
        self.assertTrue(self.board.check_win("X"))
        
        # Test a vertical win on the right column
        self.board.positions = [EMPTY_SLOT, EMPTY_SLOT, "O", EMPTY_SLOT, EMPTY_SLOT, "O", EMPTY_SLOT, EMPTY_SLOT, "O"]
        self.assertTrue(self.board.check_win("O"))
        
    def test_diagonal_win(self):
        # Test a diagonal win from top left to bottom right
        self.board.positions = ["X", EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, "X", EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, "X"]
        self.assertTrue(self.board.check_win("X"))
        
        # Test a diagonal win from bottom left to top right
        self.board.positions = [EMPTY_SLOT, EMPTY_SLOT, "O", EMPTY_SLOT, "O", EMPTY_SLOT, "O", EMPTY_SLOT, EMPTY_SLOT]
        self.assertTrue(self.board.check_win("O"))
        
    def test_no_win(self):
        # Test no win on a completely empty self.board.positions
        self.board.positions = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
        self.assertFalse(self.board.check_win("X"))
        
        # Test no win on a partially filled self.board.positions
        self.board.positions = ["X", EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, "O", EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
        self.assertFalse(self.board.check_win("O"))

class TestPlayerMove(unittest.TestCase):
    game = TicTacToe()

    def test_player_move(self):
        # Test a bot move on a partially filled board
        self.game.board.positions = ["O", EMPTY_SLOT, "X", "X", "X", "O", EMPTY_SLOT, "O", EMPTY_SLOT]
        player_symbol = "X"
        move = self.game.player_move(player_symbol)
        self.assertEqual(move, 6)
        
        # Test a bot move that blocks the opponent's win
        self.game.board.positions = ["X", EMPTY_SLOT, EMPTY_SLOT, "O", "X", EMPTY_SLOT, EMPTY_SLOT, "O", EMPTY_SLOT]
        player_symbol = "O"
        move = self.game.player_move(player_symbol)
        self.assertEqual(move, 8)

if __name__ == '__main__':
    unittest.main()

