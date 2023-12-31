import random

from Dice import Dice
from Board import Board
from Player import Player

from MoveType import MoveType

d = Dice()


def play_round(players: list[Player], board: Board, moves, consider_probability=False) -> (Player, int):
    probability = 1  # Consider probability to take ladder. It is always 1 if not specified

    number_rolls = 0
    # While nobody reached last cell
    while all(p.current != board.last_cell for p in players):
        number_rolls += 1
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
                if moves[p.current] < p.current:  # Snake
                    p.current = moves[p.current]
                else:  # Ladder
                    if consider_probability:
                        probability = random.randrange(2)
                    if bool(probability):
                        p.current = moves[p.current]

            # Winner here!
            if p.current == board.last_cell:
                # print(p.name, " wins!")
                return p, number_rolls


def play_round_immunity(players: list[Player], board: Board, moves) -> Player:
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

                if p == players[1]:  # Give immunity to Player2 first snake:
                    if moves[p.current] < p.current:  # Verify if the move is a snake
                        if p.history.count(MoveType.SNAKE) == 0:  # If there is no snake in Player 2 history
                            continue

                else:
                    p.current = moves[p.current]

            # Winner here!
            if p.current == board.last_cell:
                # print(p.name, " wins!")
                return p
