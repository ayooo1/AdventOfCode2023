from collections import deque
with open('Days of Advent Code\Day 16\input.txt','r') as file:
    fp = [x.strip() for x in file.readlines()]
    temp = fp
    fp = []
    ret = 0

    for i in range(len(temp)):
        lst = []
        for j in range(len(temp[0])):
            lst.append(temp[i][j])
        fp.append(lst)


    moves = {('|','r'): [(-1,0,'u'),(1,0,'d')], 
    ('|','l'): [(-1,0,'u'),(1,0,'d')], 
    ('|','u'):[(-1,0,'u')], 
    ('|','d'): [(1,0,'d')],
    ('-','r'): [(0,1,'r')],
    ('-','l'): [(0,-1,'l')],
    ('-','u'): [(0,-1,'l'),(0,1,'r')],
    ('-','d'): [(0,-1,'l'),(0,1,'r')],
    ('/','d'): [(0,-1,'l')],
    ('/','u'): [(0,1,'r')],
    ('/','r'): [(-1,0,'u')],
    ('/','l'): [(1,0,'d')],
    ('\\','d'): [(0,1,'r')],
    ('\\','u'): [(0,-1,'l')],
    ('\\','r'): [(1,0,'d')],
    ('\\','l'): [(-1,0,'u')],
    'r': (0,1),
    'l': (0,-1),
    'd': (1,0),
    'u': (-1,0)}

    m = len(fp)
    n = len(fp[0])
    temp1 = [[0]*n for _ in range(m)]

    lst = []
    for j in range(n):
        lst.append((0,j,'d'))
        lst.append((m-1,j,'u'))
    
    for i in range(m):
        lst.append((i,0,'r'))
        lst.append((i,n-1,'l'))

    for startx,starty,startd in lst:
        temp1 = [[0]*n for _ in range(m)]
        q = deque([(startx,starty,startd)])
        s = set()
        s.add((startx,starty,startd))
        while q:
            x,y,d = q.popleft()
            if fp[x][y] == '.':
                temp1[x][y] = 1
                r,c = x+moves[d][0],y+moves[d][1]
                if -1<r<m and -1<c<n and (r,c,d) not in s:
                    q.append((r,c,d))
                    s.add((r,c,d))
            else:
                for dx,dy,dd in moves[(fp[x][y],d)]:
                    r,c = x+dx,y+dy
                    if -1<r<m and -1<c<n and (r,c,dd) not in s:
                        q.append((r,c,dd))
                        s.add((r,c,dd))
                temp1[x][y] = 1

        ans = 0
        for i in range(len(fp)):
            for j in range(len(fp[0])):
                ans += temp1[i][j]
        ret = max(ans,ret)

    print(ret)
        