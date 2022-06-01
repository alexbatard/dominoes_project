import pygame
from .constants import SQUARE_SIZE, DOMINO_BACK


class HalfDomino:

    def __init__(self, row, col, value, player):
        self.row = row
        self.col = col
        self.value = value
        self.player = player
        self.is_on_board = False
        self.neighbors = {}
        self.x = 0
        self.y = 0
        self.calcPos()

    def calcPos(self):
        # give x and y position based on the current row and column
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def placeOnBoard(self):
        # change state of the half domino
        self.is_on_board = True

    def draw(self, win):
        DOMINO_IMAGE = pygame.transform.scale(
            pygame.image.load(f"assets/dom_{self.value}.png"), (40, 40))
        DOMINO_IMAGE_RECT = DOMINO_IMAGE.get_rect(center=(self.x, self.y))
        win.blit(DOMINO_IMAGE, DOMINO_IMAGE_RECT)

    def drawHidden(self, win):
        DOMINO_BACK_RECT = DOMINO_BACK.get_rect(center=(self.x, self.y))
        win.blit(DOMINO_BACK, DOMINO_BACK_RECT)

    def fromHandToBoard(self, row, col):
        self.row = row
        self.col = col
        self.calcPos()
        self.placeOnBoard()

    def getNeighborNumber(self):
        return sum(self.neighbors.values())

    def __repr__(self):
        return str(self.value)
