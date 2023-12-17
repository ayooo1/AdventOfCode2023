with open('Days of Advent Code\Day 18\input.txt','r') as file:
    fp = [x.strip() for x in file.readlines()]
    temp = fp
    fp = []
    
    for i in range(len(temp)):
        lst = []
        for j in range(len(temp[0])):
            lst.append(int(temp[i][j]))
        fp.append(lst)