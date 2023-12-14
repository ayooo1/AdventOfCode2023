from collections import deque

with open('Days of Advent Code\Day 14\input.txt','r') as file:
    fp = file.readlines()
    temp = []
    for i in range(len(fp)):
        fp[i] = list(fp[i].strip())

    def p():
        for row in fp:
            print(row)
        print()

    #NORTH

    for j in range(len(fp[0])):
        s = deque()
        last = 0
        for i in range(len(fp)):
            if fp[i][j] == 'O':
                s.append(i)
            elif fp[i][j] == '#':
                x = 0
                while x != len(s):
                    fp[last][j] = 'O'
                    last += 1
                    x += 1
                while s:
                    t = s.popleft()
                    if t >= last:
                        fp[t][j] = '.'
                last = i+1
        x = 0
        while x != len(s):
            fp[last][j] = 'O'
            last += 1
            x += 1
        while s:
            t = s.popleft()
            if t >= last:
                fp[t][j] = '.'

    ans = 0
    for i in range(len(fp)):
        c = 0
        for j in range(len(fp[0])):
            if fp[i][j] == 'O':
                c += 1
        
        ans += (len(fp)-i)*c
    
    print(ans)