def getArr(nList):
    newArr = []
    for i in range(len(nList)):
        newArr.append(1)
        for k in range(len(nList)):
            if i != k:
                newArr[i] *= nList[k]
    return newArr

def test():
    numList = list(map(int, input("Numbers: ").split(", ")))
    print(getArr(numList))

test()