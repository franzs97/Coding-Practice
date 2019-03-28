import math

def medianOf(nList):
    nList.sort()
    if len(nList) % 2 == 1:
        return nList[int(len(nList) / 2)]
    elif len(nList) % 2 == 0:
        medDown = nList[math.floor(len(nList) / 2)-1]
        medUp = nList[math.floor(len(nList) / 2)]
        avr = (medDown + medUp) /2
        if avr - int(avr) != 0:
            return avr
        else:
            return int(avr)

def getMedList(arr):
    medList = []
    for i in range(len(arr)):
        if i != 0:
            medList.append(medianOf(arr[0:i+1]))
        else:
            medList.append(arr[i])
    return medList

def test():
    numList = list(map(int, input("Numbers: ").split(", ")))
    print(getMedList(numList))

test()