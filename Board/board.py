from turtle import pos


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
                self.__bd[i].append("-  ")

    def getPiece(self, position: tuple):
        return self.__bd[position[0], position[1]]

    def setPiece(self, position: tuple, player: int):
        if player == 0:
            self.__bd[position[0] - 1][position[1] - 1] = "❤  "
            return
        self.__bd[position[0] - 1][position[1] - 1] = "💙  "

    def __str__(self) -> str:
        """
            Transforming the board into a str format
        Returns:
            str: String form of the board, with row and col indicators
        """
        final_string = ""
        for i in range(6):
            if i == 0:
                final_string += "   "
                for k in range(7):
                    final_string += str(k+1) + "  "
                final_string += "\n"
            final_string += str(i+1) + "  "
            for j in range(7):
                final_string += self.__bd[i][j]
            final_string += "\n"
        return final_string
