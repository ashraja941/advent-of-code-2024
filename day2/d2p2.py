data = open('input.txt', 'r').read().split('\n')
data = data[:-1]

def checkSafe(input):
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
        return True
    return False

def run(data):
    safeCount = 0
    for line in data:
        input = list(map(int,line.split()))

        for removeChar in range(len(input)):
            new_input = input[:removeChar]
            new_input.extend(input[removeChar + 1:])

            if checkSafe(new_input):
                safeCount += 1
                break

    print(safeCount)

run(data)

test = ["1 3 8 5 7 8"]
run(test)

"""
Better time complexity
checkSafe : same old
Consider : check if the result is valid after checking

consider(0) : if this was the problem then ok, if it isn't the problem it doesn't matter
for through the rest of the elements
    if there is a difference of more than 3, then consider deleting either that element or the next one, then break
    if 2 element after exist, chedk for triangle, if it's exists, consider deleting one of the 3 elements, then break
"""
