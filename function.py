from collections import deque

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
UPLEFT = 4


# R = {-1, 0, 1, 0}
# C = {0, 1, 0, -1}
# F = {1, 0, -1}


def input(filepath):
    f = m = n = 0
    agentCoord = []
    map = []

    with open(filepath, 'r') as filein:
        while True:
            line = filein.readline()
            if line == '':
                break
            if line[0] == '[':
                f += 1

    with open(filepath, 'r') as filein:
        m = int(filein.read())
        n = int(filein.read())
        # map[f][m][n] for f floors, m rows, n columns
        map = [[[(0, 0)] * n for i in range(m)] for j in range(f)]
        
        for k in range(f):
            filein.readline()
            for i in range(m):
                map[k][i] = filein.readline().split(',')
                for j in range(len(map[0][0])):
                    if map[k][i][j][0] == 'A':
                        agentCoord.append((map[k][i][j], k, i, j))

    #Sort agent by name, form A1 -> Ak
    agentCoord.sort(key=lambda tup: tup[0])
                    
    return map, agentCoord


#draw the floor where agent A1 is on
def output(map, agents_coord): #list of agents' current position, [][1] = floor, [][2] = row, [][3] = column
    TODO

def _tracePath(steppingMap, r, c, sourceR, sourceS):
    path = []
    while r != sourceR and c != sourceS:
        path.append(steppingMap[r][c])
        r -= steppingMap[r][c][0]
        c -= steppingMap[r][c][1]
    
    path.reverse()
    return path

def convert2Graph(map, agentCoord): 
    g = [[]]
    vertexType = []
    objectCoord = []
    for agent in agentCoord:
        g.append([])
        vertexType.append(agent[0])
        objectCoord.append((agent[1], agent[2], agent[3]))

    f = len(map)
    m = len(map[0])
    n = len(map[0][0])
    for k in range(f):
        for i in range(m):
            for j in range(n):
                if map[k][i][j] != '0' and map[k][i][j] != '-1' and map[k][i][j][0] != 'A':
                    objectCoord.append((k, i, j))
                    g.append([])
                    vertexType.append(map[k][i][j])
                    if map[k][i][j] == 'UP':
                        objectCoord.append((k + 1, i, j))
                        g[-1].append((len(g), (0, 0)))
                        g.append([])
                        vertexType.append('0')
                    if map[k][i][j] == 'DO':
                        objectCoord.append((k - 1, i, j))
                        g[-1].append((len(g), (0, 0)))
                        g.append([])
                        vertexType.append('0')

    #for every object, bfs at its floor
    for obj in objectCoord:
        steppingMap = [[] * n for i in range(m)]
        q = deque()
        q.append(obj)
        curObjIndex = vertexType.index(map[obj[0]][obj[1]][obj[2]])

        while len(q) != 0:
            curF = q[0][0]
            curR = q[0][1]
            curC = q[0][2]
            q.popleft()

            for i in range(-1, 2):
                newR = curR + i
                if newR < 0 or newR >= m:
                    continue

                for j in range(-1, 2):
                    newC = curC + j
                    if newC < 0 or newC >= n or map[curF][newR][newC] == '-1' or map[curF][newR][newC][0] == 'A':
                        continue
                    if i != 0 and j != 0 and (map[curF][curR][newC] == '-1' or map[curF][newR][curC] == '-1'):
                        continue
                    
                    steppingMap[curF][newR][newC] = (i, j)
                    q.append((curF, newR, newC))

                    if map[curF][newR][newC] != '0':
                        newObjIndex = vertexType.index(map[curF][newR][newC])
                        g[curObjIndex].append((newObjIndex, _tracePath(steppingMap, newR, newC, obj[1], obj[2])))
    return g, vertexType

#find a path from a selected agent to its target
def findPath(g, agent_index): #g = adjacent list
    return #list of steps{deltaR, deltaC} 

