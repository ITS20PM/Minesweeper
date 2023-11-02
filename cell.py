from init import *


class Cell:

    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x*SIZE, y*SIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged


    def draw(self, board):
        if not self.flagged and self.revealed:
            board.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            board.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            board.blit(tile_unknown, (self.x, self.y))


    def __repr__(self):
        return self.type
