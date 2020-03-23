# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Chequer Board v1
# Purpose: A program to display the first 4 rows of a chequer board using loops
# Task: Complete the program so that all 8 rows are displayed

import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Chequer Board')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

windowSurface.fill(WHITE)

# Row 1
x = 0
y = 0
for column in range(1,5):
    pygame.draw.rect(windowSurface, BLACK, (x, y, 50, 50))
    x = x+100

# Row 2
x = 50
y = y+50
for column in range(1,5):
    pygame.draw.rect(windowSurface, BLACK, (x, y, 50, 50))
    x = x+100

# Row 3
x = 0
y = y+50
for column in range(1,5):
    pygame.draw.rect(windowSurface, BLACK, (x, y, 50, 50))
    x = x+100

# Row 4
x = 50
y = y+50
for column in range(1,5):
    pygame.draw.rect(windowSurface, BLACK, (x, y, 50, 50))
    x = x+100

# render the windowSurface object
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

