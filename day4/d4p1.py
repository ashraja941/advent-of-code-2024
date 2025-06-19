data = open('input.txt', 'r').read().split('\n')
data = data[:-1]

# loop through until you find a 'X', then go through all 8 possibilities. then mark 'X' with '.' then continue
count = 0
rMax = len(data)
cMax = len(data[0])
print("Max : ",rMax,cMax)
for r, row in enumerate(data):
    for c, value in enumerate(row):
        if value != 'X':
            continue
        print("r,c :",r,c)

        if r > 2 :
            add = -1
            if data[r+add][c] == 'M' and data[r+(2*add)][c] == 'A' and data[r+(3*add)][c] == 'S':
                count += 1

        if r < rMax - 3:
            add = 1
            if data[r+add][c] == 'M' and data[r+(2*add)][c] == 'A' and data[r+(3*add)][c] == 'S':
                count += 1

        if c > 2:
            add = -1
            if data[r][c+add] == 'M' and data[r][c+(2*add)] == 'A' and data[r][c+(3*add)] == 'S':
                count += 1

        if c < cMax - 3:
            add = 1
            if data[r][c+add] == 'M' and data[r][c+(2*add)] == 'A' and data[r][c+(3*add)] == 'S':
                count += 1

        if (c > 2 and r > 2):
            add = -1
            if data[r+add][c+add] == 'M' and data[r+(2*add)][c+(2*add)] == 'A' and data[r+(3*add)][c+(3*add)] == 'S':
                count += 1

        if (c < cMax - 3 and r < rMax - 3):
            add = 1
            if data[r+add][c+add] == 'M' and data[r+(2*add)][c+(2*add)] == 'A' and data[r+(3*add)][c+(3*add)] == 'S':
                count += 1

        if (c > 2 and r < rMax - 3):
            add = -1
            if data[r-add][c+add] == 'M' and data[r-(2*add)][c+(2*add)] == 'A' and data[r-(3*add)][c+(3*add)] == 'S':
                count += 1

        if (c < cMax - 3 and r > 2):
            add = 1
            if data[r-add][c+add] == 'M' and data[r-(2*add)][c+(2*add)] == 'A' and data[r-(3*add)][c+(3*add)] == 'S':
                count += 1


print(count)
