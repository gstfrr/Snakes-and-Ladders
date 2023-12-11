import json
import pandas as pd

from MoveType import MoveType
from Board import Board
from Player import Player

from Game import play_round
from Game import play_round_immunity

runs = 10000


def process_input(input_path: str) -> (dict[int, int], Board):
    with open(input_path) as json_file:
        json_input = json.load(json_file)
        board = Board(json_input["width"], json_input["height"])

        # Transfer input moves to dictionary with integer keys, to get access time in O(1)
        moves = {int(k): int(v) for k, v in json_input["moves"].items()}

        return moves, board


def question_1(players: list[Player], board: Board, moves) -> None:
    winners = []
    for _ in range(0, runs):
        winner = play_round(players, board, moves)

        # Save the winner's name
        winners.append(winner.name)

        # Don't forget to reset the player current cell before playing again
        [p.reset() for p in players]

    for p in players:
        print(p.name, winners.count(p.name) / len(winners))


def question_2(players: list[Player], board: Board, moves) -> None:
    average_sakes = 0
    for _ in range(0, runs):
        play_round(players, board, moves)

        # Save all the cell lands
        lands = []
        for player in players:
            for move in player.history:
                lands.append(move)

        average_sakes += lands.count(MoveType.SNAKE)

        # Don't forget to reset the player current cell before playing again
        [p.reset() for p in players]

    print("Average snakes: ", float(average_sakes / runs))


def question_4(players: list[Player], board: Board, moves) -> None:
    p1, p2 = (players[0], players[1])

    results = {
        "Square": [],
        "Player1": [],
        "Player2": [],
    }

    for initial_square in range(1, board.last_cell):
        results["Square"].append(initial_square)
        winners = []
        for _ in range(0, runs):
            # Start p2 at the i_th square
            p2.current = initial_square

            winner = play_round(players, board, moves)

            # Save the winner's name
            winners.append(winner.name)

            # Don't forget to reset the player current cell before playing again
            [p.reset() for p in players]

        results["Player1"].append(winners.count(p1.name) / len(winners))
        results["Player2"].append(winners.count(p2.name) / len(winners))

    df = pd.DataFrame(results)
    print(df)  # Question 4


def question_5(players: list[Player], board: Board, moves) -> None:
    winners = []
    for _ in range(0, runs):
        winner = play_round_immunity(players, board, moves)

        # Save the winner's name
        winners.append(winner.name)

        # Don't forget to reset the player current cell before playing again
        [p.reset() for p in players]

    for p in players:
        print(p.name, winners.count(p.name) / len(winners))


def main():
    p1 = Player("Ale")
    p2 = Player("Augusto")

    players = [p1, p2]

    moves, board = process_input("input0.json")

    question_1(players, board, moves)
    question_2(players, board, moves)
    question_4(players, board, moves)
    question_5(players, board, moves)


if __name__ == "__main__":
    main()
