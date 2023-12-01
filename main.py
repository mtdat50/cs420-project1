from function import *
from time import sleep

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


path, nodes = findPath(g, vertexType, agent_index = 1)


for step in path:
    agent1Coord = [agentCoord[0][1], agentCoord[0][2] , agentCoord[0][3]]
    agent1Coord[1] += step[0]
    agent1Coord[2] += step[1]

    if map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] == 'UP':
        agent1Coord[0] += 1
    elif map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] == 'DO':
        agent1Coord[0] -= 1

    # output(map, agents_coord = agentCoord)
    print(step, agent1Coord)
    if map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]] != '0':
        print(map[agent1Coord[0]][agent1Coord[1]][agent1Coord[2]])
    
    agentCoord[0] = (agentCoord[0][0], agent1Coord[0], agent1Coord[1], agent1Coord[2])
    sleep(0.25)