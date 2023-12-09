import numpy as np


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = None

        self.init_board()

    def init_board(self):
        array = np.array(range(1, self.width * self.height + 1))
        matrix = array.reshape((self.height, self.width))

        matrix[1::2] = matrix[1::2, ::-1]
        matrix = matrix[::-1]

        self.board = matrix

    def __repr__(self):
        return str(self.board)
