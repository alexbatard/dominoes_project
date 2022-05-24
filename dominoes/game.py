import pygame
from dominoes.board import Board
from .constants import PLAYER1, PLAYER2


class Game:
    cnt = 0

    def __init__(self, win):
        self._init()
        self.win = win  # game window

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = PLAYER1
        self.valid_moves = {}

    def reset(self):
        self._init()

    def update(self):
        # update the board
        self.board.draw(self.win, self.turn)

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.getPiece(row, col)
            if piece != 'x' and piece.player == self.turn:
                self.selected = piece
                # self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False

    def _move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 'x':
            # and (row, col) in self.valid_moves:
            self.board.fromHandToBoard(self.selected, row, col)
            Game.cnt += 1
            if Game.cnt == 1:
                global value_1
                value_1 = self.selected.value
            elif Game.cnt == 2:
                global value_2
                value_2 = self.selected.value
                Game.cnt = 0
                self.changeTurn()
        else:
            return False

        return True

    def changeTurn(self):
        if self.turn == PLAYER1:
            if (value_1, value_2) in self.board.player1_dominoes:
                self.board.player1_dominoes.remove((value_1, value_2))
            else:
                self.board.player1_dominoes.remove((value_2, value_1))
            self.turn = PLAYER2
        else:
            if (value_1, value_2) in self.board.player2_dominoes:
                self.board.player2_dominoes.remove((value_1, value_2))
            else:
                self.board.player2_dominoes.remove((value_2, value_1))
            self.turn = PLAYER1

    def winner(self):
        return self.board.winner()
