import itertools as it

InputList = []
with open("Days of Advent Code\Day 24\input.txt", "r") as data:
    for t in data:
        P, V = t.strip().split(" @ ")
        PX, PY, PZ = list(map(int, P.split(", ")))
        VX, VY, VZ = list(map(int, V.split(", ")))
        NewTuple = (PX, PY, PZ, VX, VY, VZ)
        InputList.append(NewTuple)

PotentialXSet = None
PotentialYSet = None
PotentialZSet = None
for A, B in it.combinations(InputList, 2):
    APX, APY, APZ, AVX, AVY, AVZ = A
    BPX, BPY, BPZ, BVX, BVY, BVZ = B

    if AVX == BVX and abs(AVX) > 100:
        NewXSet = set()
        Difference = BPX - APX
        for v in range(-1000, 1000):
            if v == AVX:
                continue
            if Difference % (v-AVX) == 0:
                NewXSet.add(v)
        if PotentialXSet != None:
            PotentialXSet = PotentialXSet & NewXSet
        else:
            PotentialXSet = NewXSet.copy()
    if AVY == BVY and abs(AVY) > 100:
        NewYSet = set()
        Difference = BPY - APY
        for v in range(-1000, 1000):
            if v == AVY:
                continue
            if Difference % (v-AVY) == 0:
                NewYSet.add(v)
        if PotentialYSet != None:
            PotentialYSet = PotentialYSet & NewYSet
        else:
            PotentialYSet = NewYSet.copy()
    if AVZ == BVZ and abs(AVZ) > 100:
        NewZSet = set()
        Difference = BPZ - APZ
        for v in range(-1000, 1000):
            if v == AVZ:
                continue
            if Difference % (v-AVZ) == 0:
                NewZSet.add(v)
        if PotentialZSet != None:
            PotentialZSet = PotentialZSet & NewZSet
        else:
            PotentialZSet = NewZSet.copy()

RVX, RVY, RVZ = PotentialXSet.pop(), PotentialYSet.pop(), PotentialZSet.pop()

APX, APY, APZ, AVX, AVY, AVZ = InputList[0]
BPX, BPY, BPZ, BVX, BVY, BVZ = InputList[1]
MA = (AVY-RVY)/(AVX-RVX)
MB = (BVY-RVY)/(BVX-RVX)
CA = APY - (MA*APX)
CB = BPY - (MB*BPX)
XPos = int((CB-CA)/(MA-MB))
YPos = int(MA*XPos + CA)
Time = (XPos - APX)//(AVX-RVX)
ZPos = APZ + (AVZ - RVZ)*Time

Part2Answer = XPos + YPos + ZPos

print(f"{Part2Answer = }")