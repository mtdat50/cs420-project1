from collections import deque
from queue import PriorityQueue

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
        m, n = filein.readline()[:-1].split(',')
        m = int(m)
        n = int(n)
        # map[f][m][n] for f floors, m rows, n columns
        map = [[[] * n for i in range(m)] for j in range(f)]
        
        for k in range(f):
            filein.readline()
            for i in range(m):
                map[k][i] = filein.readline()[:-1].split(',')
                for j in range(len(map[0][0])):
                    if map[k][i][j][0] == 'A':
                        agentCoord.append((map[k][i][j], k, i, j))

    #Sort agent by name, form A1 -> Ak
    agentCoord.sort(key=lambda tup: tup[0])
                    
    return map, agentCoord


#draw the floor where agent A1 is on
def output(map, agents_coord): #list of agents' current position, [][1] = floor, [][2] = row, [][3] = column
    TODO


def _tracePath(steppingTrack, r, c, sourceR, sourceS):
    path = []
    while r != sourceR or c != sourceS:
        path.append(steppingTrack[r][c])
        step = steppingTrack[r][c]
        r -= step[0]
        c -= step[1]
    
    path.reverse()
    return path


#convert matrix to graph, vertices are objects on the map, edges are paths between objects
def convert2Graph(map, agentCoord): 
    g = []
    vertexType = []
    objectCoord = []
    objIndexList = {}
    for agent in agentCoord:
        objIndexList[(agent[1], agent[2], agent[3])] = len(g)
        g.append([])
        vertexType.append(map[agent[1]][agent[2]][agent[3]])
        objectCoord.append((agent[1], agent[2], agent[3]))
        
    f = len(map)
    m = len(map[0])
    n = len(map[0][0])
    for k in range(f):
        for i in range(m):
            for j in range(n):
                if map[k][i][j] != '0' and map[k][i][j] != '-1' and map[k][i][j][0] != 'A':
                    objectCoord.append((k, i, j))
                    objIndexList[(k, i, j)] = len(g)
                    g.append([])
                    vertexType.append(map[k][i][j])
                    if map[k][i][j] == 'UP':
                        objectCoord.append((k + 1, i, j))
                        objIndexList[(k + 1, i, j)] = len(g)
                        g[-1].append((len(g), [(0, 0)]))
                        g.append([])
                        vertexType.append('0')
                    if map[k][i][j] == 'DO':
                        objectCoord.append((k - 1, i, j))
                        objIndexList[(k - 1, i, j)] = len(g)
                        g[-1].append((len(g), [(0, 0)]))
                        g.append([])
                        vertexType.append('0')



    #for every object, bfs at its floor
    for obj in objectCoord:
        steppingTrack = [[(0, 0)] * n for i in range(m)]
        q = deque()
        q.append(obj)
        curObjIndex = objIndexList[(obj[0], obj[1], obj[2])]
        steppingTrack[obj[1]][obj[2]] = (-10, -10)

        while len(q) != 0:
            curF = q[0][0]
            curR = q[0][1]
            curC = q[0][2]
            q.popleft()

            if map[curF][curR][curC] == '-1':
                print('-1================')

            for i in range(-1, 2):
                newR = curR + i
                if newR < 0 or newR >= m:
                    continue

                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    newC = curC + j

                    if newC < 0 or newC >= n or map[curF][newR][newC] == '-1' or map[curF][newR][newC][0] == 'A':
                        continue
                    if i != 0 and j != 0 and (map[curF][curR][newC] == '-1' or map[curF][newR][curC] == '-1'):
                        continue
                    if steppingTrack[newR][newC] != (0, 0):
                        continue
                        
                    steppingTrack[newR][newC] = (i, j)
                    
                    if map[curF][newR][newC] == '0':
                        q.append((curF, newR, newC))
                    else:
                        newObjIndex = objIndexList[(curF, newR, newC)]
                        g[curObjIndex].append((newObjIndex, _tracePath(steppingTrack, newR, newC, obj[1], obj[2])))
    return g, vertexType


def _tracePath2(prevEdge, g, agent_index, u, keys):
    path = []
    nodes = [u]
    while u != (agent_index - 1) or keys != 0:
        prevVertex = prevEdge[u][keys][0]
        edgeIndex = prevEdge[u][keys][1]
        path = g[prevVertex][edgeIndex][1] + path
        keys = prevEdge[u][keys][2]
        u = prevVertex
        nodes.append(u)

    nodes.reverse()
    return path, nodes


#find a path from a selected agent to its target
def findPath(g, vertexType, agent_index): #g = adjacent list
    path = []
    prevEdge = [[(0, 0, 0)] * 1024 for i in range(len(g))] #store vertex and edge index leading to the state
    d = [[1e9] * 1024 for i in range(len(g))]
    q = PriorityQueue()
    q.put((0, agent_index - 1, 0))
    d[agent_index - 1][0] = 0


    while not q.empty():
        temp = q.get()
        d_u_keys = temp[0]
        u = temp[1]
        keys = temp[2]
        if d[u][keys] != d_u_keys:
            continue

        if vertexType[u][0] == 'T' and int(vertexType[u][1]) == agent_index:
            path = _tracePath2(prevEdge, g, agent_index, u, keys)
            break
        
        for i, edge in enumerate(g[u]):
            if vertexType[edge[0]][0] == 'D':
                if (keys >> (int(vertexType[edge[0]][1]) - 1)) & 1 == 0:
                    continue

            newKeys = keys
            if vertexType[edge[0]][0] == 'K':
                newKeys |= 1 << (int(vertexType[edge[0]][1]) - 1)
            
            if d[edge[0]][newKeys] <= d_u_keys + len(edge[1]):
                continue

            d[edge[0]][newKeys] = d_u_keys + len(edge[1])
            prevEdge[edge[0]][newKeys] = (u, i, keys)
            q.put((d[edge[0]][newKeys], edge[0], newKeys))

    #list of steps{deltaR, deltaC}
    return path

