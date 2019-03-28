def rotateArrBy(arr, k):
    newArr = []
    while(len(arr) < k):
        k -= len(arr)
    for i in range(len(arr)):
        if i+k<len(arr):
            newArr.append(arr[i+k])
        else:
            newArr.append(arr[(i+k)-len(arr)])
    return newArr

def test():
    uinput = list(input("Array: ").split(", "))
    r = int(input("rotate by: "))
    print("Output:",rotateArrBy(uinput, r))

test()