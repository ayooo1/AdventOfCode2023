from collections import deque

with open('Days of Advent Code\Day 10\input.txt','r') as file:
    moves = {'|': [(1,0),(-1,0)], '-': [(0,1),(0,-1)], 'F':[(0,1),(1,0)], 'J': [(-1,0),(0,-1)], '7': [(1,0),(0,-1)], 'L':[(-1,0),(0,1)],'S':[(1,0),(0,1),(-1,0),(0,-1)]}
    comein = {'|': [(-1,0),(1,0)], '-': [(0,-1),(0,1)], 'F':[(0,-1),(-1,0)], 'J': [(1,0),(0,1)], '7': [(-1,0),(0,1)], 'L':[(1,0),(0,-1)]}
    move = [(0,1),(0,-1),(1,0),(-1,0)]

    fp = file.readlines()
    m,n = len(fp), len(fp[0])-1
    start = None
    for i in range(m):
        for j in range(n):
            if fp[i][j] == 'S':
                start = (i,j)
    
    q = deque([start])
    depth = 0
    s = set()
    s.add(start)
    grid = [[0]*(n**2) for _ in range(m**2)]
    while q:
        size = len(q)
        depth += 1
        for _ in range(size):
            x,y = q.popleft()
            for dx,dy in moves[fp[x][y]]:
                r = x+dx
                c = y+dy
                if -1<r<m and -1<c<n and fp[r][c] != '.' and (r,c) not in s:
                    if (dx,dy) not in comein[fp[r][c]]:
                        continue
                    q.append((r,c))
                    s.add((r,c))

    tube = s
    #Part 2: find number of squares within the loop
    res=0
    # viable = []
    for j in range(n):
        par = 0
        lr = 0
        #0: not in a vertical tube space
        #-1: to the left
        #1: to the right
        for i in range(m):
            if (i,j) not in tube:
                if par:
                    # viable.append((i,j))
                    res+=1
            else:
                if par:
                    match fp[i][j]:
                        case '-': par^=1
                        case 'J':
                            par^=(lr==-1)
                            lr = 0
                        case 'L':
                            par^=(lr==1)
                            lr = 0
                        case '7':
                            par^=1
                            lr = -1
                        case 'F':
                            par^=1
                            lr = 1
                else:
                    match fp[i][j]:
                        case '-': par^=1
                        case 'J':
                            par^=(lr==-1)
                            lr = 0
                        case 'L':
                            par^=(lr==1)
                            lr = 0
                        case '7':
                            par^=1
                            lr = -1
                        case 'F':
                            par^=1
                            lr = 1
    # print(sorted(viable))
    print(res)

    '''
    
    looked at reddit for answer hard ass problem :/
    should have been a math major
    
    '''


    
    