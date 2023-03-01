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
        totalSum+=1
        if prevChar == "A":
            totalSum+=3
        elif prevChar == "C":
            totalSum+=6
    elif attack == "Y":
        totalSum+=2
        if prevChar == "B":
            totalSum+=3
        elif prevChar == "A":
            totalSum+=6
    elif attack == "Z":
        totalSum+=3
        if prevChar == "C":
            totalSum+=3
        elif prevChar == "B":
            totalSum+=6
print(totalSum)