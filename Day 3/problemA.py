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

def p1(x):
    ret = 0
    for i in range(m):
        cur = 0
        found = 0

        x[i] += '.'
        for j in range(n+1):
            if not x[i][j].isnumeric():
                if cur > 0 and found:
                    ret += cur
                cur = 0
                found = 0
            
            else:
                cur = cur * 10 + int(x[i][j])
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx,ny = i+dx, j+dy

                        if -1<nx<m and -1<ny<n-1 and x[nx][ny] != '.' and not x[nx][ny].isnumeric():
                            found = 1
        
    print(ret)

p1(temp)


# special = {'!','@','#','$','%','&','*','-','+','?','=','/'}

# file = open('Day 3\input.txt','r')
# fp = file.readlines()
# m,n = len(fp), len(fp[0])

# moves = [(1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1)]
# temp = []

# for line in fp:
#     temp.append(line.rstrip().strip())

# m,n = len(temp), len(temp[0])


# def getNum(x,y):
#     i,j = 0,0
#     while y-i > -1 and y+j < n and (temp[x][y-i].isdigit() or temp[x][y+j].isdigit()):
#         if temp[x][y-i].isdigit():
#             i += 1
#         if temp[x][y+j].isdigit():
#             j += 1

#     return int(temp[x][y-i+1:y+j])

# def check(x,y):
#     s = set()
#     ret = 0
#     for i,j in moves:
#         r = i+x
#         c = j+y
#         if temp[r][c].isdigit():
#             num = getNum(r,c)
#             if num not in s:
#                 ret += num
#                 s.add(num)
#     print(list(s))
#     return ret


# ans = 0
# for i in range(m):
#     for j in range(n):
#         if temp[i][j] in special:
#             ans += check(i,j)

# print(ans)