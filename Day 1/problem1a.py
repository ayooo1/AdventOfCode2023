file = open('Day 1\input.txt','r')
ans = 0

def checknum(s):
    n = len(s)
    x = ''
    for i in range(n):
        if s[i].isdigit():
            x += s[i]
            break
    
    for i in range(n-1,-1,-1):
        if s[i].isdigit():
            x += s[i]
            break
    
    return int(x)


for s in file.readlines():
    ans += checknum(s.strip())

print(ans)