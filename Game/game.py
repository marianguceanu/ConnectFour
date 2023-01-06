from Board.board import Board
from Exceptions.exceptions import BoardException
from random import randrange


class Game:

    """
        The game class, here we will see if the pieces are put correctly and check for winners.
    """

    def __init__(self) -> None:
        """
            Class variables, one of them will be the Board, other the player marker.
        """
        self.__bd = Board()
        self.__player_last_move = 0

    def computer_piece(self) -> int:
        if self.__player_last_move == 1:
            for i in range(6):
                p1 = self.__bd.get_piece((i+1, 0))
                p2 = self.__bd.get_piece((i, 0))
                if p1 == "- ":
                    self.__bd.set_piece(i+1, 1)
                    return
                if p2 == "- ":
                    self.__bd.set_piece(i, 1)
                    return
        if self.__player_last_move == 7:
            for i in range(6):
                p1 = self.__bd.get_piece((i-1, 6))
                p2 = self.__bd.get_piece((i, 6))
                if p1 == "- ":
                    self.__bd.set_piece(i-1, 1)
                    return
                if p2 == "- ":
                    self.__bd.set_piece(i, 1)
                    return
        while True:
            i = randrange(0, 5)
            j = randrange(1, 5)
            if self.__bd.get_piece((i, j)) == "- ":
                self.__bd.set_piece(j, 1)
                return

    def put_piece(self, col: int):
        """
            A function that sets the piece properly and raises errors when it must.
        Args:
            col (int): The column chosen by the user.

        Raises:
            BoardException: Custom exception made for the game
        """
        if col not in range(7):
            raise BoardException("Invalid value!")
        marker = self.__bd.set_piece(col, 0)
        if marker == 1:
            raise BoardException("No more space on this column!")
        self.__player_last_move = col

    def check_winner_row(self) -> str:
        """
            Checks if there's a winner.
        Returns:
            str: A string that represents the piece of a player or 'no winner'
        """
        for i in range(6):
            for j in range(4):
                piece = self.__bd.get_piece((i, j))
                if piece != "- ":
                    winner = piece
                    for k in range(4):
                        if piece != self.__bd.get_piece((i, j+k)):
                            winner = None
                    if winner is not None:
                        return winner

        return "no winner"

    def check_winner_col(self) -> str:
        """
            Checks if there is winner that connected pieces on the column.
        Returns:
            str: Winner's piece or 'no winner'
        """
        for j in range(7):
            for i in range(3):
                piece = self.__bd.get_piece((i, j))
                if piece != "- ":
                    winner = piece
                    for k in range(4):
                        if piece != self.__bd.get_piece((i+k, j)):
                            winner = None
                    if winner is not None:
                        return winner
        return "no winner"

    def check_winner_diag(self) -> str:
        """
            Checks the cases that are parallel to the 'main' and 'secondary' diagonals of the 6x7 board.
        Returns:
            str: Winner's piece or 'no winner'.
        """
        for i in range(3):
            for j in range(4):
                piece = self.__bd.get_piece((i, j))
                if piece != "- ":
                    winner = piece
                    for k in range(4):
                        if piece != self.__bd.get_piece((i+k, j+k)):
                            winner = None
                    if winner is not None:
                        return winner

                piece = self.__bd.get_piece((5-i, j))
                if piece != "- ":
                    winner = piece
                    for k in range(4):
                        if piece != self.__bd.get_piece((5-i-k, j+k)):
                            winner = None
                    if winner is not None:
                        return winner
        return "no winner"

    def __str__(self) -> str:
        return self.__bd.__str__()
