from collections import Counter

file = open('Day 4\input.txt','r')

ans = 0
c = Counter()
for idx,line in enumerate(file.readlines()):
    c[idx+1] += 1
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
    
    w = len(win & y)

    for i in range(1,w+1):
        c[idx+i+1] += c[idx+1]

print(sum(c.values()))