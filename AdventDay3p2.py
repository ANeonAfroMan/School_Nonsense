rucksacks = str(input("Input thingies here: "))
rucksack1 = []
rucksack2 = []
rucksack3 = []
sumTotal = 0
sackNum = 1
letterReference = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for x in rucksacks:
    if x != " " and sackNum == 1:
        rucksack1.append(x)
    elif x != " " and sackNum == 2:
        rucksack2.append(x)
    elif x != " " and sackNum == 3:
        rucksack3.append(x)
    elif sackNum != 3:
        sackNum += 1
    else:
        sackNum = 1
        for a in rucksack1:
            for b in rucksack2:
                for c in rucksack3:
                    if a == b == c: sumTotal+=letterReference.index(a)+1
                    if a == b == c: break
                if a == b == c: break
            if a == b == c: break
        rucksack1.clear()
        rucksack2.clear()
        rucksack3.clear()
print(sumTotal)