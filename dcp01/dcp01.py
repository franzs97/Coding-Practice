def anyTwoNumbers(nList, k):
    for i in range(len(nList)):
        a = k -nList[i]
        if a in nList:
            return True
    return False

def test():
    numList = list(map(int,input("Input: ").split(", ")))
    ik = int(input("k: "))
    print(anyTwoNumbers(numList, ik))

test()
