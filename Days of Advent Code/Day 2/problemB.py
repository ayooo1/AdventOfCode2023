file = open('Day 2\input.txt','r')

ans = 0
for line in file.readlines():
    line.replace(' ','')
    line.strip()
    i,temp = int(line.split(':')[0][4:]), line.split(':')[1]
    roun = temp.split(';')
    f = 0
    r,b,g = 0,0,0
    for se in roun:
        for bee in se.split(', '):
            num,color = bee.strip().split(' ')
            num = int(num)
            if color == 'red':
                r = max(r,num)
            elif color == 'green':
                g = max(g,num)
            elif color == 'blue':
                b = max(b,num)

    ans += (r*b*g)

print(ans)