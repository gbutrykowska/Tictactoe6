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
            print("Player: " + self.activePlayer.name + ": choose coordinate row (starting from 0): ")
            chosenRow = int(input())
            print("Player: " + self.activePlayer.name + ": choose coordinate col (starting from 0): ")
            chosenCol = int(input())

            if self.board.isMoveValid(chosenRow, chosenCol) == True:
                self.board.makeMove(chosenRow, chosenCol, self.activePlayer)
                self.gameState = self.board.checkGameState()
                if self.gameState == GameState.IN_PROGRESS:
                    self.switchPlayers()
                    self.board.printBoard()
                else: self.result()
            else:
                print("Move is not valid. Try again")

    def result(self):
        if self.board.isBoardFull():
            print("Game over! It's a draw.")

        else:
            if self.activePlayer == Player.ONE:
                print("Game over! Player One wins.")
            else:
                print("Game over! Player Two wins.")


tictactoe = TicTacToe()
tictactoe.start()
