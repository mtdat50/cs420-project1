import pygame
from map import Map
from const import *

pygame.init()
surface = pygame.display.set_mode(RESOLUTION)

world = Map(10, 10)
world.draw_map(surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()