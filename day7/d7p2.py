def isValid(lhs:int, rhs:list):
    def recurse(index,current):
        if index == len(rhs):
            return lhs == current
        return (
                recurse(index + 1, current + rhs[index]) or
                recurse(index + 1, current * rhs[index]) or 
                recurse(index + 1, int(str(current) + str(rhs[index])))
                )
    return recurse(1,rhs[0])


def run(data:list):
    solution = 0
    for line in data:
        lhs, rhs = line.split(":")
        rhs = list(map(int,rhs.split()))

        # print(f'lhs : {lhs}')
        # print(f'rhs : {rhs}')
        if isValid(int(lhs),rhs):
            solution += int(lhs)

    return solution

if __name__ == "__main__":
    data = open('input.txt').read().strip().split("\n")
    print(run(data))

    # test = ["100: 10 90"]
    # print(run(test))
    # print(isValid(100,[10, 90]))

"""
def recurse(lhs, current, rhs, operator):
    if not rhs and current == lhs:
        return True
    current = operators["*"](current,recurse(rhs))

"""
