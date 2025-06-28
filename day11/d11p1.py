from tqdm import tqdm
def blink(data: list):
    newList = []
    for value in data:
        if value == '0':
            newList.append('1')
        elif not len(value) % 2:
            newList.append(str(int(value[:len(value)//2])))
            newList.append(str(int(value[len(value)//2:])))
        else:
            newList.append(str(2024 * int(value)))

    return newList


if __name__ == '__main__':
    # data = list(map(int,open('input.txt').read().strip().split()))
    data = open('input.txt').read().strip().split()
    print(data)

    test = ['125', '17']
    temp = data

    for i in tqdm(range(75)):
        temp = blink(temp)
        # print(temp)
        print(len(temp))
    
    print(len(temp))
        
