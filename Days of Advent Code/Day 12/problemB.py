from functools import cache

with open('Days of Advent Code\Day 12\input.txt','r') as file:
    fp = file.readlines()

    def dfs(real,seq):
        @cache
        def dp(i,x,left):
            if i == len(real):
                if x == len(seq) and left == 0:
                    return 1
                return 0
            if x > len(seq):
                return 0

            ans = 0
            if real[i] == '.':
                if left == 0:
                    if x < len(seq):
                        ans += dp(i+1,x+1,seq[x])
                    ans += dp(i+1,x,0)
            
            elif real[i] == '#':
                if left > 0:
                    ans += dp(i+1,x,left - 1)
            
            else:
                if left == 0:
                    if x < len(seq):
                        ans += dp(i+1,x+1,seq[x])
                    ans += dp(i+1,x,0)
                
                if left > 0:
                    ans += dp(i+1,x,left - 1)
            
            return ans
                    
        
        return dp(0,0,0)

    ret = 0

    for line in fp:
        c,seq = line.split()
        seq = [int(x) for x in seq.strip().split(',')]
        mod_c = [c]*5
        c = '.'+'?'.join(mod_c)+'.'
        seq *= 5
        ret += dfs(c,seq)

    print(ret)