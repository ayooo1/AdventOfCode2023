from collections import deque

with open('Days of Advent Code\Day 18\input.txt','r') as file:
    fp = [x.strip() for x in file.readlines()]
    curr = (0,0)
    moves = {0: (0,1), 1: (1,0), 2: (0,-1), 3: (-1,0)}
    pts = []
    perimeter = 0
    for line in fp:
        prev = curr
        x,y,z = line.strip().split(' ')
        z = z.strip()
        y,x = int(z[2:7],16),int(z[7])
        curr = curr[0]+moves[x][0]*y, curr[1]+moves[x][1]*y
        pts.append((prev, curr))
        perimeter += y

    pts.append((curr,(0,0)))

    #shoelace
    area = 0
    for e in pts:
        (a,b) = e
        area += a[1] * b[0] - a[0] * b[1]
    area = int(abs(area) / 2)

    #picks theorem
    sq = int(area - perimeter / 2 + 1)

    print(perimeter + interior)
    



        
    



