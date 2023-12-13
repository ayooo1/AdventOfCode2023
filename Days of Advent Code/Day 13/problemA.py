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


    def rcheck(g):
        for i in range(len(g)-1,0,-1):
            l,r = [g[i-1]],[g[i]]
            p1,p2 = i-1,i
            while p1 != 0 and p2 != len(g)-1:
                if r == l:
                    p1 -= 1
                    p2 += 1
                else:
                    break
                r.append(g[p2])
                l.append(g[p1])
            if (p1 == 0 or p2 == len(g) - 1) and l == r:
                return i
        return -1
    
    def ccheck(g):
        f = 0
        for j in range(len(g[0])-1,0,-1):
            l,r = j-1,j
            ll,rr = [],[]
            lhash = {}
            rhash = {}  
            idx = 0
            for i in range(len(g)):
                ll.append(g[i][l])
                rr.append(g[i][r])
            lhash[idx] = ll
            rhash[idx] = rr
            while l != 0 and r != len(g[0])-1:
                ll,rr = [],[]
                idx += 1
                if lhash == rhash:
                    l -= 1
                    r += 1
                else:
                    break
                for i in range(len(g)):
                    ll.append(g[i][l])
                    rr.append(g[i][r])
                lhash[idx] = ll
                rhash[idx] = rr
            

            if (l == 0 or r == len(g[0]) -1) and lhash == rhash:
                return j
        return -1


    ans = 0
    for x in graph:
        r = rcheck(x)
        c = ccheck(x)
        print(r,c)
        if r != -1:
            ans += 100*r
        if c != -1:
            ans += c
    
    print(ans)
