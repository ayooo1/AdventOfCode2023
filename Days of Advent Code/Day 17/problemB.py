from heapq import heappush,heappop
from collections import defaultdict
import math

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
    cache = defaultdict(lambda: math.inf)
    cache1 = [[0]*n for _ in range(m)]


    for key in moves.keys():
        heappush(h,(0,0,0,0,key))
        cache[(0,0,0,key)] = fp[0][0]


    while h:
        cc,x,y,streak,d = heappop(h)
        if x == m-1 and y == n-1:
            print(cc)
            break
        
        for dd,(dx,dy) in moves.items():
            r,c = dx+x,y+dy
            if -1<r<m and -1<c<n:
                if dd == d:
                    if streak + 1 <= 10:
                        if cache[(r,c,streak+1,d)] > cache[(x,y,streak,d)] + fp[r][c]:
                            cache[(r,c,streak+1,d)] = cache[(x,y,streak,d)] + fp[r][c]
                            heappush(h,(cache[(r,c,streak+1,d)],r,c,streak+1,d))
                elif op[d] != dd:
                    if streak >= 4:
                        if cache[(r,c,1,d)] > cache[(x,y,streak,d)] + fp[r][c]:
                            cache[(r,c,1,d)] = cache[(x,y,streak,d)] + fp[r][c]
                            heappush(h,(cache[(r,c,1,d)],r,c,1,d))


# had to look at sub reddit cant see whats wrong with my code

#1149