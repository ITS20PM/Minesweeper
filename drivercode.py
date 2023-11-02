import pygame
from game import *
from init import *
from board import *

def main():
    game = Game()
    while True:
        # create game
        game.new()
        # run the game
        game.run()


if __name__ == "__main__":
    main()