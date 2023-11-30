from function import *
from time import sleep

map, agentCoord = input('input.txt')
f = len(map)
m = len(map[0])
n = len(map[0][0])


g, vertexType= convert2Graph(map, agentCoord = agentCoord)
for vertex, edgeList in enumerate(g):
    print(vertex, vertexType[vertex], '====')
    for edge in g[vertex]:
        print(edge[0], vertexType[edge[0]])
        print(edge[1])
print(vertexType)


path, nodes = findPath(g, vertexType, agent_index = 1)
# print(path)
# for node in nodes:
#     print(vertexType[node])


# for step in path:
#     agentCoord[0] = (agentCoord[0][0], agentCoord[0][1], agentCoord[0][2] + step[0], agentCoord[0][3])
#     agentCoord[0] = (agentCoord[0][0], agentCoord[0][1], agentCoord[0][2], agentCoord[0][3] + step[1])

#     if map[agentCoord[0][1]][agentCoord[0][2]][agentCoord[0][3]] == 'UP':
#         agentCoord[0] = (agentCoord[0][0], agentCoord[0][1] + 1, agentCoord[0][2], agentCoord[0][3])
#     elif map[agentCoord[0][1]][agentCoord[0][2]][agentCoord[0][3]] == 'DO':
#         agentCoord[0] = (agentCoord[0][0], agentCoord[0][1] - 1, agentCoord[0][2], agentCoord[0][3])

#     # output(map, agents_coord = agentCoord)
#     print(agentCoord[0][2], agentCoord[0][3])
#     if map[agentCoord[0][1]][agentCoord[0][2]][agentCoord[0][3]] != '0':
#         print(map[agentCoord[0][1]][agentCoord[0][2]][agentCoord[0][3]])
#     sleep(0.25)