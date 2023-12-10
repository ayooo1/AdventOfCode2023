from collections import deque

with open('Days of Advent Code\Day 10\input.txt','r') as file:
    moves = {'|': [(1,0),(-1,0)], '-': [(0,1),(0,-1)], 'F':[(0,1),(1,0)], 'J': [(-1,0),(0,-1)], '7': [(1,0),(0,-1)], 'L':[(-1,0),(0,1)],'S':[(1,0),(0,1),(-1,0),(0,-1)]}
    comein = {'|': [(-1,0),(1,0)], '-': [(0,-1),(0,1)], 'F':[(0,-1),(-1,0)], 'J': [(1,0),(0,1)], '7': [(-1,0),(0,1)], 'L':[(1,0),(0,-1)]}

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
        
    print(depth - 1)
    
    