"""
Sort the list
zip them up and then subtract them
add them up
"""

arr1 = []
arr2 = []

data = open('input.txt', 'r').read().split('\n')

data = data[:-1]
for line in data:
        a,b = tuple(map(int,line.split()))
        arr1.append(a)
        arr2.append(b)

arr1.sort()
arr2.sort()

arr = zip(arr1,arr2)
ans = 0

for a,b in arr:
    ans += abs(a-b)

print(ans)
