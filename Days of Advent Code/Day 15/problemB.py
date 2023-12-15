from collections import defaultdict
class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
        self.prev = None
    
    def pop(self):
        self.next.prev = self.prev
        self.prev.next = self.next

class LinkList:
    def __init__(self):
        self.l = Node()
        self.r = Node()
        self.l.next = self.r
        self.r.prev = self.l
        self.length = 2
    
    def add(self,n):
        prev = self.r.prev
        prev.next, self.r.prev = n,n
        n.prev = prev
        n.next = self.r
        self.length += 1
        return n

            
    


with open('Days of Advent Code\Day 15\input.txt','r') as file:
    fp = file.readline().split(',')
    m = defaultdict(LinkList)
    n = {}
    for line in fp:
        if '=' in line:
            x,y = line.split('=')
            x = x.strip()
            y = int(y.strip())
            s = 0
            for c in x:
                s += ord(c)
                s*=17
                s%=256
            if x not in n:
                n[x] =  m[s].add(Node(y))
            else:
                n[x].val = y
        
        elif '-' in line:
            x,y = line.split('-')
            x = x.strip()
            y = y.strip()
            s = 0
            for c in x:
                s += ord(c)
                s*=17
                s%=256
            cur = m[s].l
            if x in n:
                n[x].pop()
                del n[x]
        
        cur = m[s].l

    ans = 0
    for key in m.keys():
        cur = m[key].l
        x = 0
        lst = []
        while cur:
            if cur.val != 0:
                ans += (key + 1)*x*cur.val
            x += 1
            cur = cur.next
    print(ans)