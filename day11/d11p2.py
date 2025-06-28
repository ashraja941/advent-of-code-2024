from typing import DefaultDict
from collections import Counter, defaultdict
from tqdm import tqdm
from functools import cache
import math

def checkEven(n):
    if n == 0:
        return False
    digit = int(math.log10(n)) 
    return digit % 2

def split(n):
    digit = int(math.log10(n)) + 1
    divisor = 10 ** (digit//2)
    return n // divisor, n %divisor

# def memory(data) -> dict:
#     res = DefaultDict(int)
#     for value in data:
#         res[value] += 1
#     return res

@cache
def changeStone(value: int):
    if value == 0:
        return [1]
    elif checkEven(value):
        a,b = split(value)
        return [a,b]
    else:
        return [2024 * value]

def blink(data: dict):
    newList = defaultdict(int)
    for key,value in data.items():
        for i in changeStone(key):
            newList[i] += 1*value

    return newList

if __name__ == '__main__':
    data = list(map(int,open('input.txt').read().strip().split()))
    # data = open('input.txt').read().strip().split()
    # print(data)

    test = [ 125 ,  17 ]

    dataDict = Counter(data)
    print(dataDict)

    for i in tqdm(range(75)):
        dataDict = blink(dataDict)
        print(dataDict)
        # print(len(dataDict))

    print(sum(list(dataDict.values())))
        
