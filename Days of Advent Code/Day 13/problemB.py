from collections import deque
#39359
with open('Days of Advent Code\Day 13\input.txt','r') as file:
    fp = file.readlines()
    graph = []
    top = []
    f = 0
    for line in fp:
        line = line.strip()
        if line != '':
            top.append(line)
        else:
            graph.append(top)
            top = []
    graph.append(top)

    def order(x1,x2):
        q1 = deque(x1)
        q2 = deque(x2)
        f = 0
        while q1:
            if q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
            else:
                f += 1
                if f > 1:
                    return -1
                q1.popleft()
                q2.popleft()

        return f


    def rcheck(g):
        for i in range(len(g)-1,0,-1):
            l,r = [g[i-1]],[g[i]]
            p1,p2 = i-1,i
            f = 0
            while p1 != 0 and p2 != len(g)-1:
                boo = order(g[p1],g[p2])
                if boo != -1:
                    if boo == 1:
                        f += 1
                    p1 -= 1
                    p2 += 1
                else:
                    break
                if f == 1:
                    r.append(g[p2])
                    l.append(g[p2])
                else:
                    r.append(g[p1])
                    l.append(g[p2])
            
            boo = order(g[p1],g[p2])
            if boo != -1:
                if boo == 1:
                    f += 1
                if (p1 == 0 or p2 == len(g) - 1) and f==1:
                    return i
        return -1
    
    def ccheck(g):
        for j in range(len(g[0])-1,0,-1):
            l,r = j-1,j
            ll,rr = [],[]
            lhash = []
            rhash = []
            f = 0
            for i in range(len(g)):
                ll.append(g[i][l])
                rr.append(g[i][r])
            lhash.append(ll)
            rhash.append(rr)
            while l != 0 and r != len(g[0])-1:
                boo = order(ll,rr)
                if boo != -1:
                    if boo == 1:
                        f += 1
                    l -= 1
                    r += 1
                else:
                    break
                ll,rr = [],[]
                for i in range(len(g)):
                    ll.append(g[i][l])
                    rr.append(g[i][r])
                lhash.append(ll)
                rhash.append(rr)
            
            boo = order(ll,rr)
            if boo != -1:
                if boo == 1:
                    f += 1
                if (l == 0 or r == len(g[0]) -1) and f == 1:
                    return j
        return -1



    ans = 0
    for x in graph:
        r = rcheck(x)
        c = ccheck(x)
        if r != -1:
            ans += 100*r
        if c != -1:
            ans += c
    
    print(ans)
