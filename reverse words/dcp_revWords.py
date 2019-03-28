def reverseWords(inp):
    inp = inp.split()
    revArr = []
    for s in inp:
        rev = list(s)
        rev.reverse()
        revStr = "".join(rev)
        revArr.append(revStr)
    return " ".join(revArr)

def test():
    inpStr = input("Input: ")
    print(reverseWords(inpStr))

test()