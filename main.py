listWords = []
listWeights = []
stringInput = str(input("put it here. "))
for character in stringInput:
  for listCharacter in listWords:
    if character == listCharacter:
      listWeights[listWords.index(listCharacter)]+=1
      break
  else:
    listWords.append(character)
    listWeights.append(1)
import random
length = int(input("length of new thing. "))
inc = 1
xSum = 0
storEE = "Once upon a time... "
while inc < length:
  choose = random.randint(0,sum(listWeights))
  for x in listWeights:
    xSum += x
    if choose <= xSum:
      conL = listWords[listWeights.index(x)]
      storEE = storEE+conL
      break
print(storEE)