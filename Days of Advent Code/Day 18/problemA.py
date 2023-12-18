from collections import deque

with open('Days of Advent Code\Day 18\input.txt','r') as file:
    fp = [x.strip() for x in file.readlines()]
    curr = (0,0)
    moves = {'R': (0,1), 'D': (1,0), 'L': (0,-1), 'U': (-1,0)}
    pts = []
    perimeter = 0
    for line in fp:
        prev = curr
        x,y,z = line.strip().split(' ')
        y = int(y)
        curr = curr[0]+moves[x][0]*y, curr[1]+moves[x][1]*y
        pts.append((prev, curr))
        perimeter += y

    pts.append((curr,(0,0)))

    #shoelace theorem
    area = 0
    for e in pts:
        (a,b) = e
        area += a[1] * b[0] - a[0] * b[1]
    area = int(abs(area) / 2)
    
    #picks theorem
    interior = int(area - perimeter / 2 + 1)

    print(perimeter + interior)
    



        
    



