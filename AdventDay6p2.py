readingList = ["@","!","?","}",":",",","%","$","&","'",">","<","/","]"]
input = str(input("Input: "))
packetPos = 0
for x in input:
    readingList.pop(0)
    readingList.append(x)
    packetPos+=1
    for y in range(0,13):
        if y == 13: break
        for z in range(0,13-y):
            if z+y+1 > 14: break
            if readingList[y] == readingList[z+y+1] and packetPos >= 14 and y != z: break
        if readingList[y] == readingList[z+y+1] and packetPos >= 14 and y != z: break
    if y == 13: break
print(packetPos)