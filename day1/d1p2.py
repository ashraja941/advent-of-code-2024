
"""


"""
from collections import Counter

arr1 = []
arr2 = []

data = open('input.txt', 'r').read().split('\n')

data = data[:-1]
for line in data:
        a,b = tuple(map(int,line.split()))
        arr1.append(a)
        arr2.append(b)

count = Counter(arr2)

ans = 0
for element in arr1:
    ans += element * count.get(element,0)

print(ans)
