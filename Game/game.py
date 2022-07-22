from Board.board import Board
from Exceptions.exceptions import BoardException


class Game:

    """
        The game class, here we will see if the pieces are put correctly and check for winners.
    """

    def __init__(self) -> None:
        """
            Clas variables, one of them will be the Board, other the player marker.
        """
        self.__bd = Board()
        self.__player = 0

    def put_piece(self, col: int):
        """
            A function that sets the piece properly and raises errors when it must.
        Args:
            col (int): The column chosen by the user.

        Raises:
            BoardException: Custom exception made for the game
        """
        marker = self.__bd.setPiece(col, self.__player)
        if marker == 1:
            raise BoardException("No more space here!")
        if self.__player == 0:
            self.__player = 1
            return
        self.__player = 0

    def check_winner(self) -> int:
        pass
