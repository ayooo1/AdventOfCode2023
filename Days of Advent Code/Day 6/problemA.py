import numpy

file = open('Days of Advent Code\Day 6\input.txt','r')
time = [int(x) for x in file.readline().split(':')[1].strip().split()]
dist = [int(x) for x in file.readline().split(':')[1].strip().split()]


def dp(x,t):
    if t == 0:
        return x

    if (x,t) in cache:
        return cache[(x,t)]

    ans = max(dp(x+1,t-1),x*t)
    lst.append(x*t)

    cache[(x,t)] = ans

    return ans

ret = []
for i,t in enumerate(time):
    lst = []
    cache = {}
    dp(0,t)
    c = 0
    for v in lst:
        if v > dist[i]:
            c += 1
    ret.append(c)

print(numpy.prod(ret))
