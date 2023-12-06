from math import sqrt, floor, ceil

file = open('Days of Advent Code\Day 6\input.txt','r')
t = int("".join(file.readline().split(":")[1].strip().split()))
d = int("".join(file.readline().split(":")[1].strip().split()))

a, b, c = -1, t, -d
def quadratic(a, b, c):
    return [(-b + sqrt((b*b) - 4*a*c)) / (2*a), (-b - sqrt((b*b) - 4*a*c)) / (2*a)]
l, r = quadratic(a, b, c)
print(floor(r) - ceil(l) + 1)
