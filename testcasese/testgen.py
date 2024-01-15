input('test2.txt')
def input(filepath):
    f = 0
    m = 0
    n = 0
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
                line = filein.readline()
                if line[-1] == '\n':
                    line = line[:-1]
                map[k][i] = line.split(',')
                if (len(map[k][i])):
                    map[k][i].append('0')
                

    #Sort agent by name, form A1 -> Ak
    agentCoord.sort(key=lambda tup: tup[0])
                    
    return map, agentCoord


file = open('test2.csv', mode = 'w')
for i in range(200):
    for j in range(200):
        file.write('0')
        if j < 199:
            file.write(',')
    file.write('\n')
file.close()