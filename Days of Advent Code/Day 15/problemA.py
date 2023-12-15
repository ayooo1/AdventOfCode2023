with open('Days of Advent Code\Day 15\input.txt','r') as file:
    fp = file.readline().split(',')
    ans = 0
    for line in fp:
        s = 0
        for c in line:
            s += ord(c)
            s*=17
            s%=256
        ans += s
    
    print(ans)