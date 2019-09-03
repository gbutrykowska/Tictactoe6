from FieldOption import FieldOption
from GameState import GameState
from Player import Player


class Board(object):
    def __init__(self):
        self.board = [[FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY]]

    def __str__(self):
        boardString = ''
        for fields in self.board:
            for field in fields:
                if field == FieldOption.EMPTY:
                    boardString += '? '
                else:
                    boardString += field.name + ' '
            boardString += '\n'

        return boardString

    def checkGameState(self):
        if self.isFirstRowO():
            return GameState.OVER
        if self.isFirstRowX():
            return GameState.OVER
        if self.isSecondRowO():
            return GameState.OVER
        if self.isSecondRowX():
            return GameState.OVER
        if self.isThirdRowO():
            return GameState.OVER
        if self.isThirdRowX():
            return GameState.OVER
        if self.isFirstColumnO():
            return GameState.OVER
        if self.isFirstColumnX():
            return GameState.OVER
        if self.isSecondColumnO():
            return GameState.OVER
        if self.isSecondColumnX():
            return GameState.OVER
        if self.isThirdColumnO():
            return GameState.OVER
        if self.isThirdColumnX():
            return GameState.OVER
        if self.isForwardDiagonalO():
            return GameState.OVER
        if self.isForwardDiagonalX():
            return GameState.OVER
        if self.isBackwardDiagonalO():
            return GameState.OVER
        if self.isBackwardDiagonalX():
            return GameState.OVER
        if self.isBoardFull():
            return GameState.OVER
        else:
            return GameState.IN_PROGRESS

    def isFirstRowO(self):
        if all(field == FieldOption.O for field in self.board[0]):
            return True

    def isFirstRowX(self):
        if all(field == FieldOption.X for field in self.board[0]):
            return True

    def isSecondRowO(self):
        if all(field == FieldOption.O for field in self.board[1]):
            return True

    def isSecondRowX(self):
        if all(field == FieldOption.X for field in self.board[1]):
            return True

    def isThirdRowO(self):
        if all(field == FieldOption.O for field in self.board[2]):
            return True

    def isThirdRowX(self):
        if all(field == FieldOption.X for field in self.board[2]):
            return True

    def isFirstColumnO(self):
        if self.board[0][0] == FieldOption.O and self.board[1][0] == FieldOption.O and self.board[2][0] == FieldOption.O:
            return True

    def isFirstColumnX(self):
        if self.board[0][0] == FieldOption.X and self.board[1][0] == FieldOption.X and self.board[2][0] == FieldOption.X:
            return True

    def isSecondColumnO(self):
        if self.board[0][1] == FieldOption.O and self.board[1][1] == FieldOption.O and self.board[2][1] == FieldOption.O:
            return True

    def isSecondColumnX(self):
        if self.board[0][1] == FieldOption.X and self.board[1][1] == FieldOption.X and self.board[2][1] == FieldOption.X:
            return True

    def isThirdColumnO(self):
        if self.board[0][2] == FieldOption.O and self.board[1][2] == FieldOption.O and self.board[2][2] == FieldOption.O:
            return True

    def isThirdColumnX(self):
        if self.board[0][2] == FieldOption.X and self.board[1][2] == FieldOption.X and self.board[2][2] == FieldOption.X:
            return True

    def isForwardDiagonalO(self):
        if self.board[2][0] == FieldOption.O and self.board[1][1] == FieldOption.O and self.board[0][2] == FieldOption.O:
            return True

    def isForwardDiagonalX(self):
        if self.board[2][0] == FieldOption.X and self.board[1][1] == FieldOption.X and self.board[0][2] == FieldOption.X:
            return True

    def isBackwardDiagonalO(self):
        if self.board[0][0] == FieldOption.O and self.board[1][1] == FieldOption.O and self.board[2][2] == FieldOption.O:
            return True

    def isBackwardDiagonalX(self):
        if self.board[0][0] == FieldOption.X and self.board[1][1] == FieldOption.X and self.board[2][2] == FieldOption.X:
            return True

    def isBoardFull(self):
        row1 = self.board[0]
        row2 = self.board[1]
        row3 = self.board[2]
        if row1.count(FieldOption.EMPTY) == 0 and row2.count(FieldOption.EMPTY) == 0 and row3.count(FieldOption.EMPTY) == 0:
            return True

    def isMoveValid(self, row, col):
        return self.board[row][col] == FieldOption.EMPTY

    def makeMove(self, row, col, activePlayer):
        if (activePlayer == Player.ONE):
            self.board[row][col] = FieldOption.O
        else:
            self.board[row][col] = FieldOption.X
