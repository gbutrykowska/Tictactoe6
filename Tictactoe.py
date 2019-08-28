# Napisz kolko i krzyzyk.
from Board import Board
from GameState import GameState
from Player import Player


class TicTacToe(object):
    def __init__(self):
        self.gameState = GameState.IN_PROGRESS
        self.activePlayer = Player.ONE
        self.board = Board()

    def switchPlayers(self):
        if (self.activePlayer == Player.ONE):
            self.activePlayer = Player.TWO
        else:
            self.activePlayer = Player.ONE

    def start(self):  # tylko tu print i input

        while self.gameState == GameState.IN_PROGRESS:
            print("Player: " + self.activePlayer.name + ": choose coordinate row: ")
            chosenRow = int(input())
            print("Player: " + self.activePlayer.name + ": choose coordinate col: ")
            chosenCol = int(input())

            if self.board.isMoveValid(chosenRow, chosenCol) == True:
                self.board.makeMove(chosenRow, chosenCol, self.activePlayer)
                self.gameState = self.board.checkGameState()
                self.switchPlayers()
            else:
                print("Move is not valid. Try again")

        else:
            self.result()

    def result(self):
        if Board.isBoardFull == True:
            print("Game over! It's a draw.")

        elif self.activePlayer == Player.ONE:
            print("Game over! Player One wins.")
        else:
            print("Game over! Player Two wins.")


tictactoe = TicTacToe()
tictactoe.start()
