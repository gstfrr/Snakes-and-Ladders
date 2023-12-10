import json

from Dice import Dice
from Board import Board
from Player import Player

d = Dice()


def play_round(players: list[Player], board: Board, moves) -> Player:
    # While nobody reached last cell
    while all(p.current != board.last_cell for p in players):

        for p in players:

            # Each player rolls the dice
            houses = d.roll()

            # If the number current cell is greater than the last cell, we have a winner
            if p.current + houses >= board.last_cell:  # Board overflow
                p.current = board.last_cell
            else:
                p.current += houses

            # If there is a snake or a ladder, then the destination cell will be given by the moves dictionary
            if p.current in moves:
                p.current = moves[p.current]

            # Winner here!
            if p.current == board.last_cell:
                # print(p.name, " wins!")
                return p


def process_input(input_path: str) -> (dict[int, int], Board):
    with open(input_path) as json_file:
        json_input = json.load(json_file)
        board = Board(json_input["width"], json_input["height"])

        # Transfer input moves to dictionary with integer keys, to get access time in O(1)
        moves = {int(k): int(v) for k, v in json_input["moves"].items()}

        return moves, board


def main():
    p1 = Player("Ale")
    p2 = Player("Augusto")

    players = [p1, p2]

    moves, board = process_input("input0.json")

    winners = []
    for _ in range(0, 10000):
        winner = play_round(players, board, moves)
        winners.append(winner.name)
        [p.reset() for p in players]

    for p in players:
        print(p.name, winners.count(p.name) / len(winners))


if __name__ == "__main__":
    main()
