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
print(vertexType)

displayMaps: list[DisplayMap] = []
for i in range(f):
    displayMaps.append(DisplayMap(map[i]))

pygame.init()
surface = pygame.display.set_mode(RESOLUTION)
displayMaps[0].draw_map(surface)

path, nodes = findPath(g, vertexType, agent_index = 1)


for step in path:
    agent1Coord = [agentCoord[0][1], agentCoord[0][2] , agentCoord[0][3]]

    cur_floor = agent1Coord[0]
    cur_floor_n_rows = len(map[0])
    cur_floor_n_cols = len(map[0][0])
    
    cur_row = agent1Coord[1]
    cur_col = agent1Coord[2]
    cur_cell_id = cur_row*cur_floor_n_cols + cur_col

    displayMaps[cur_floor].grid[cur_cell_id].update_node_type('0', surface)

    # print(displayMaps[cur_floor].grid[cur_cell_id].nodeType, displayMaps[cur_floor].grid[cur_cell_id].color
    #       , displayMaps[cur_floor].grid[cur_cell_id].text_color)

    agent1Coord[1] += step[0]
    agent1Coord[2] += step[1]

    if map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] == 'UP':
        agent1Coord[0] += 1
    elif map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] == 'DO':
        agent1Coord[0] -= 1

    cur_row = agent1Coord[1]
    cur_col = agent1Coord[2]
    cur_cell_id = cur_row*cur_floor_n_cols + cur_col
    displayMaps[cur_floor].grid[cur_cell_id].update_node_type('A1', surface)

    pygame.time.delay(PYGAME_DELAY)
    pygame.display.update()
    
    # print(step, agent1Coord)
    # if map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] != '0':
    #     print(map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]])
    
    agentCoord[0] = (agentCoord[0][0], agent1Coord[0], agent1Coord[1], agent1Coord[2])
    # sleep(0.25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()