def encode(input: str):
    encodedString = []
    for i, value in enumerate(input):
        if not i%2:
            toAdd = [str(i//2) for _ in range(int(value))]
            encodedString.extend(toAdd)
        else:
            toAdd = ["." for _ in range(int(value))]
            encodedString.extend(toAdd)
    return encodedString


def moveElements(input: list):
    i = 0
    while i < len(input):
        print(i)
        if input[i] != ".":
            i += 1
            continue
        while input[-1] == ".":
            input.pop()

        input[i] = input[-1]
        input.pop()
        i += 1
    return input

def calculateCheckSum(input: list):
    checkSum = 0
    for i, value in enumerate(input):
        if value == ".":
            return "Error"
        checkSum += i * int(value)
    return checkSum

if __name__ == "__main__":
    data = open('input.txt').read().strip().split()
    temp_input = "2333133121414131402"

    encoded = encode(data[0])
    converted = moveElements(encoded)

    print(calculateCheckSum(converted))
