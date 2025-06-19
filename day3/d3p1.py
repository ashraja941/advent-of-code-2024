import re

data = open('input.txt', 'r').read().split('\n')
data = data[:-1]

def mul(a,b):
    return int(a)*int(b)

ans = 0
for line in data:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)",line)
    print(matches)
    for match in matches:
        print(match)
        ans += eval(match)

print(ans)
