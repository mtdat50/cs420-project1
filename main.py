import pygame
from function import *
from time import sleep
from DisplayMap import DisplayMap, Node
from const import *

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

displayMaps: list[DisplayMap] = []
for i in range(f):
    displayMaps.append(DisplayMap(map[i]))

pygame.init()
surface = pygame.display.set_mode(RESOLUTION)
displayMaps[0].draw_map(surface)

path = []
for i in range(len(agentCoord)):
    path.append(findPath(g, vertexType, agent_index = i + 1))

agent1Floor = agentCoord[0][1]
for istep in range(len(path[0])):
    for agent in range(len(agentCoord)):
        step = (0, 0)
        if istep < len(path[agent]):
            step = path[agent][istep]

        coord = [agentCoord[agent][1], agentCoord[agent][2] , agentCoord[agent][3]]

        cur_floor = coord[0]
        cur_row = coord[1]
        cur_col = coord[2]
        cur_cell_id = cur_row*n + cur_col

        displayMaps[agent1Floor].grid[cur_cell_id].update_node_type('0', surface)

        # print(displayMaps[cur_floor].grid[cur_cell_id].nodeType, displayMaps[cur_floor].grid[cur_cell_id].color
        #       , displayMaps[cur_floor].grid[cur_cell_id].text_color)

        coord[1] += step[0]
        coord[2] += step[1]

        
        if map[coord[0]][coord[1]][coord[2]] == 'UP':
            coord[0] += 1
        elif map[coord[0]][coord[1]][coord[2]] == 'DO':
            coord[0] -= 1
        
        if agent == 0:
            agent1Floor = coord[0]

        cur_row = coord[1]
        cur_col = coord[2]
        cur_cell_id = cur_row*n + cur_col
        displayMaps[agent1Floor].grid[cur_cell_id].update_node_type(agentCoord[agent][0], surface)

        pygame.time.delay(PYGAME_DELAY)
        pygame.display.update()
        
        # print(step, agent1Coord)
        # if map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] != '0':
        #     print(map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]])
        
        agentCoord[agent] = (agentCoord[agent][0], coord[0], coord[1], coord[2])
        sleep(0.05)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()