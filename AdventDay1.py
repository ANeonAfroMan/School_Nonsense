FinalSum = 1
currentSum = 0
currentNum = ""
prevVal = "1"
elvesList = [0]
Elves = str(input("input here "))
for x in Elves:
    if x != (" "):
        currentNum = currentNum+x
    elif prevVal == (" "):
        if currentSum > FinalSum:
            FinalSum = currentSum
        elvesList.append(currentSum)
        currentSum = 0
    else:
        y = int(currentNum)
        currentNum = ""
        currentSum += y
        y = 0
    prevVal = x
elvesList.sort(reverse = True)
print(elvesList[0])
print(elvesList[0]+elvesList[1]+elvesList[2])