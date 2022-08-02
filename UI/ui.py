from Game.game import *


class UI:

    def __init__(self) -> None:
        self.__game = Game()

    @staticmethod
    def welcome():
        print("\tHello players, and welcome to an honest game of ConnectFour!\n" +
              "\tMay the best win!\n")

    def move(self) -> None:
        try:
            print(self.__game.__str__())
            col = int(input("Enter place to position: "))
            self.__game.put_piece(col)
        except BoardException as be:
            print(be)

    def play(self):
        row_win = self.__game.check_winner_row()
        col_win = self.__game.check_winner_col()
        diag_win = self.__game.check_winner_diag()
        while row_win == col_win == diag_win == "no winner":
            row_win = self.__game.check_winner_row()
            col_win = self.__game.check_winner_col()
            diag_win = self.__game.check_winner_diag()
            self.move()

        if row_win == "X ":
            print("Player 1 won by connecting 4 dots on a row!")
        elif row_win == "Y ":
            print("Player 2 won by connecting 4 dots on a row!")

        if col_win == "X ":
            print("Player 1 won by connecting 4 dots on a column!")
        elif col_win == "Y ":
            print("Player 2 won by connecting 4 dots on a column!")

        if diag_win == "X ":
            print("Player 1 won by connecting 4 dots on a diagonal!")
        elif diag_win == "X ":
            print("Player 2 won by connecting 4 dots on a diagonal!")
