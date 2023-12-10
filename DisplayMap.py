import pygame
from const import *
from enum import Enum

class Node(pygame.sprite.Sprite):
    def __init__(self, pos, nodeType, group):
        super().__init__(group)
        self.nodeType = nodeType
        self.text_color = WHITE
        if nodeType[0] == 'A':
            self.image = pygame.image.load('Assets/empty_cell.png').convert_alpha()
            self.text_color = WHITE
            self.bg_color = RED
        if nodeType[0] == '0':
            self.image = pygame.image.load('Assets/empty_cell.png').convert_alpha()
            self.bg_color = WHITE
        if nodeType == '-1':
            self.image = pygame.image.load('Assets/empty_cell.png').convert_alpha()
            self.text_color = GREY
            self.bg_color = BLACK
        if nodeType[0] == 'K':
            self.image = pygame.image.load('Assets/empty_cell.png').convert_alpha()
            self.text_color = YELLOW
            self.bg_color = WHITE
        if nodeType[0] == 'T':
            self.image = pygame.image.load('Assets/empty_cell.png').convert_alpha()
            self.text_color = RED
            self.bg_color = WHITE
        if nodeType[0] == 'D':
            self.image = pygame.image.load('Assets/empty_cell.png').convert_alpha()
            self.text_color = YELLOW
            self.bg_color = BLACK

        self.rect = self.image.get_rect(topleft = pos)
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(self.bg_color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

        # Text
        self.font = pygame.font.SysFont(GAME_FONT, 28)
        self.textSurf = self.font.render(nodeType, 1, self.text_color)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.rect.width/2 - W/2, self.rect.height/2 - H/2])

        self.id = id

    def __deepcopy__(self, memo):
        # just create a new instance 
            return Node(self.rect.topleft, self.nodeType, self.groups()[0])

    def update_node_type(self, nodeType):
        self.nodeType = nodeType
        self.text_color = WHITE
        if nodeType[0] == 'A':
            self.text_color = WHITE
            self.bg_color = RED
        if nodeType[0] == '0':
            self.bg_color = WHITE
        if nodeType == '-1':
            self.text_color = GREY
            self.bg_color = BLACK
        if nodeType[0] == 'K':
            self.text_color = YELLOW
            self.bg_color = WHITE
        if nodeType[0] == 'T':
            self.text_color = RED
            self.bg_color = WHITE
        if nodeType[0] == 'D':
            self.text_color = YELLOW
            self.bg_color = BLACK

        self.image = pygame.image.load('Assets/empty_cell.png').convert_alpha()
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(self.bg_color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

        # Text
        self.font = pygame.font.SysFont(GAME_FONT, 28)
        self.textSurf = self.font.render(nodeType, 1, self.text_color)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.rect.width/2 - W/2, self.rect.height/2 - H/2])
        



    # def update(self):
        # self.image = self.image.copy()
        # colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        # colorImage.fill(self.bg_color)
        # self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

        # # Text
        # self.font = pygame.font.SysFont(GAME_FONT, 28)
        # self.textSurf = self.font.render(self.nodeType, 1, self.text_color)
        # W = self.textSurf.get_width()
        # H = self.textSurf.get_height()
        # self.image.blit(self.textSurf, [self.rect.width/2 - W/2, self.rect.height/2 - H/2])

        # print("node.update")
    
    def get_node_id(x: int, y: int, ncols: int):
        return y*ncols + x



class DisplayMap:
    def __init__(self, floor, group) -> None:
        self.grid: list[Node] = []
        self.n_row = len(floor)
        self.n_col = len(floor[0])

        for y in range(self.n_row):
            for x in range(self.n_col):
                self.grid.append(Node((x*(NODE_EDGE_LEN), y*(NODE_EDGE_LEN)), 
                                    floor[y][x],
                                    group))