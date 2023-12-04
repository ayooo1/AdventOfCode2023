file = open('Day 4\input.txt','r')

ans = 0
for line in file.readlines():
    _,numbers = line.split(':')[0],line.split(':')[1].rstrip().strip()
    winning,yours = set(numbers.split('|')[0].strip().split()), set(numbers.split('|')[1].strip().split())
    w = len(winning & yours)
    c = 0
    if w:
        c = 2**(w-1)
        
    
    ans += c

print(ans)