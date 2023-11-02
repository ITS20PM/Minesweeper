import random
from init import *
from cell import *

class Board:

    def __init__(self):
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.field = [[Cell(col, row, tile_empty, ".") for row in range(ROW)] for col in range(COL)]
        self.add_mine()
        self.place_number()
        self.dug = []


    def add_mine(self):
        i = 0
        # generate mines in the grid
        while i < MINES:
            r = random.randrange(0, ROW)
            c = random.randrange(0, COL)

            if self.field[r][c].type == ".":
                self.field[r][c].image = tile_mine
                # add mine
                self.field[r][c].type = "X"
                i += 1
                


    def place_number(self):
        for i in range(ROW):
            for j in range(COL):
                # check if it is not mine
                if self.field[i][j].type != "X":
                    adjacent_mines = self.get_neighbours(i, j)
        
                    if adjacent_mines > 0:
                        self.field[i][j].image = tile_numbers[adjacent_mines-1]
                        self.field[i][j].type = "C"
            
    @staticmethod
    def is_inside(x, y):
        return 0 <= x < ROW and 0 <= y < COL


    def get_neighbours(self, r, c):
        res = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                adjacent_x = r + x
                adjacent_y = c + y
                
                if self.is_inside(adjacent_x, adjacent_y) and self.field[adjacent_x][adjacent_y].type == "X":
                    res += 1

        return res
           

    def draw_cell(self, window):
        for r in self.field:
            for cell in r:
                cell.draw(self.board_surface)
        window.blit(self.board_surface, (0, 0))

    
    def dig(self, x, y):
        self.dug.append((x, y))
        # if we click the mine
        if self.field[x][y].type == "X":
            self.field[x][y].revealed = True
            self.field[x][y].image = tile_exploded
            return False
        # if we click the number
        elif self.field[x][y].type == "C":
            self.field[x][y].revealed = True
            return True

        self.field[x][y].revealed = True

        for r in range(max(0, x-1), min(ROW-1, x+1) + 1):
            for c in range(max(0, y-1), min(COL-1, y+1) + 1):
                if (r, c) not in self.dug:
                    self.dig(r, c)
        return True


    def print_minefield(self):
        for line in self.field:
            print(line)

