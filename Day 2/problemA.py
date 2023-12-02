file = open('Day 2\input.txt','r')

ans = 0
for line in file.readlines():
    line.replace(' ','')
    line.strip()
    i,temp = int(line.split(':')[0][4:]), line.split(':')[1]
    roun = temp.split(';')
    f = 0
    for se in roun:
        for b in se.split(', '):
            num,color = b.strip().split(' ')
            num = int(num)
            if color == 'red' and num > 12:
                f = 1
            elif color == 'green' and num > 13:
                f = 1
            elif color == 'blue' and num > 14:
                f = 1

    if not f:
        ans += i

print(ans)