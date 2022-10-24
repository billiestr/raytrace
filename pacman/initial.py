import pygame, sys
from pygame.locals import QUIT

pygame.init()
SIZE=(1200, 400)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('raycast - bump into something to change house colour!')