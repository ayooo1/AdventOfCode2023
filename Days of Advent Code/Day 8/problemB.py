from collections import defaultdict,deque
from math import lcm
with open('Days of Advent Code\Day 8\input.txt','r') as file:
    instruction = list(file.readline().strip())
    dic = defaultdict(list)
    file.readline()
    s,i = deque(),0
    for line in file.readlines():
        start,left = line[0:3], line[5:]
        left = left.replace('(','')
        left = left.replace(')','')
        left = left.strip()
        left = left.replace(' ','')
        dic[start] = list(left.split(','))
        if start[-1] == 'A':
            s.append(start)
    
    steps = 1

    for x in s:
        q = deque([x])
        step = 0
        while q:
            cur = q.popleft()
            way = 0
            if cur[-1] == 'Z':
                steps = lcm(steps,step)
                break

            if instruction[i%len(instruction)] == 'R':
                way = 1
            q.append(dic[cur][way])
            i += 1
            step += 1
    
    print(steps)