# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to create the illusion of a moving 50x50 square red block

import pygame, sys, time

# set up pygame
pygame.init()

window = pygame.display.set_mode((400, 500))

# set up the colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# draw a 50x50 red square
x = 0 # x-value of top left co-ordinate
y = 0 # y-value of top left co-ordinate
pygame.draw.rect(window, RED,(x, y, 50, 50))

# update the window display
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == 12:
             pygame.quit()
             sys.exit()

    x = x + 5 # add 5 to the top position
    y = y + 5 # add 5 to the left position
    pygame.draw.rect(window, RED,(x, y, 50, 50))
 
    pygame.display.update() # show the block
    #window.fill(BLACK) # paint the entire window black
    time.sleep(0.02) # pause for 2 milliseconds
