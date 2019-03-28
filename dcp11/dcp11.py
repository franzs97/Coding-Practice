def getStrOfSet(s, qSet):
    out = []
    correctChars = 0
    for i in range(len(qSet)):
        for c in range(len(qSet[i])):
            if c < len(s):
                if qSet[i][c] == s[c]:
                    correctChars += 1
            else:
                continue
        if correctChars == len(s):
            out.append(qSet[i])
        correctChars = 0
    if out:
        return out
    else:
        return "no matching strings found"

def test():
    testSet = ['alligator', 'ant', 'baboon', 'bat', 'bear', 'dog', 'deer', 'duck', 'eagle', 'elephant']
    inpt = input("Input: ")
    print("Output:", getStrOfSet(inpt, testSet))

test()
