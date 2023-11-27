UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
UPSTAIR = 4
SAMESTAIR = 5
DOWNSTAIR = 6

R = {-1, 0, 1, 0}
C = {0, 1, 0, -1}
F = {1, 0, -1}


def input():
    TODO

    #map[f][m][n] for f floors
    return map

#draw the floor where agent A1 is on
def output(map, agents_coord): #coord is agents' current position
    TODO


#agent -> key/target/up/down stair ; up/down -> key/target/up/down stair ; key -> door/other key ; door -> key/target
def convert2Graph(map): 
    TODO
    return #adjacent list g[n][...] = (adjacent vertex, path{UP, DOWN,...}) and list of agents, targets' index (which vertex if agent_i, which vertex is target_i)

#find a path from a selected agent to its target
def findPath(g, agent_index, target_index): #g = adjacent list
    return #list of steps{UP DOWN LEFT RIGHT} 

