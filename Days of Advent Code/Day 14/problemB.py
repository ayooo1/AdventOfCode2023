from collections import deque,Counter

with open('Days of Advent Code\Day 14\input.txt','r') as file:
    fp = file.readlines()
    temp = []
    for i in range(len(fp)):
        fp[i] = list(fp[i].strip())

    def p():
        for row in fp:
            print(row)
        print()
    lst1 = [93701,93698,93694,93688,93683,93684,93688,93678,93686,93720,93740,93730,93731,93738,93746,93751,93743,93728,93730,93731,93735,93736,93724,93713,93725,93718]
    c = {i:-1 for i in lst1}

    for _ in range(2000):
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

        #EAST

        for i in range(len(fp)):
            s = deque()
            last = 0
            for j in range(len(fp[0])):
                if fp[i][j] == 'O':
                    s.append(j)
                elif fp[i][j] == '#':
                    x = 0
                    while x != len(s):
                        fp[i][last] = 'O'
                        last += 1
                        x += 1
                    while s:
                        t = s.popleft()
                        if t >= last:
                            fp[i][t] = '.'
                    last = j+1
            x = 0
            while x != len(s):
                fp[i][last] = 'O'
                last += 1
                x += 1
            while s:
                t = s.popleft()
                if t >= last:
                    fp[i][t] = '.'

        # SOUTH

        for j in range(len(fp[0])):
            s = deque()
            last = len(fp)-1
            for i in range(len(fp)-1,-1,-1):
                if fp[i][j] == 'O':
                    s.append(i)
                elif fp[i][j] == '#':
                    x = 0
                    while x != len(s):
                        fp[last][j] = 'O'
                        last -= 1
                        x += 1
                    while s:
                        t = s.popleft()
                        if t <= last:
                            fp[t][j] = '.'
                    last = i-1
            x = 0
            while x != len(s):
                fp[last][j] = 'O'
                last -= 1
                x += 1
            while s:
                t = s.popleft()
                if t <= last:
                    fp[t][j] = '.'

        # WEST

        for i in range(len(fp)):
            s = deque()
            last = len(fp[0])-1
            for j in range(len(fp[0])-1,-1,-1):
                if fp[i][j] == 'O':
                    s.append(j)
                elif fp[i][j] == '#':
                    x = 0
                    while x != len(s):
                        fp[i][last] = 'O'
                        last -= 1
                        x += 1
                    while s:
                        t = s.popleft()
                        if t <= last:
                            fp[i][t] = '.'
                    last = j-1
            x = 0
            while x != len(s):
                fp[i][last] = 'O'
                last -= 1
                x += 1
            while s:
                t = s.popleft()
                if t <= last:
                    fp[i][t] = '.'
    
        ans = 0
        for i in range(len(fp)):
            count = 0
            for j in range(len(fp[0])):
                if fp[i][j] == 'O':
                    count += 1
        
            ans += (len(fp)-i)*count
        c[_] = ans


    q = 1000000000 - 1209
    q %= 26
    print(q)
    print(c[1209+25-1])