# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Chequer Board v1
# Purpose: A program to display the first 3 rows of a chequer board
# Task: Modify the program to a) display all 8 rows and b) use loops

import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Chequer Board')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window.fill(WHITE)

# Row 1
pygame.draw.rect(window, BLACK, (0,   0, 50, 50))
pygame.draw.rect(window, BLACK, (100, 0, 50, 50))
pygame.draw.rect(window, BLACK, (200, 0, 50, 50))
pygame.draw.rect(window, BLACK, (300, 0, 50, 50))
# Row 2
pygame.draw.rect(window, BLACK, (50,  50, 50, 50))
pygame.draw.rect(window, BLACK, (150, 50, 50, 50))
pygame.draw.rect(window, BLACK, (250, 50, 50, 50))
pygame.draw.rect(window, BLACK, (350, 50, 50, 50))
# Row 3
pygame.draw.rect(window, BLACK, (0,   100, 50, 50))
pygame.draw.rect(window, BLACK, (100, 100, 50, 50))
pygame.draw.rect(window, BLACK, (200, 100, 50, 50))
pygame.draw.rect(window, BLACK, (300, 100, 50, 50))

# render the window object
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
