def getNonDuplicatedIntOf(nList):
    nList.sort()
    for i in range(len(nList)):
        if i % 3 == 0:
            if i+1 < len(nList):
                if(nList[i] != nList[i+1] or nList[i] != nList[i+2]):
                    return nList[i]
            else:
                return nList[i]

def test():
    numList = list(map(int, input("Numbbers: ").split(", ")))
    print("Non-duplicated integer:",getNonDuplicatedIntOf(numList))

test()