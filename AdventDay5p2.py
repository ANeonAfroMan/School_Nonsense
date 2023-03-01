instructions = str(input("Tell me what to do: "))
stack1 = ["B","Z","T"]
stack2 = ["V","H","T","D","N"]
stack3 = ["B","F","M","D"]
stack4 = ["T","J","G","W","V","Q","L"]
stack5 = ["W","D","G","P","V","F","Q","M"]
stack6 = ["V","Z","Q","G","H","F","S"]
stack7 = ["Z","S","N","R","L","T","C","W"]
stack8 = ["Z","H","W","D","J","N","R","M"]
stack9 = ["M","Q","L","F","D","S"]
movingStack = []
allBoxes = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
loopNum = 1
prevNum = ""
for x in instructions:
    if x.isnumeric():
        if prevNum.isnumeric:
            prevNum=prevNum+x
        else:
            prevNum = x
    elif prevNum.isnumeric():
        y = int(prevNum)
        if loopNum == 1: repet = y
        if loopNum == 2: grabFrom = y - 1
        if loopNum == 3:
            counting = 1
            allBoxes[grabFrom].reverse()
            while counting <= repet:
                counting += 1
                movingStack.append(allBoxes[grabFrom][0])
                allBoxes[grabFrom].pop(0)
            counting = 1
            movingStack.reverse()
            while counting <= repet:
                counting += 1
                allBoxes[y - 1].append(movingStack[0])
                movingStack.pop(0)
            allBoxes[grabFrom].reverse()
            loopNum = 0
        prevNum = ""
        y = ""
        loopNum += 1
print(allBoxes)