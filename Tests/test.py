from Game.game import Game
import unittest


class GameTests(unittest.TestCase):
    """
        Testing the game win cases.
    """

    def setUp(self) -> None:
        return super().setUp()

    def testDiagWin(self):
        game = Game()
        game.put_piece(1)
        game.put_piece(2)
        game.put_piece(2)
        game.put_piece(3)
        game.put_piece(3)
        game.put_piece(4)
        game.put_piece(3)
        game.put_piece(4)
        game.put_piece(4)
        game.put_piece(6)
        game.put_piece(4)
        self.assertEqual(game.check_winner_diag(), "X ")

    def testRowWin(self):
        game = Game()
        game.put_piece(1)
        game.put_piece(1)
        game.put_piece(2)
        game.put_piece(2)
        game.put_piece(3)
        game.put_piece(3)
        game.put_piece(4)
        game.put_piece(6)
        self.assertEqual(game.check_winner_row(), "X ")

    def testColWin(self):
        game = Game()
        game.put_piece(1)
        game.put_piece(2)
        game.put_piece(1)
        game.put_piece(2)
        game.put_piece(1)
        game.put_piece(2)
        game.put_piece(1)
        self.assertEqual(game.check_winner_col(), "X ")
