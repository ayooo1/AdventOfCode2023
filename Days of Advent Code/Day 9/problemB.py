with open('Days of Advent Code\Day 9\input.txt','r') as file:
    ans = 0
    for t,line in enumerate(file.readlines()):
        lst = [int(x) for x in line.split()]
        pre = []
        clone = lst.copy()
        dic = {0: clone[0]}
        x = 1
        while len(set(pre)) != 1:
            pre = []
            for i in range(1,len(lst)):
                pre.append(lst[i]-lst[i-1])
            dic[x] = pre[0]
            lst = pre
            x += 1
        s = 0

        for i in range(len(dic.keys())-1,-1,-1):
            s = dic[i]-s

        ans += s
    print(ans)
