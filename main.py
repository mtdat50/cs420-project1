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
import tkinter
import tkinter.filedialog

def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name


def play_path(map, path, displayMaps, agentCoord, agent_idx, cur_step_idx):
    cur_agentCoord = [agentCoord[agent_idx][1], agentCoord[agent_idx][2] , agentCoord[agent_idx][3]]
    step = path[cur_step_idx]

    cur_floor = cur_agentCoord[0]
    cur_floor_n_rows = displayMaps[cur_floor].n_row
    cur_floor_n_cols = displayMaps[cur_floor].n_col
    
    cur_row = cur_agentCoord[1]
    cur_col = cur_agentCoord[2]

    cur_agentCoord[1] += step[0]
    cur_agentCoord[2] += step[1]
    
    # Collision resolve
    # if displayMaps[cur_floor].grid[Node.get_node_id(cur_agentCoord[2], cur_agentCoord[1], cur_floor_n_cols)].nodeType[0] == 'A':
    #     print("Collision!")
    #     return False

    displayMaps[cur_floor].grid[Node.get_node_id(cur_col, cur_row, cur_floor_n_cols)].update_node_type('0')

    if map[cur_agentCoord[0]][cur_agentCoord[1]][cur_agentCoord[2]] == 'UP':
        cur_agentCoord[0] += 1
    elif map[cur_agentCoord[0]][cur_agentCoord[1]][cur_agentCoord[2]] == 'DO':
        cur_agentCoord[0] -= 1

    cur_row = cur_agentCoord[1]
    cur_col = cur_agentCoord[2]
    cur_cell_id = cur_row*cur_floor_n_cols + cur_col
    displayMaps[cur_floor].grid[Node.get_node_id(cur_col, cur_row, cur_floor_n_cols)].update_node_type('A' + str(agent_idx+1))
    
    agentCoord[agent_idx] = (agentCoord[agent_idx][0], cur_agentCoord[0], cur_agentCoord[1], cur_agentCoord[2])
    return True
    

def main(map_file_path):

    # MAP SETUPS
    # map, agentCoord = input('maxsize_map.txt')
    # map, agentCoord = input('input.txt')
    map, agentCoord = input(map_file_path)
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
    screen.fill(CYAN)
    map_surface = screen.subsurface(0, 0, MAP_RES[0], RESOLUTION[1])
    map_surface.fill(GREY)

    menu = Menu()
    cur_floor_statboard = Button(menu.rect.left+50, menu.rect.top+200, "A1's current Floor", menu, 'Assets/statistic_table.jpg', True, 500, 80)
    A1_totalcost_statboard = Button(menu.rect.left+50, menu.rect.top+300, "A1's Total Cost: xxxxx", menu, 'Assets/statistic_table.jpg', True, 500, 80)
    A1_cursteps_statboard = Button(menu.rect.left+50, menu.rect.top+400, "A1's Current Steps: xxxxx", menu, 'Assets/statistic_table.jpg', True, 500, 80)

    play_button = Button(menu.rect.left+200, menu.rect.top+700, "Play", menu, 'Assets/orange_button.png', True, 210, 50)
    pause_button = Button(menu.rect.left+200, menu.rect.top+760, "Pause", menu, 'Assets/orange_button.png', True, 210, 50)
    reset_button = Button(menu.rect.left+200, menu.rect.top+820, "Reset", menu, 'Assets/orange_button.png', True, 210, 50)
    load_button = Button(menu.rect.left+200, menu.rect.top+880, "Load Map", menu, 'Assets/orange_button.png', True, 210, 50)
    quit_button = Button(menu.rect.left+200, menu.rect.top+940, "Quit", menu, 'Assets/orange_button.png', True, 210, 50)



    camera_groups: list[CameraGroup] = []
    # camera_group = pygame.sprite.Group()

    # Map setups
    displayMaps: list[DisplayMap] = []
    for i in range(f):
        camera_groups.append(CameraGroup(map_surface))
        displayMaps.append(DisplayMap(map[i], camera_groups[i]))


    paths = []

    # Backups
    agentCoordBU = copy.deepcopy(agentCoord)

    # Flags
    is_playing: bool = False
    cur_step_idices = [0 for _ in range(len(agentCoord))]
    n_steps = [0 for _ in range(len(agentCoord))]

    # Find paths
    for i in range(len(agentCoord)):
        paths.append(findPath(g, vertexType, agent_index = i+1))
        n_steps[i] = len(paths[i])

    A1_totalcost_statboard.changeText("A1's Total Cost: " + str(len(paths[0])))
    A1_cursteps_statboard.changeText("A1's Current Steps: 0")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEWHEEL:
                camera_groups[agentCoord[0][1]].zoom_scale += event.y * 0.06
                if event.y < 0 and camera_groups[agentCoord[0][1]].zoom_scale < 0.3:
                    camera_groups[agentCoord[0][1]].zoom_scale = 0.3
                if event.y > 0 and camera_groups[agentCoord[0][1]].zoom_scale > 1.3:
                    camera_groups[agentCoord[0][1]].zoom_scale = 1.3
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1):
                    if play_button.checkForInput(pygame.mouse.get_pos()):
                        is_playing = True

                    if pause_button.checkForInput(pygame.mouse.get_pos()):
                        is_playing = False

                    if reset_button.checkForInput(pygame.mouse.get_pos()):
                        is_playing = False
                        cur_step_idices = [0 for _ in range(len(agentCoord))]
                        agentCoord = copy.deepcopy(agentCoordBU)

                        for cg in camera_groups:
                            cg.empty()
                        # camera_groups[agentCoord[0][1]].empty()
                        displayMaps: list[DisplayMap] = []
                        for i in range(f):
                            displayMaps.append(DisplayMap(map[i], camera_groups[i]))

                        A1_cursteps_statboard.changeText("A1's Current Steps: 0")

                    if load_button.checkForInput(pygame.mouse.get_pos()):
                        f = prompt_file()
                        main(f)
                        return
                    
                    if quit_button.checkForInput(pygame.mouse.get_pos()):
                        exit()
                                     
        if is_playing:
            for agent_idx in range(len(agentCoord)):
                if cur_step_idices[agent_idx] < n_steps[agent_idx]:
                    if play_path(map, paths[agent_idx], displayMaps, agentCoord, agent_idx, cur_step_idices[agent_idx]):
                        cur_step_idices[agent_idx] += 1
                        camera_groups[agentCoord[agent_idx][1]].update()
                        if agent_idx == 0:
                            A1_cursteps_statboard.changeText("A1's Current Steps: " + str(cur_step_idices[agent_idx]))
                pygame.time.delay(0)

        # camera_group.update()
        camera_groups[agentCoord[0][1]].custom_draw(map_surface)
        # camera_group.draw(map_surface)

        cur_floor_statboard.changeText("A1's current Floor: " + str(agentCoord[0][1]+1))
        
        menu.update(pygame.mouse.get_pos())
        menu.draw_menu(screen)
        
        pygame.display.flip()
        
main('input.txt')