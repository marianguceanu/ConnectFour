from Board.board import Board
from Exceptions.exceptions import BoardException


class Game:

    """
        The game class, here we will see if the pieces are put correctly and check for winners.
    """

    def __init__(self) -> None:
        """
            Class variables, one of them will be the Board, other the player marker.
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

    def check_winner_row(self) -> int:
        """
            Checks if there's a winner by connecting 4 dots on a row
        Returns:
            int: 0 in case that the first player wins or 1 for the second, -1 for none.
        """
        for i in range(6):
            winner = "p"

            # The middle piece from each line
            piece = self.__bd.getPiece((i, 3))

            # First part, or all the pieces from the beginning of the line to the middle
            for j in range(3):
                if self.__bd.getPiece((i, j)) != piece:
                    winner = None
            if winner is not None:
                if piece == "X ":
                    return 0
                return 1

            winner = "p"

            # Second part, or all the pieces from the middle to the end of the line
            for j in range(3):
                if self.__bd.getPiece((i, j+3)) != piece:
                    winner = None
            if winner is not None:
                if piece == "X ":
                    return 0
                return 1

        return -1

    def check_winner_col(self) -> int:
        """
            Checks if there is winner that connected pieces on the column.
        Returns:
            int: 0 in case that the first player wins or 1 for the second, -1 for none.
        """
        for j in range(7):
            winner = "p"

            # Choosing a piece that is going to be in all the combinations
            piece = self.__bd.getPiece((2, j))

            # First 4 pieces on a col
            for i in range(4):
                if self.__bd.getPiece((i, j)) != piece:
                    winner = None
            if winner is not None:
                if piece == "X ":
                    return 0
                return 1

            winner = "p"

            # Next 4 pieces
            for i in range(4):
                if self.__bd.getPiece((i+1, j)) != piece:
                    winner = None
            if winner is not None:
                if piece == "X ":
                    return 0
                return 1

            winner = "p"

            # Last 4 pieces
            for i in range(4):
                if self.__bd.getPiece((i+2, j)) != piece:
                    winner = None
            if winner is not None:
                if piece == "X ":
                    return 0
                return 1
        return -1
