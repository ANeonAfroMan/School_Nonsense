listWords = {}
stringInput = str(input("put it here. "))
for character in stringInput:
  for listCharacter in listWords.values:
    if character == listCharacter:
      listWords[listCharacter] += 1
      break
  else:
    listWords.update(character , 1)
print(listWords)
import random
length = int(input("length of new thing. "))+1
inc = 1
storEE = "Once upon a time... "
while inc < length:
  choose = random.randint(0,sum(listWords.values))
  #print(choose,"R")
  xSum = 0
  for x in listWords.values:
    xSum += x
    #print(xSum,"S")
    if choose <= xSum:
      #print(x,"X")
      print(choose , listWords[x])
      #conL = listWords[listWeights.index(x)]
      #storEE = storEE+conL
      break
  inc += 1
#print(storEE)