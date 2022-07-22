from Exceptions.exceptions import BoardException

class Board:
    """
        The board for our game
    """

    def __init__(self) -> None:
        """
            Here we will initialize the board with it's necessary dimensions
        """
        self.__bd = list()
        for i in range(6):
            self.__bd.append(list())
            for _ in range(7):
                self.__bd[i].append("- ")

    def setPiece(self, position: int, player: int):
        """
            Setter, unlike other MxN boards, here we only need the column to set a piece.
        """
        for i in range(5,0, -1):
            if self.__bd[i][position-1] == "- ":
                if player == 0:
                    self.__bd[i][position-1] = "X "
                    return
                self.__bd[i][position-1] = "Y "
                return
        raise BoardException("No position available")

    def __str__(self) -> str:
        """
            Turning our board into a string
        """
        final_str = ""
        for i in range(6):
            for j in range(7):
                final_str += str(self.__bd[i][j]) + " "
            final_str += "\n"

        for i in range(7):
            final_str += str(i + 1) + "  "
        final_str += "\n"
        return final_str
