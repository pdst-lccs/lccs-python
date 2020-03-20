# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: To demonstrate the use of the pygame library

import pygame, sys

# set up pygame
pygame.init()
window = pygame.display.set_mode((400, 500)) # (width, height)

# set up the colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# draw some shapes
pygame.draw.line(window,    BLUE, (50,   50), (250, 50), 4)
pygame.draw.line(window,    GREEN,(100, 250), (250, 50), 2)
pygame.draw.rect(window,    WHITE,(100, 250,   200, 75))
pygame.draw.circle(window,  RED,  (300, 250),  30, 0)
pygame.draw.ellipse(window, RED,  (200, 400,   40, 80), 1)

# update the window display
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == 12:
            #print(event.type)
            pygame.quit()
            sys.exit()

