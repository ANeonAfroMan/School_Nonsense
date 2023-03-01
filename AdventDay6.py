readingList = ["@","!","?","}"]
input = str(input("Input: "))
packetPos = 0
for x in input:
    readingList.pop(0)
    readingList.append(x)
    packetPos+=1
    print(readingList)
    if not(readingList[0] == readingList[1] or readingList[0] == readingList[2] or readingList[0] == readingList[3] or readingList[1] == readingList[2] or readingList[1] == readingList[3] or readingList[2] == readingList[3]) and packetPos >= 4:
        break
print(packetPos)