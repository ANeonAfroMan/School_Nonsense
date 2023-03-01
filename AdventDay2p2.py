strategyGuide = str(input("strategy here: "))
totalSum = 0
prevChar = ""
for attack in strategyGuide:
    if attack == "A":
        prevChar = "A"
    elif attack == "B":
        prevChar = "B"
    elif attack == "C":
        prevChar = "C"
    elif attack == "X":
        if prevChar == "A":
            totalSum+=3
        elif prevChar == "B":
            totalSum+=1
        elif prevChar == "C":
            totalSum+=2
    elif attack == "Y":
        totalSum+=3
        if prevChar == "A":
            totalSum+=1
        elif prevChar == "B":
            totalSum+=2
        elif prevChar == "C":
            totalSum+=3
    elif attack == "Z":
        totalSum+=6
        if prevChar == "C":
            totalSum+=1
        elif prevChar == "B":
            totalSum+=3
        elif prevChar == "A":
            totalSum+=2
print(totalSum)