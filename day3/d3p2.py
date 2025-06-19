import re

data = open('input.txt', 'r').read().split('\n')
data = data[:-1]

def mul(a,b):
    return int(a)*int(b)

ans = 0
enabled = True
for line in data:
    matches = re.findall(r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)",line)
    print(matches)
    for match in matches:
        if match == 'don\'t()':
            enabled = False
            continue
        if match == 'do()':
            enabled = True
            continue

        if enabled:
            ans += eval(match)

print(ans)
