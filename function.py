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

#map value: 0 = empty 
#           -1 = wall 
#           1 = up stair 
#           2 = down stair 
#           1X = agents 
#           2X = targets 
#           3X = keys 
#           4X = doors

def input(filepath):
    f = m = n = 0

    with open(filepath, 'r') as filein:
        while True:
            line = filein.readline()
            if line == '':
                break
            if line[0] == '[':
                f = f + 1

    with open(filepath, 'r') as filein:
        m = int(filein.read())
        n = int(filein.read())
        map = [[[0] * n for i in range(m)] for j in range(f)]
        
        for k in range(f):
            filein.readline()
            
            for i in range(m):
                line = filein.readline()
                line = line.split(',')
                for j, s in enumerate(line):
                    match s:
                        case '0':
                            map[k][i][j] = 0
                        case '-1':
                            map[k][i][j] = -1
                        case 'UP':
                            map[k][i][j] = 1
                        case 'DO':
                            map[k][i][j] = 2
                        case _:
                            match s[0]:
                                case 'A':
                                    map[k][i][j] = 10
                                case 'T':
                                    map[k][i][j] = 20
                                case 'K':
                                    map[k][i][j] = 30
                                case 'D':
                                    map[k][i][j] = 40
                            map[k][i][j] += int(s[1]) - 1

    # map[f][m][n] for f floors, m rows, n columns
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

