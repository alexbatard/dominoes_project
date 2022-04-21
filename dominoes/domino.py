from .constants import SQUARE_SIZE


class Domino:

    def __init__(self, row1, col1, row2, col2, value):
        self.row1 = row1
        self.col1 = col1
        self.row2 = row2
        self.col2 = col2
        self.value = value
        self.is_on_board = False
        self.is_in_stock = True
        self.orientation = 'top'  # initial domino orientation
        # if something is done by the player, self.orientation = either left,
        # right, top or bottom

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.calc_pos()

    def calc_pos(self):
        # calculate x and y position based on the current row and column
        self.x1 = SQUARE_SIZE * self.col1 + SQUARE_SIZE // 2
        self.y1 = SQUARE_SIZE * self.row1 + SQUARE_SIZE // 2
        self.x2 = SQUARE_SIZE * self.col2 + SQUARE_SIZE // 2
        self.y2 = SQUARE_SIZE * self.row2 + SQUARE_SIZE // 2

    def place_on_board(self):
        # change state of the domino
        self.is_on_board = True

    def draw_from_stock(self):
        # change state of the domino
        self.is_in_stock = False

    def change_orientation(self):
        # change state of the domino
        pass

    def draw(self, win):
        # draw domino on the window
        pass
        # format a str with self.value to select the right image
        # ex for selecting the right image:
        # f"domino_{domino.value[0]}_{domino.value[1]}.jpg"
        # rotate the image if necessary depending on self.direction

    def __str__(self):
        return str(self.value)
