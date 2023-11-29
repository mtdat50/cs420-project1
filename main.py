from function import *
from time import sleep

map, agentCoord = input()
f = len(map)
m = len(map[0])
n = len(map[0][0])



g, vertexType= convert2Graph(map, agentCoord = agentCoord)
path = findPath(g, agent_index = 1)


for step in path:
    agentCoord[0][2] += step[0]
    agentCoord[0][3] += step[1]

    if map[agentCoord[0][1]][agentCoord[0][2]][agentCoord[0][3]] == 'UP':
        agentCoord[0][1] += 1
    elif map[agentCoord[0][1]][agentCoord[0][2]][agentCoord[0][3]] == 'DO':
        agentCoord[0][1] -= 1

    output(map, agents_coord = agentCoord)
    sleep(0.5)