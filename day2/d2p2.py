data = open('input.txt', 'r').read().split('\n')
data = data[:-1]

def old(input):
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

def checkSafe(arr):
    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            ascending = False
        if arr[i] < arr[i+1]:
            descending = False
        if abs(arr[i] - arr[i+1]) > 3 or abs(arr[i] - arr[i+1]) < 1:
            return False
    return ascending or descending

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
