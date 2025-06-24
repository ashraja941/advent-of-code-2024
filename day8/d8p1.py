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

            if 0 <= pair[0][0] + xMod < rMax and 0 <= pair[0][1] + yMod <cMax :
                loc1 = (pair[0][0] + xMod,pair[0][1] + yMod)
                antinodes.add(loc1)

            if 0 <= pair[1][0] - xMod < rMax and 0 <= pair[1][1] - yMod <cMax :
                loc2 = (pair[1][0] - xMod,pair[1][1] - yMod)
                antinodes.add(loc2)


    print(nodes)
    return len(antinodes)



if __name__ == "__main__":
    data = open('input.txt').read().strip().split()
    print(run(data))

