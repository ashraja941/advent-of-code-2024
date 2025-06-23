data = open('input.txt').read().split("\n")
data = data[:-1]

rMax = len(data)
cMax = len(data[0])

directions = [(-1,0),(0,1),(1,0),(0,-1)]
currDir = 0
currPos = [0,0]
seen = set()

for r,row in enumerate(data):
    for c, value in enumerate(row):
        if value in ['v','^','<','>']:
            currPos = [r,c]
            print(f'found player at {r},{c} : {value}')

while True:
    seen.add(tuple(currPos))
    nextPos = [currPos[0]+directions[currDir][0], currPos[1]+directions[currDir][1]]
    if nextPos[0] < 0 or nextPos[0] >= rMax or nextPos[1] >= cMax or nextPos[1] < 0:
        break
    if data[nextPos[0]][nextPos[1]] == '#':
        currDir = (currDir + 1) % 4
    else:
        currPos = nextPos

print(len(seen))
