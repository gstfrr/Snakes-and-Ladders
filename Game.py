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
                p.current = moves[p.current]

            # Winner here!
            if p.current == board.last_cell:
                # print(p.name, " wins!")
                return p
