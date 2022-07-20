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
            for j in range(7):
                self.__bd[i].append("- ")

    def getPiece(self, position: tuple):
        return self.__bd[position[0]][position[1]]

    def setPiece(self, position: tuple, player: int):
        if player == 0:
            self.__bd[position[0] - 1][position[1] - 1] = "A "
            return
        self.__bd[position[0] - 1][position[1] - 1] = "B "

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
