import json

from Dice import Dice
from Board import Board
from Player import Player

d = Dice()


def play_round(players: list[Player], board: Board, moves) -> Player:
    print('\t '.join(str(p.name) for p in players))

    # No winner yet
    while all(p.current != board.last_cell for p in players):

        for p in players:
            # Each player rolls the dice
            houses = d.roll()

            # If the number current cell is greater than the last cell, we have a winner
            if p.current + houses >= board.last_cell:
                p.current = board.last_cell
            else:
                p.current += houses

            # If there is a snake or a ladder, then the position is the destination cell
            if p.current in moves:
                p.current = moves[p.current]

            print('\t '.join(str(p.current) for p in players))
            # Winner here!
            if p.current == board.last_cell:
                print("winner is ", p.name)
                return p



def main():
    p1 = Player("Ale")
    p2 = Player("Augusto")

    players = [p1, p2]

    with open("input_dict0.json") as json_file:
        json_input = json.load(json_file)
        board = Board(json_input["width"], json_input["height"])

        # Transfer input moves to dictionary with integer keys, to get access time in O(1)
        moves = {int(k): int(v) for k, v in json_input["moves"].items()}

        # Play the game
        winner = play_round(players, board, moves)
        print(winner.name)


if __name__ == "__main__":
    main()
