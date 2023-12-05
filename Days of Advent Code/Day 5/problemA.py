file = open('Day 5\input.txt','r')
seed = file.readline()
seed_num, seed_map, soil_map,fertilizer_map,water_map,light_map,temp_map,hum_map = [],{},{},{},{},{},{},{}

for i in seed.split(':')[1].split():
    seed_num.append(i)

fp = file.readlines()

def seed_m(x):
    while len(fp[x].split()) != 0:
        i,j,k = [int(c) for c in fp[x].split()]
        seed_map[(j,j+k-1)] = i-j
        x += 1

def soil_m(x):
    while len(fp[x].split()) != 0:
        i,j,k = [int(c) for c in fp[x].split()]
        soil_map[(j,j+k-1)] = i-j
        x += 1

def fertilizer_m(x):
    while len(fp[x].split()) != 0:
        i,j,k = [int(c) for c in fp[x].split()]
        fertilizer_map[(j,j+k-1)] = i-j
        x += 1

def water_m(x):
    while len(fp[x].split()) != 0:
        i,j,k = [int(c) for c in fp[x].split()]
        water_map[(j,j+k-1)] = i-j
        x += 1

def light_m(x):
    while len(fp[x].split()) != 0:
        i,j,k = [int(c) for c in fp[x].split()]
        light_map[(j,j+k-1)] = i-j
        x += 1

def temp_m(x):
    while len(fp[x].split()) != 0:
        i,j,k = [int(c) for c in fp[x].split()]
        temp_map[(j,j+k-1)] = i-j
        x += 1

def hum_m(x):
    while x < len(fp) and len(fp[x].split()) != 0:
        i,j,k = [int(c) for c in fp[x].split()]
        hum_map[(j,j+k-1)] = i-j
        x += 1



for idx,i in enumerate(fp):
    if 'seed-to-soil' in i:
        seed_m(idx+1)
    elif 'soil-to-fertilizer map' in i:
        soil_m(idx+1)
    elif 'fertilizer-to-water map' in i:
        fertilizer_m(idx+1)
    elif 'water-to-light map' in i:
        water_m(idx+1)
    elif 'light-to-temperature map' in i:
        light_m(idx+1)
    elif 'temperature-to-humidity map' in i:
        temp_m(idx+1)
    elif 'humidity-to-location map' in i:
        hum_m(idx+1)

ans = float('inf')
for s in seed_num:
    soil = -1
    for start,end, in seed_map:
        if start <= int(s) <= end:
            soil = seed_map[(start,end)] + int(s)
            break
    if soil == -1:
        soil = int(s)

    fert = -1
    for start,end in soil_map:
        if start <= soil <= end:
            fert = soil_map[(start,end)] + soil
            break
    if fert == -1:
        fert = soil
    
    water = -1
    for start,end in fertilizer_map:
        if start <= fert <= end:
            water = fertilizer_map[(start,end)] + fert
            break
    if water == -1:
        water = fert
    
    light = -1
    for start,end in water_map:
        if start <= water <= end:
            light = water_map[(start,end)] + water
            break
    if light == -1:
        light = water
    
    temp = -1
    for start,end in light_map:
        if start <= light <= end:
            temp = light_map[(start,end)] + light
            break
    if temp == -1:
        temp = light
    
    hum = -1
    for start,end in temp_map:
        if start <= temp <= end:
            hum = temp_map[(start,end)] + temp
            break
    if hum == -1:
        hum = temp
    
    loc = -1
    for start,end in hum_map:
        if start <= hum <= end:
            loc = hum_map[(start,end)] + hum
            break
    if loc == -1:
        loc = hum

    ans = min(ans,loc)
print(ans)