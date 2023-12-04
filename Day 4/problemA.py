file = open('Day 4\input.txt','r')

ans = 0
for line in file.readlines():
    _,numbers = line.split(':')[0],line.split(':')[1].rstrip().strip()
    winning,yours = numbers.split('|')[0].strip().split(' '), numbers.split('|')[1].strip().split(' ')
    win = set()
    y = set()
    for x in winning:
        if x != '':
            win.add(x)
    
    for x in yours:
        if x != '':
            y.add(x)

    w = len(set(win) - set(y))
    c = 0
    if w != len(win):
        c = 1
        while len(win)-w>1:
            c*=2
            w+=1
    
    ans += c

print(ans)