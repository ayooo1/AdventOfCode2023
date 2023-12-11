from collections import Counter,deque
from math import sqrt
import heapq

with open('Days of Advent Code\Day 11\input.txt','r') as file:
    fp = [x.strip() for x in file.readlines()]
    m,n = len(fp), len(fp[0])

    lstr = []
    lstc = []

    for i in range(m):
        if '#' not in fp[i]:
            lstr.append(i)
    
    for j in range(n):
        c = Counter()
        for i in range(m):
            c[fp[i][j]] += 1

        if not c['#']:
            lstc.append(j)

    lst = []

    for i in range(m):
        for j in range(n):
            if fp[i][j] == '#':
                lst.append((i,j))

    new_lst = []
    for x,y in lst:
        xx,yy = 0,0
        for i in lstr:
            if x > i:
                xx += 999999
        for j in lstc:
            if y > j:
                yy += 999999
        new_lst.append((x+xx,y+yy))
    
    ans = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            ans += 2 * min(abs(new_lst[i][0]-new_lst[j][0]), abs(new_lst[i][1]-new_lst[j][1])) + abs(abs(new_lst[i][0]-new_lst[j][0]) - abs(new_lst[i][1]-new_lst[j][1]))
    print(ans)
            