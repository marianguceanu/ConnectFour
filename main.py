from Board.board import Board


def main():
    b = Board()
    b.setPiece(1, 0)
    b.setPiece(2, 1)
    print(str(b))


if __name__ == "__main__":
    main()
