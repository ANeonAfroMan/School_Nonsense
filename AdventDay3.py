rucksacks = str(input("Input thingies here: "))
rucksack = []
sumTotal = 0
letterReference = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for x in rucksacks:
    if x != " ":
        rucksack.append(x)
    else:
        for y in rucksack[:int(len(rucksack)/2)]:
            for z in rucksack[int(len(rucksack)/2):]:
                if y == z: sumTotal+=letterReference.index(y)+1
                if y == z: break
            if y == z: break
        rucksack.clear()
print(sumTotal)