from MoveType import MoveType


class Player(object):
    def __init__(self, name):
        self.name = name
        self._current = 0
        self._history = []

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        if self.current == value:
            self._history.append(MoveType.NULL)
        elif self.current > value:
            self._history.append(MoveType.SNAKE)
        else:
            self._history.append(MoveType.LADDER)
        self._current = value
        # self._history.append(value)

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value
