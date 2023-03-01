from termcolor import colored
import os
answer = str(input(""))
os.system('clear')
guesses = 0
print("Enter your guess.")
while guesses < 6:
  wordinput = str(input(""))
  if len(wordinput)==5:
    guesses += 1
    loop=0
    for x in wordinput:
      loop+=1
      if loop==1: l1=x
      if loop==2: l2=x
      if loop==3: l3=x
      if loop==4: l4=x
      if loop==5: l5=x
    loop=0
    colourvalue1='grey'
    colourvalue2='grey'
    colourvalue3='grey'
    colourvalue4='grey'
    colourvalue5='grey'
    for x in answer:
      loop+=1
      if l1==x and loop!=1: colourvalue1='yellow'
      if l2==x and loop!=2: colourvalue2='yellow'
      if l3==x and loop!=3: colourvalue3='yellow'
      if l4==x and loop!=4: colourvalue4='yellow'
      if l5==x and loop!=5: colourvalue5='yellow'
      if l1==x and loop==1: colourvalue1='green'
      if l2==x and loop==2: colourvalue2='green'
      if l3==x and loop==3: colourvalue3='green'
      if l4==x and loop==4: colourvalue4='green'
      if l5==x and loop==5: colourvalue5='green'
    print(colored(l1,colourvalue1),colored(l2,colourvalue2),colored(l3,colourvalue3),colored(l4,colourvalue4),colored(l5,colourvalue5))
  else:
    print("Your guess must be 5 letters long.")

print("The word was",answer)
