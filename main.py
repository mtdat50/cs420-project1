from function import *
from time import sleep

map = input()
f = len(map)
m = len(map[0])
n = len(map[0][0])

#scan thro the map and get the agents coordinate
agents_coord = []


g, agents, targets = convert2Graph(map)
path = findPath(g, agent_index = agents[0], target_index = targets[0])


for step in path:
    if step < 4:
        agents_coord[0][1] += R[step]
        agents_coord[0][2] += C[step]
    else:
        agents_coord[0][0] += F[step - 4]

    output(map, agents_coord=agents_coord)
    sleep(0.5)