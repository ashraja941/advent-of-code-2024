"""
brute force, that shi for all places that the guard has been. keep track of direction as well
"""

from tqdm import tqdm

with open("input.txt") as fin:
    data = [list(line) for line in fin.read().strip().split("\n")]

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

initPos = currPos.copy()

while True:
    seen.add(tuple(currPos))
    nextPos = [currPos[0]+directions[currDir][0], currPos[1]+directions[currDir][1]]
    if nextPos[0] < 0 or nextPos[0] >= rMax or nextPos[1] >= cMax or nextPos[1] < 0:
        break
    if data[nextPos[0]][nextPos[1]] == '#':
        currDir = (currDir + 1) % 4
    else:
        currPos = nextPos

def willLoop(oi:int,oj:int):
    if data[oi][oj] == '#':
        return False

    data[oi][oj] = '#'
    pos = initPos

    dir = 0
    visited = set()

    while True:
        if (pos[0],pos[1],dir) in visited:
            data[oi][oj] = '.'
            return True

        visited.add((pos[0],pos[1],dir))

        nextPos = [pos[0]+directions[dir][0], pos[1]+directions[dir][1]]

        if nextPos[0] < 0 or nextPos[0] >= rMax or nextPos[1] >= cMax or nextPos[1] < 0:
            data[oi][oj] = '.'
            return False
        if data[nextPos[0]][nextPos[1]] == '#':
            dir = (dir + 1) % 4
        else:
            pos = nextPos

ans = 0
for i,j in seen:
    print(f"i : {i}, j : {j}")
    if i == initPos[0] and j == initPos[1]:
        continue
    loop = willLoop(int(i),int(j))
    ans += int(loop)

print(ans)
