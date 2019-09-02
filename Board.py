from FieldOption import FieldOption
from GameState import GameState
from Player import Player


class Board(object):
    def __init__(self):
        self.board = [[FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY]]

    def __str__(self):
        printedboard = [[field.name for field in row] for row in self.board]
        print(*printedboard, sep='\n')

    def checkGameState(self):
        if self.isFirstRowO() == True:
            return GameState.OVER
        if self.isFirstRowX() == True:
            return GameState.OVER
        if self.isSecondRowO() == True:
            return GameState.OVER
        if self.isSecondRowX() == True:
            return GameState.OVER
        if self.isThirdRowO() == True:
            return GameState.OVER
        if self.isThirdRowX() == True:
            return GameState.OVER
        if self.isFirstColumnO() == True:
            return GameState.OVER
        if self.isFirstColumnX() == True:
            return GameState.OVER
        if self.isSecondColumnO() == True:
            return GameState.OVER
        if self.isSecondColumnX() == True:
            return GameState.OVER
        if self.isThirdColumnO() == True:
            return GameState.OVER
        if self.isThirdColumnX() == True:
            return GameState.OVER
        if self.isForwardDiagonalO() == True:
            return GameState.OVER
        if self.isForwardDiagonalX() == True:
            return GameState.OVER
        if self.isBackwardDiagonalO() == True:
            return GameState.OVER
        if self.isBackwardDiagonalX() == True:
            return GameState.OVER
        if self.isBoardFull() == True:
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

    def printBoard(self): #tostring
        print(self)
