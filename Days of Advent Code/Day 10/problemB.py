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

    ans = 0
    ss = set()
    for x,y in s:
        for dx,dy in move:
            r,c = x+dx, y+dy
            if -1<r<m and -1<c<n and fp[r][c] == '.':
                q = deque([(r,c)])
                flag = 1
                inner_s = set()
                inner_s.add((r,c))
                while q:
                    j,k = q.popleft()
                    for d,dd in move:
                        new_j, new_k = j+d, k+dd
                        if new_j < 0 or new_j >= m or new_k < 0 or new_k >= n not in inner_s:
                            flag = 0
                            inner_s.add((new_j,new_k))
                        if -1<new_j<m and -1<new_k<n and fp[new_j][new_k] == '.' and (new_j,new_k) not in inner_s:
                            inner_s.add((new_j,new_k))
                            q.append((new_j,new_k))
        
                if flag:
                    ss.update(inner_s)

    for x,y in ss:
        grid[x][y] = 'Y'

    for row in grid:
        print(row)
    print(ss)
    print(len(ss))

    '''
    
    looked at reddit for answer hard ass problem :/
    should have been a math major
    
    '''


    
    