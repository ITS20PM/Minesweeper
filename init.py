import pygame
import os

# size of the window
SIZE = 32
ROW, COL = 15, 15
WIDTH, HEIGHT = COL*SIZE, ROW*SIZE

# number of mines
MINES = 30

FPS = 50

NUM_COLOR = {1: "blue", 2: "green", 3: "red", 4: "blue4", 
            5: "brown", 6: "aqua", 7: "black", 8: "gray"}
BG_COLOR = "white"
RECT_COLOR = "gainsboro"
CLICKED_RECT_COLOR = (248,248,255)
FLAG_COLOR = "red"
BOMB_COLOR = "black"

tile_numbers = []
for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("images", f"Tile{i}.png")), (SIZE, SIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileEmpty.png")), (SIZE, SIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileExploded.png")), (SIZE, SIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileFlag.png")), (SIZE, SIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileMine.png")), (SIZE, SIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileUnknown.png")), (SIZE, SIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("images", "TileNotMine.png")), (SIZE, SIZE))
