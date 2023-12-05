from collections import defaultdict

special = {'!','@','#','$','%','&','*','-','+','?','=','/'}

file = open('Day 3\input.txt','r')
fp = file.readlines()
m,n = len(fp), len(fp[0])

moves = [(1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1)]
temp = []

for line in fp:
    temp.append(line.rstrip().strip())

m,n = len(temp), len(temp[0])

def p2(x):
    ret = 0
    char = ''
    c = defaultdict(list)
    for i in range(m):
        cur = 0
        found = None
        x[i] += '.'
        for j in range(n+1):
            if not x[i][j].isnumeric():
                if cur > 0 and found is not None:
                    c[found].append(cur)
                cur = 0
                found = None
                char = ''
            
            else:
                cur = cur * 10 + int(x[i][j])
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx,ny = i+dx, j+dy

                        if -1<nx<m and -1<ny<n-1 and x[nx][ny] == '*':
                            found = (nx,ny)
        
    for k in c.keys():
        if len(c[k]) == 2:
            ret += c[k][0] * c[k][1]
    
    print(ret)

p2(temp)