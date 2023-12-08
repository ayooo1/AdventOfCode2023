from collections import defaultdict,deque
with open('Days of Advent Code\Day 8\input.txt','r') as file:
    instruction = list(file.readline().strip())
    dic = defaultdict(list)
    file.readline()
    for line in file.readlines():
        start,left = line[0:3], line[5:]
        left = left.replace('(','')
        left = left.replace(')','')
        left = left.strip()
        left = left.replace(' ','')
        dic[start] = list(left.split(','))

    q,i = deque(['AAA']),0
    steps = 0
    while q:
        cur = q.popleft()
        if cur == 'ZZZ':
            print(steps)
            break
        way = 0
        if instruction[i%len(instruction)] == 'R':
            way = 1
        q.append(dic[cur][way])
        i += 1
        steps += 1
