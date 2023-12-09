from Dice import Dice
from Board import Board


def main():
    d = Dice()
    print(d.roll())

    board = Board(6, 6)
    print(board)


if __name__ == "__main__":
    main()
