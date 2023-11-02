import pygame
from init import *
from board import *
import random

class Game:

    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minesweeper") 
        self.clock = pygame.time.Clock()


    def new(self):
        self.board_obj = Board()

        # print the minefield cell content
        self.board_obj.print_minefield()

    def run(self):
        # variable that keeps if the game runs or stops
        self.run = True

        while self.run:
            self.clock.tick(FPS)
            self.event()
            self.draw(self.window)


        else:
            self.end_screen()
            

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                r, c = pygame.mouse.get_pos()
                
                r //= SIZE
                c //= SIZE

                if r >= ROW or c >= COL:
                    continue


                # left click
                if event.button == 1:
                    if not self.board_obj.field[r][c].flagged:
                        # dig and check if exploded
                        if not self.board_obj.dig(r, c):
                            # explode
                            for r in self.board_obj.field:
                                for cell in r:
                                    if cell.flagged and cell.type != "X":
                                        cell.flagged = False
                                        cell.revealed = True
                                        cell.image = tile_not_mine
                                    elif cell.type == "X":
                                        cell.revealed = True
                            self.playing = False
                            

                # right click
                if event.button == 3:
                    
                    if not self.board_obj.field[r][c].revealed:
                        self.board_obj.field[r][c].flagged = not self.board_obj.field[r][c].flagged

                if self.win():
                    self.win = True
                    self.playing = False
                    for r in self.board_obj.field:
                        for cell in r:
                            if not cell.revealed:
                                cell.flagged = True
                    
                    


    def draw(self, window):
        self.window.fill(BG_COLOR)
        self.board_obj.draw_cell(self.window)
        pygame.display.flip()


    def win(self):
        for r in self.board_obj.field:
            for cell in r:
                if cell.type != "X" and not cell.revealed:
                    return False
                
        return True


    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return