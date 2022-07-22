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

    def getPiece(self, position: tuple):
        """
            Simple getter
        Args:
            position (tuple): x and y coordinates of the piece

        Returns:
            str: the piece itself
        """
        return self.__bd[position[0]][position[1]]

    def setPiece(self, position: int, player: int) -> int:
        """
            Simple setter
        Args:
            position (int): The column in which the players will add their piece
            player (int): The player's marker ( 1 or 0 )

        Returns:
            int: A convenient integer to know if there is a success or not ( 1 for success, 0 for failure )
        """
        for i in range(5, 0, -1):
            if self.__bd[i][position-1] == "- ":
                if player == 0:
                    self.__bd[i][position-1] = "X "
                    return 0
                self.__bd[i][position-1] = "Y "
                return 0
        return 1

    def __str__(self) -> str:
        """
            Turning the board into a string.
        Returns:
            str: The string form
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
