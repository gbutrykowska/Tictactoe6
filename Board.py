from FieldOption import FieldOption
from GameState import GameState
from Player import Player


class Board(object):
    def __init__(self):
        self.board = [[FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY]]

    def checkGameState(self):
        if all(field == self.board[0][0] for field in self.board[0]):
            return GameState.OVER
        elif all(field == self.board[1][0] for field in self.board[1]):
            return GameState.OVER
        elif all(field == self.board[2][0] for field in self.board[2]):
            return GameState.OVER
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return GameState.OVER
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return GameState.OVER
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return GameState.OVER
        elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return GameState.OVER
        elif self.isBoardFull() == True:
            return GameState.OVER
        else:
            return GameState.IN_PROGRESS

    def isBoardFull(self):
        return self.board.count(FieldOption.EMPTY) == 0

    def isMoveValid(self, row, col):
        return self.board[row][col] == FieldOption.EMPTY

    def makeMove(self, row, col, activePlayer):
        if (activePlayer == Player.ONE):
            self.board[row][col] = FieldOption.O
        else:
            self.board[row][col] = FieldOption.X
