file = open('Days of Advent Code\Day 6\input.txt','r')
t = int("".join(file.readline().split(":")[1].strip().split()))
d = int("".join(file.readline().split(":")[1].strip().split()))


count = 0
for i in range(t+1):
    if (i*(t-i))>d:
        count += 1

print(count)
