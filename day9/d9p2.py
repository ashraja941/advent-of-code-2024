from tqdm import tqdm

def encode(input: str):
    loc = [0] * len(input)
    size = [0] * len(input)
    encodedString = []
    for i, value in enumerate(input):
        if not i%2:
            loc[i//2] = len(encodedString)
            size[i//2] = int(value)
            toAdd = [i//2 for _ in range(int(value))]
            encodedString.extend(toAdd)
        else:
            # toAdd = [None for _ in range(int(value))]
            toAdd = [None] * int(value)
            encodedString.extend(toAdd)
    return encodedString, loc, size


def moveElements(input: list, loc: list, size: list):
    big = 0
    while size[big] > 0:
        big += 1
    big -= 1
    
    for toMove in tqdm(range(big,-1,-1)):
        freeSpace = 0
        firstFree = 0

        while firstFree < loc[toMove] and freeSpace < size[toMove]:
            firstFree = firstFree + freeSpace
            freeSpace = 0
            while input[firstFree] != None:
                firstFree += 1
            while firstFree + freeSpace < len(input) and input[firstFree + freeSpace] == None:
                freeSpace += 1
            
        if firstFree >= loc[toMove]:
            continue
        
        # Move file by swapping block values
        for idx in range(firstFree, firstFree + size[toMove]):
            input[idx] = toMove
        for idx in range(loc[toMove], loc[toMove] + size[toMove]):
            input[idx] = None

    return input


def calculateCheckSum(input: list):
    checkSum = 0
    for i, value in enumerate(input):
        if value == None:
            continue
        checkSum += i * int(value)
    return checkSum

if __name__ == "__main__":
    data = open('input.txt').read().strip().split()
    temp_input = "2333133121414131402"

    encoded, loc, size = encode(data[0])
    # encoded, loc, size = encode(temp_input)
    print(encoded)
    converted = moveElements(encoded,loc,size)

    print(calculateCheckSum(converted))
