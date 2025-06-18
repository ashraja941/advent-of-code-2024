data = open('input.txt', 'r').read().split('\n')
data = data[:-1]

safeCount = 0
for line in data:
    input = list(map(int,line.split()))

    status = 'Fail'

    prev = input[0]
    for i in range(1,len(input)):
        diff = prev - input[i]

        if diff == 0 or (diff < 0 and status == 'Increasing') or (diff > 0 and status == 'Decreasing') or abs(diff) > 3 or abs(diff) < 1:
            status = 'Fail'
            break

        status = 'Increasing' if diff > 0 else 'Decreasing'

        prev = input[i]
    if status != 'Fail':
        safeCount += 1

print(safeCount)
