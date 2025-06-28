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

    area, perimeter = 1,4
    visited.add((r,c))
    
    for di, dj in directions:
        curR, curC = r + di, c + dj
        if not withinBounds(grid,curR,curC):
            continue
        if grid[curR][curC] != curSearch:
            continue
        if (curR,curC) in visited:
            perimeter -= 1
            continue
        a, p = findGroups(grid,curR,curC,curSearch)
        area += a
        perimeter += p - 1

    return area, perimeter



if __name__ == '__main__':
    data = open('input.txt').read().strip().split()
    test = open('test.txt').read().strip().split()

    print(solve(data))
