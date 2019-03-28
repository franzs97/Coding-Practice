def findLowestMissingInt(arr):
    arr.sort()
    missingInt = 1
    for i in range(len(arr)):
        if arr[i] == missingInt:
            missingInt += 1
    return missingInt

def test():
    numList = list(map(int,input("Input: ").split(", ")))
    print("First missing positiv integer is:",findLowestMissingInt(numList))

test()