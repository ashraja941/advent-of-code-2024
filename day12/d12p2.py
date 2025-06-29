directions = [(1,0),(-1,0),(0,1),(0,-1)]
visited = set()

def withinBounds(grid,r,c):
    n = len(grid)
    m = len(grid[0])

    return ( 0 <= r < n ) and ( 0 <= c < m )

def solve(grid):
    global visited
    ans = 0

    rMax = len(grid)
    cMax = len(grid[0])

    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if (r,c) in visited:
                continue

            a, p = findGroups(grid,r,c,value)
            print(f"area of group {value} is {a} with perimeter {p}")
            ans += a*p

    return ans


def findGroups(grid,r,c,curSearch):
    global visited

    area, perimeter = 1,0
    visited.add((r,c))
    
    for di, dj in directions:
        curR, curC = r + di, c + dj
        if not withinBounds(grid,curR,curC):
            continue
        if grid[curR][curC] != curSearch:
            continue
        if (curR,curC) in visited:
            continue
        a, p = findGroups(grid,curR,curC,curSearch)
        area += a
        perimeter += p 

    perimeter += countCorners(findCorners(grid,r,c,curSearch))

    return area, perimeter

def findCorners(grid,r,c,currSearch):
    temp = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            curR, curC = r + i, c + j
            if not withinBounds(grid,curR,curC):
                temp.append(0)
            elif grid[curR][curC] != currSearch:
                temp.append(0)
            else:
                temp.append(1)

    if len(temp) != 8:
        raise RuntimeError

    return temp

def countCorners(temp):
    c = 0
    if temp[0] == 0 and temp[1] == 1 and temp[3] == 1:
        c += 1
    if temp[2] == 0 and temp[1] == 1 and temp[4] == 1:
        c += 1
    if temp[5] == 0 and temp[6] == 1 and temp[3] == 1:
        c += 1
    if temp[7] == 0 and temp[6] == 1 and temp[4] == 1:
        c += 1

    if temp[1] == 0 and temp[3] == 0:
        c += 1
    if temp[6] == 0 and temp[3] == 0:
        c += 1
    if temp[1] == 0 and temp[4] == 0:
        c += 1
    if temp[6] == 0 and temp[4] == 0:
        c += 1

    return c


if __name__ == '__main__':
    data = open('input.txt').read().strip().split()
    test = open('test.txt').read().strip().split()

    print(solve(data))
