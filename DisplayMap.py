import pygame
from const import *
from enum import Enum

class Node:
    def __init__(self, x, y, l, id, nodeType) -> None:
        self.cell = pygame.Rect(x, y, l, l)
        self.nodeType = nodeType
        self.color = WHITE
        self.text_color = self.color
        if nodeType[0] == 'A':
            self.color = WHITE
            self.text_color = RED
        if nodeType[0] == '0':
            self.color = WHITE
        if nodeType == '-1':
            self.color = GREY
            self.text_color = BLACK
        if nodeType[0] == 'K':
            self.color = WHITE
            self.text_color = YELLOW
        if nodeType[0] == 'T':
            self.text_color = BLUE
        if nodeType[0] == 'D':
            self.color = GREY
            self.text_color = YELLOW
        self.id = id

    def draw_node(self, sur:pygame.Surface) -> None:
        pygame.draw.rect(sur, self.color, self.cell)
        if (self.nodeType != '0'):
            myfont = pygame.font.SysFont(None, 28)
            display_text = myfont.render(self.nodeType, True, self.text_color)
            sur.blit(display_text, self.cell)
    def update_node_type(self, nodeType, sur:pygame.Surface):
        self.nodeType = nodeType
        if nodeType[0] == 'A':
            self.color = WHITE
            self.text_color = RED
            # self.cell = pygame.Rect(self.cell.topleft[0], self.cell.topleft[1], self.cell.height, self.cell.height)
        if nodeType[0] == '0':
            self.color = WHITE
            self.text_color = self.color
            # self.cell = pygame.Rect(self.cell.topleft[0], self.cell.topleft[1], self.cell.height, self.cell.height)
        if nodeType == '-1':
            self.color = GREY
            self.text_color = BLACK
        if nodeType[0] == 'K':
            self.color = WHITE
            self.text_color = YELLOW
        if nodeType[0] == 'T':
            self.text_color = BLUE
        if nodeType[0] == 'D':
            self.color = GREY
            self.text_color = YELLOW

        self.draw_node(sur)

    # Set color of the node on Surface
    def set_live_color(self, color, sur:pygame.Surface):
        self.color = color
        self.draw_node(sur)

        pygame.time.delay(PYGAME_DELAY)
        pygame.display.update()
        
    # Set internal color of the node
    def _set_color(self, color):
        self.color = color



class DisplayMap:
    def __init__(self, floor) -> None:
        self.grid: list[Node] = []
        self.n_row = len(floor)
        self.n_col = len(floor[0])
        for y in range(self.n_row):
            for x in range(self.n_col):
                self.grid.append(Node(x*(NODE_EDGE_LEN + GAP_BETWEEN_NODES),
                                       y*(NODE_EDGE_LEN + GAP_BETWEEN_NODES), 
                                       NODE_EDGE_LEN,
                                       y*self.n_col + x,
                                       floor[y][x])) # missing is_obstacle

    def draw_map(self, sur:pygame.Surface):
        for node in self.grid:
            node.draw_node(sur)
        pygame.display.flip()
                
    