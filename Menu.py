import pygame
import sys
from Button import Button
from const import *

MENU_WIDTH = RESOLUTION[0] - MAP_RES[0]
MENU_HEIGHT = RESOLUTION[1]
MENU_X_POS = RESOLUTION[0] - MENU_WIDTH
MENU_Y_POS = 0
MENU_BACKGROUND_COLOR = WHITE

class Menu(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.x_pos = MENU_X_POS
        self.y_pos = MENU_Y_POS
        self.width = MENU_WIDTH
        self.height = MENU_HEIGHT
        self.background_color = MENU_BACKGROUND_COLOR
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def draw_menu(self, sur: pygame.Surface):
        pygame.draw.rect(sur, self.background_color, self.rect)
        for sprite in self.sprites():
            sur.blit(sprite.image, [sprite.x_pos, sprite.y_pos])