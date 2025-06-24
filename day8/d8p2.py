from collections import defaultdict
from itertools import combinations
from os import rmdir


def run(data):
    antinodes = set()
    nodes = defaultdict(list)
    rMax = len(data)
    cMax = len(data[0])

    for r, row in enumerate(data):
        for c, value in enumerate(row):
            if value == '.':
                continue
            nodes[value].append((r,c))


    for node, locs in nodes.items():
        pairs = list(combinations(locs,2))
        for pair in pairs:
            xMod = pair[0][0] - pair[1][0]
            yMod = pair[0][1] - pair[1][1]

            loc1 = (pair[0][0] ,pair[0][1] )
            loc2 = (pair[1][0] ,pair[1][1] )
            
            while 0 <= loc1[0] < rMax and 0 <= loc1[1] < cMax :
                antinodes.add(loc1)
                loc1 = (loc1[0] + xMod, loc1[1] + yMod)

            while 0 <= loc2[0] < rMax and 0 <= loc2[1] < cMax :
                antinodes.add(loc2)
                loc2 = (loc2[0] - xMod,loc2[1] - yMod)


    print(nodes)
    return len(antinodes)



if __name__ == "__main__":
    data = open('input.txt').read().strip().split()
    print(run(data))
    
