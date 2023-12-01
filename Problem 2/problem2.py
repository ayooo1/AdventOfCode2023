file = open('Problem 2\input.txt','r')
ans = 0
num = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}


def checknum(s):
    n = len(s)
    x = ''

    for i in range(n):
        if s[i].isdigit():
            x += s[i]
            break
        elif i >= 2 and s[i-2:i+1] in num:
            x += num[s[i-2:i+1]]
            break
        elif i >= 3 and s[i-3:i+1] in num:
            x += num[s[i-3:i+1]]
            break
        elif i >= 4 and s[i-4:i+1] in num:
            x += num[s[i-4:i+1]]
            break
    
    for i in range(n-1,-1,-1):
        if s[i].isdigit():
            x += s[i]
            break
        elif i >= 2 and s[i-2:i+1] in num:
            x += num[s[i-2:i+1]]
            break
        elif i >= 3 and s[i-3:i+1] in num:
            x += num[s[i-3:i+1]]
            break
        elif i >= 4 and s[i-4:i+1] in num:
            x += num[s[i-4:i+1]]
            break
    
    return int(x)


for s in file.readlines():
    ans += checknum(s.strip())

print(ans)