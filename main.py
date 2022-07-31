from Board.board import Board
from Game.game import Game


def main():
    game = Game()
    game.put_piece(1)
    game.put_piece(1)
    game.put_piece(2)
    game.put_piece(1)
    game.put_piece(3)
    game.put_piece(2)
    game.put_piece(4)
    print(game.__str__())
    print(game.check_winner_col())
    print(game.check_winner_row())
    print(game.check_winner_diag())


if __name__ == "__main__":
    main()
