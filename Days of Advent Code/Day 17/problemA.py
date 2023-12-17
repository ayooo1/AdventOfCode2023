from heapq import heappush,heappop

with open('Days of Advent Code\Day 17\input.txt','r') as file:
    fp = [x.strip() for x in file.readlines()]
    temp = fp
    fp = []
    
    for i in range(len(temp)):
        lst = []
        for j in range(len(temp[0])):
            lst.append(int(temp[i][j]))
        fp.append(lst)

    m,n = len(fp),len(fp[0])

    moves = {'r': (0,1),'l': (0,-1), 'u':(-1,0),'d': (1,0)}
    op = {'r':'l','l':'r','d':'u','u':'d'}
    h = []
    cache = {}


    for key in moves.keys():
        heappush(h,(0,0,0,0,key))
        cache[(0,0,0,key)] = 1

    while h:
        cc,x,y,l,d = heappop(h)
        if x == m-1 and y == n-1:
            print(cc)
            break
        for dd,(dx,dy) in moves.items():
            r,c = dx+x,y+dy
            streak = l+1 if dd == d else 0
            if -1<r<m and -1<c<n and cache.get((r,c,streak,dd),0) == 0 and streak < 3 and op[d] != dd:
                heappush(h,(cc+fp[r][c],r,c,streak,dd))
                cache[(r,c,streak,dd)] = 1