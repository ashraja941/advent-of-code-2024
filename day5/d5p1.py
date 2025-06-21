from typing import DefaultDict

def findMiddle(update: list):
    return update[len(update)//2]

def fix(update,conditions):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[i] in conditions[update[j]]:
                update[i],update[j] = update[j], update[i]
    return update

def run(data):
    conditions = DefaultDict(list)
    updates = []
    findFix = []
    readConditionsFlag = True
    fixedMiddleSum = 0
    middleSum = 0
    for line in data:
        # print(line)
        if line == "":
            readConditionsFlag = False
            continue

        if readConditionsFlag:
            x,y = list(map(int,line.split("|")))
            conditions[x].append(y)

        else:
            updates.append(list(map(int,line.split(","))))

    for update in updates:
        currUpdate = set()
        validFlag = True
        for item in update:
            for value in conditions[item]:
                if value in currUpdate:
                    validFlag = False
                    break
            if not validFlag:
                findFix.append(update)
                break
            currUpdate.add(item)
        
        if validFlag:
            middleSum += findMiddle(update)

    for update in findFix:
        fixedMiddleSum += findMiddle(fix(update,conditions))
        
    return middleSum, fixedMiddleSum






if __name__ == "__main__":
    data = open('input.txt', 'r').read().split('\n')
    data = data[:-1]

    test = ['10|2',' ','10 245 42']

    print(run(data))

