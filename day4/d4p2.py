data = open('input.txt', 'r').read().split('\n')
data = data[:-1]

# loop through until you find a 'M', find all 4 possibilities, then replace 'M' with '.'.

count = 0
rMax = len(data)
cMax = len(data[0])
print("Max : ",rMax,cMax)
for r, row in enumerate(data):
    for c, value in enumerate(row):
        if value != 'M':
            continue

        # top right
        if c < cMax - 2 and r > 1:
            if data[r-2][c] == 'S' and data[r-2][c+2] == 'S' and data[r-1][c+1] == 'A' and data[r][c+2] == 'M':
                count += 1

        # bottom right
        if c < cMax - 2 and r < rMax - 2:
            if data[r+2][c] == 'M' and data[r+2][c+2] == 'S' and data[r+1][c+1] == 'A' and data[r][c+2] == 'S':
                count += 1

        # top left
        if c > 1 and r > 1:
            if data[r-2][c] == 'M' and data[r-2][c-2] == 'S' and data[r-1][c-1] == 'A' and data[r][c-2] == 'S':
                count += 1

        # bottom left
        if c > 1 and r < rMax - 2:
            if data[r+2][c] == 'S' and data[r+2][c-2] == 'S' and data[r+1][c-1] == 'A' and data[r][c-2] == 'M':
                count += 1

print(count)


