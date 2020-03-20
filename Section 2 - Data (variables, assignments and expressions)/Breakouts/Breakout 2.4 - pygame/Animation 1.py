# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to display a 50x50 square red block
# in the top left hand corner of a pygame window

import pygame, sys

# set up pygame
pygame.init()

window = pygame.display.set_mode((400, 500))

# set up the colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# draw a 50x50 square at (0,0)
pygame.draw.rect(window, RED,(0, 0, 50, 50))

# update the window display
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == 12:
            pygame.quit()
            sys.exit()
