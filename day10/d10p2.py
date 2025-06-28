
with open("./input.txt") as fin:
    grid = fin.read().strip().split("\n")

cMax = len(grid)
rMax = len(grid[0])

n = len(grid)

directions = [(-1,0),(1,0),(0,1),(0,-1)]

def inGrid(i,j):
    return 0 <= i < n and 0 <= j < n

def score(i,j):
    if grid[i][j] != '0':
        return 0

    currentAns = 0

    stack = [(i,j)]
    visited = set()
    while stack:
        curI, curJ = stack.pop()
        visited.add((curI,curJ))
        cur = int(grid[curI][curJ])

        if cur == 9:
            currentAns += 1
            continue

        for di, dj in directions:
            nextI, nextJ = curI + di, curJ + dj
            if (nextI,nextJ) in visited:
                continue

            if not inGrid(nextI,nextJ):
                continue

            next = int(grid[nextI][nextJ])
            if next != cur + 1:
                continue
            stack.append((nextI,nextJ))

    return currentAns

def score_recursive(i,j):
    currentAns = 0
    if int(grid[i][j]) == 9:
        # print("found 9 at ",i,j)
        return  1

    for di, dj in directions:
        nextI, nextJ = i + di, j + dj
        if not inGrid(nextI,nextJ):
            continue

        next = int(grid[nextI][nextJ])
        if next != int(grid[i][j]) + 1:
            continue
        # print("next ",nextI,nextJ)
        currentAns += score_recursive(nextI,nextJ)

    return currentAns




ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if int(grid[i][j]) == 0:
            ans += score_recursive(i,j)
print(ans)

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if int(grid[i][j]) == 0:
            ans += score(i,j)
print(ans)
