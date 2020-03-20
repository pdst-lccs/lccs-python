# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Further pygame activities

import pygame, sys
from pygame.locals import *

# start the pygame engine
pygame.init()

# create a 400x400 window
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Chequer Board')

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window.fill(WHITE) # paint the window white

# Draw Row 1
pygame.draw.rect(window, BLACK, (0,   0, 50, 50))
pygame.draw.rect(window, BLACK, (100, 0, 50, 50))
pygame.draw.rect(window, BLACK, (200, 0, 50, 50))
pygame.draw.rect(window, BLACK, (300, 0, 50, 50))
# Draw Row 1
pygame.draw.rect(window, BLACK, (0,   50, 50, 50))
pygame.draw.rect(window, BLACK, (150, 50, 50, 50))
pygame.draw.rect(window, BLACK, (200, 50, 50, 50))
pygame.draw.rect(window, BLACK, (350, 50, 50, 50))
# Draw Row 1
pygame.draw.rect(window, BLACK, (50,  100, 50, 50))
pygame.draw.rect(window, BLACK, (100, 100, 50, 50))
pygame.draw.rect(window, BLACK, (300, 100, 50, 50))
pygame.draw.rect(window, BLACK, (350, 100, 50, 50))

# update the window display
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
