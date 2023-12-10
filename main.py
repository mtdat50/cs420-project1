import pygame
from function import *
from time import sleep
from DisplayMap import DisplayMap, Node
from const import *
from Menu import Menu
from Button import Button
from Camera import CameraGroup
import copy
import sys


def play_path(map, path, displayMaps, agentCoord, cur_step_idx):
    agent1Coord = [agentCoord[0][1], agentCoord[0][2] , agentCoord[0][3]]
    step = path[cur_step_idx]

    cur_floor = agent1Coord[0]
    cur_floor_n_rows = displayMaps[cur_floor].n_row
    cur_floor_n_cols = displayMaps[cur_floor].n_col
    
    cur_row = agent1Coord[1]
    cur_col = agent1Coord[2]
    cur_cell_id = cur_row*cur_floor_n_cols + cur_col

    displayMaps[cur_floor].grid[Node.get_node_id(cur_col, cur_row, cur_floor_n_cols)].update_node_type('0')

    agent1Coord[1] += step[0]
    agent1Coord[2] += step[1]

    if map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] == 'UP':
        agent1Coord[0] += 1
    elif map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] == 'DO':
        agent1Coord[0] -= 1

    cur_row = agent1Coord[1]
    cur_col = agent1Coord[2]
    cur_cell_id = cur_row*cur_floor_n_cols + cur_col
    displayMaps[cur_floor].grid[Node.get_node_id(cur_col, cur_row, cur_floor_n_cols)].update_node_type('A1')
    
    # print(step, agent1Coord)
    # if map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] != '0':
    #     print(map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]])
    
    agentCoord[0] = (agentCoord[0][0], agent1Coord[0], agent1Coord[1], agent1Coord[2])
    # sleep(0.25)
    

def main():

    # MAP SETUPS
    # map, agentCoord = input('maxsize_map.txt')
    map, agentCoord = input('input.txt')
    f = len(map)
    m = len(map[0])
    n = len(map[0][0])

    g, vertexType= convert2Graph(map, agentCoord = agentCoord)
    # for vertex, edgeList in enumerate(g):
    #     print('=================', vertex, vertexType[vertex])
    #     for edge in g[vertex]:
    #         print(edge[0], vertexType[edge[0]])
    #         print(edge[1])
    # print(vertexType)

    # PYGAME SETUPS
    pygame.init()
    pygame.display.set_caption("Group Project 1: Search")
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(RESOLUTION)
    screen.fill(BLACK)
    map_surface = screen.subsurface(0, 0, MAP_RES[0], RESOLUTION[1])
    map_surface.fill(GREY)

    menu = Menu()
    play_button = Button(menu.rect.left+50, menu.rect.top+50, "Play", menu, 'Assets/orange_button.png', is_text_button=True)
    pause_button = Button(menu.rect.left+50, menu.rect.top+130, "Pause", menu, 'Assets/orange_button.png', is_text_button=True)
    reset_button = Button(menu.rect.left+50, menu.rect.top+210, "Reset", menu, 'Assets/orange_button.png', is_text_button=True)


    camera_group = CameraGroup(map_surface)
    # camera_group = pygame.sprite.Group()

    # Map setups
    displayMaps: list[DisplayMap] = []
    for i in range(f):
        displayMaps.append(DisplayMap(map[i], camera_group))


    path, nodes = findPath(g, vertexType, agent_index = 1)

    # Backups
    agentCoordBU = copy.deepcopy(agentCoord)

    # Flags
    is_playing: bool = False
    cur_step_idx = 0
    n_steps = len(path)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEWHEEL:
                camera_group.zoom_scale += event.y * 0.06
                if event.y < 0 and camera_group.zoom_scale < 0.3:
                    camera_group.zoom_scale = 0.3
                if event.y > 0 and camera_group.zoom_scale > 1.3:
                    camera_group.zoom_scale = 1.3
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1):
                    if play_button.checkForInput(pygame.mouse.get_pos()):
                        is_playing = True
                    if pause_button.checkForInput(pygame.mouse.get_pos()):
                        is_playing = False
                    if reset_button.checkForInput(pygame.mouse.get_pos()):
                        is_playing = False
                        cur_step_idx = 0
                        agentCoord = copy.deepcopy(agentCoordBU)

                        camera_group.empty()
                        displayMaps: list[DisplayMap] = []
                        for i in range(f):
                            displayMaps.append(DisplayMap(map[i], camera_group))
        


        if is_playing and cur_step_idx < n_steps:
            play_path(map, path, displayMaps, agentCoord, cur_step_idx)
            cur_step_idx += 1
            camera_group.update()

        # camera_group.update()
        camera_group.custom_draw(map_surface)
        # camera_group.draw(map_surface)

        menu.update(pygame.mouse.get_pos())
        menu.draw_menu(screen)
        
        pygame.display.flip()
        
main()