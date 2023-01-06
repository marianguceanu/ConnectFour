from Game.game import *


class UI:

    def __init__(self) -> None:
        self.__game = Game()

    @staticmethod
    def welcome():
        print("\tHello players, and welcome to an honest game of ConnectFour!\n" +
              "\tMay the best win!\n")

    def __move__(self) -> None:
        try:
            print(self.__game.__str__())
            col = int(input("Enter place to position: "))
            self.__game.put_piece(col)
            self.__game.computer_piece()
        except BoardException as be:
            print(be)

    def play(self) -> None:
        row_win = self.__game.check_winner_row()
        col_win = self.__game.check_winner_col()
        diag_win = self.__game.check_winner_diag()
        while row_win == col_win == diag_win == "no winner":
            self.__move__()
            row_win = self.__game.check_winner_row()
            col_win = self.__game.check_winner_col()
            diag_win = self.__game.check_winner_diag()

        if row_win == "X ":
            print(self.__game.__str__())
            print("Player 1 won by connecting 4 dots on a row!")
        elif row_win == "Y ":
            print(self.__game.__str__())
            print("Player 2 won by connecting 4 dots on a row!")

        if col_win == "X ":
            print(self.__game.__str__())
            print("Player 1 won by connecting 4 dots on a column!")
        elif col_win == "Y ":
            print(self.__game.__str__())
            print("Player 2 won by connecting 4 dots on a column!")

        if diag_win == "X ":
            print(self.__game.__str__())
            print("Player 1 won by connecting 4 dots on a diagonal!")
        elif diag_win == "X ":
            print(self.__game.__str__())
            print("Player 2 won by connecting 4 dots on a diagonal!")


def main():
    ui = UI()
    ui.welcome()
    ui.play()
    check = input("Do you want to play again?(y/n) ")
    if check == 'y':
        main()
