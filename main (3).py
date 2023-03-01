def start():
  global a
  a = str("no")
  print(""" Type what you would like to access. Sum, Calculator, C to F, 0 comparison, 
sum-product comparison, cube, number swap, fibbonacci sequence, equal comparison, 
even or odd, positive or negative, leap year, guesser, websurf, abs, ifcontains, 
divisibility, text_based_adventure, guesserer, orderchecker, usernamepassword, tututu, and madlib are your options.""")
  a = str(input(""))
  if a == "calculator":
    print("Welcome to calculator.")
    n1 = float(input("enter your first number "))
    n2 = float(input("enter your second number "))
    if n2 == 0: print("Your answer cannot be 0")
    if n2 == 0: start()
    print(n1 , "multiplied by" , n2 , "=" , n1*n2)
    print(n1 , "plus" , n2 , "=" , n1+n2)
    print(n1 , "divided by" , n2 , "=" , n1/n2)
    print(n1 , "subtract" , n2 , "=" , n1-n2)
    print(n1 , "to the power of" , n2 , "=" , n1**n2)
    print("There are your answers.")
    start()
  elif a == "C to F":
    print("Welcome to Celcius to Farenheight.")
    n1 = float(input("Enter you temperature in celcius."))
    n2 = n1
    n2 *= 1.8
    n2 += 32
    print(n1, "C =", n2 ,"F")
    start()
  elif a == "0 comparison":
    print("Welcome to 0 comparison.")
    n1 = float(input("Enter the number you would like to compare with 0."))
    print("Your answer is greater than 0") if n1 > 0 else print("Your number is not greater than 0")
    start()
  elif a == "sum-product comparison":
    print("Welcome to the sum-product comparison")
    n1 = float(input("Enter your first number."))
    n2 = float(input("Enter your second number."))
    n3=n1*n2
    n4=n1+n2
    print(n3==n4)
    start()
  elif a == "cube":
    print("Welcome to cube.")
    n1 = float(input("Enter the number you would like cubed."))
    n1 **= 3
    print(n1)
    start()
  elif a == "number swap":
    print("Welcome to number swap.")
    n1 = str(input("Enter your first number."))
    n2 = str(input("Enter your second number."))
    print("You entered",n1,"for numberOne")
    print("You entered",n2,"for nuberTwo")
    n3 = n1
    n1 = n2
    n2 = n3
    print("Your numbers have been swapped.")
    print("numberOne now has", n1)
    print ("numberTwo now has", n2)
    start()
  elif a == "sum":
    print("Welcome to sum.")
    n1 = float(input("Input your fisrt number."))
    n2 = float(input("Input your second number."))
    print("The sum of",n1,"and",n2,"=",n1+n2)
    start()
  elif a == "madlib":
    name = str(input("Enter your name please. "))
    if name=="Joel": print("Huh, that's my name.")
    print("Welcome", name,". You will be asked for a series of words.")
    print("They will then be put into a paragraph and possibly not make sense. Good   Luck.")
    adj = str(input("Please input an adjective "))
    foods = str(input("Please input a food (plural) "))
    ver = str(input("Please input a verb "))
    say = str(input("Please input a something something would say "))
    noun = str(input("Please input a noun "))
    foods2 = str(input("Please input a food (plural) "))
    colour = str(input("Please input a colour "))
    ride = str(input("Please input something you would ride in "))
    anml = str(input("Please input an animal "))
    person = str(input("Finally, please input a person "))
    print("Today",name,"went to my favourite Taco stand called the",adj,anml,". Unlike most food stands, they cook and prepare the food the food in a",ride,"while you",ver,". The best thing on the menu is the",colour,noun,". Instead of ground beef they fill the taco with",foods2,", cheese, and top it all off with a salsa made from",foods,". If that doesn't make your mouth water, then it's just like",person,"always says:",say,"!")
    start()
  elif a == "fibbonacci":
    n1 = int(input("How many numbers would you like to see of the sequence? "))
    print("Here is the fibbonacci sequence.")
    loop = 1
    x = int(1)
    y = int(1)
    while loop <= n1:
      loop += 1
      print(x)
      loop += 1
      print(y)
      x = x+y
      y = x+y
      start()
  elif a == "equal comparison":
    print("Welcome to equal comparison.")
    n1 = int(input("Enter your first number. "))
    n2 = int(input("Enter your second number. "))
    print("Your two numbers are equal.") if n1==n2 else print("Your two numbers are not equal.")
  elif a == "even or odd":
    print("Welcome to even or odd.")
    n1 = int(input("Enter your number. "))
    print("your number is even") if n1%2==0 else print("Your number is odd.")
    start()
  elif a == "positive or negative":
    print("Welcome to positive or negative.")
    n1 = int(input("Input your number. "))
    if n1==0:
      print("Your number is 0.")
    elif n1>0:
      print("Your number is positive.")
    else:
      print("Your number is negative.")
    start()
  elif a == "leap year":
    print("Welcome to leap year.")
    n1 = int(input("Enter the year you would like to know about. "))
    print(n1,"is a leap year.") if n1%4==0 else print(n1,"is not a leap year.")
    start()
  elif a == "guesser":
    import random
    print("Welcome to guesser. Please input the range of the numbers you want to guess between.")
    n1 = int(input("Lower end of your range. "))
    n2 = int(input("Higher end of your range. "))
    global rn
    rn = (random.randint(n1, n2))
    def guess():
      n4 = int(input("Guess a number. "))
      if n4==rn:
        print("Good Job! That's correct!")
        start()
      elif n4>rn:
        print("Your guess is too high.")
        guess()
      else:
        print("Your guess is too low.")
        guess()
    guess()
  elif a == "websurf":
    print("Welcome to Surf the Web.")
    print("The web is in low tide right now, please come back later.")
    start()
  elif a == "abs":
    print("Welcome to absolute Value.")
    n1 = int(input("Please input your number. "))
    print("The absolute value of",n1,"is",abs(n1))
    start()
  elif a == "ifcontains":
    print("Welcome to the containing checker.")
    n1 = str(input("Please input the word or phrase or number you will be checking for. "))
    print("Please input the word or phrase you will check if it has",n1)
    n2 = str(input(""))
    print(n2,"has",n1)if n1 in n2 else print(n2,"does not have",n1)
    start()
  elif a == "divisibility":
    print("Welcome to divisibility.")
    n1 = int(input("Please input your number you want to check for divisibility. "))
    print("Please input your number you want to check if it is divisible by",n1)
    n2 = int(input(""))
    print(n2,"is divisible by",n1)if (n2%n1==0) else print(n2,"is not divisible by",n1)
  elif a == "text_based_adventure":
    print("Text based adventure is not available right now, once it is complete this will work.")
    start()
  elif a == "orderchecker":
    print("Welcome to orderchecker.")
    numbList = [0,0,0]
    numbList[1] = int(input("Input your first number. "))
    numbList[2] = int(input("Input your second number. "))
    numbList[3] = int(input("Input your third number."))
    print("Your numbers are in order.")if numbList[1]<numbList[2]<numbList[3] else print("Your numbers are not in order.")
  elif a == "guesserer":
    import random
    level = 1
    fourHighscore=[10]
    fiveHighscore=[25]
    sixHighscore=[50]
    fourHighscoreDict={
      10 : "Generic Name",
    }
    fiveHighscoreDict={
      25 : "Normal Person",
    }
    sixHighscoreDict={
      50 : "Pre-Programmed Person",
    }
    hubCheck = 0
    print("Welcome to the Guessing game. Complete the first 3 levels to unlock everything.")
    def guesser():
      global level
      global hubCheck
      global highscores
      levelData=[0,0,0,0]
      if level==4 or hubCheck==1:
        highFour = fourHighscoreDict.get(fourHighscore[0])
        highFive = fiveHighscoreDict.get(fiveHighscore[0])
        highSix = sixHighscoreDict.get(sixHighscore[0])
        hubCheck = 1
        print("""Welcome to the hub. Since you have beaten the first 3 levels, you may now choose what level 
    to go to. 1-3 have a limited number of guesses, while 4-6 are highscore oriented.
    1. Random from 1 to 25, 5 guesses total.
    2. Random from 50 to 200, 8 guesses total.
    3. Random from 100 to 1000, 15 guesses total.
    4. Random from 1 to 100, highscore is""",fourHighscore[0],"""by""",highFour,"""
    5. Random from 1 to 1000, highscore is""",fiveHighscore[0],"""by""",highFive,"""
    6. Random from 1 to 10000, highscore is""",sixHighscore[0],"""by""",highSix,"""
    7. Custom level - Input your own range and guess limit.
      Input a number from 1 - 7.""")
        level = int(input(""))
      if level==7:
        print("Welcome to the custom level generator.")
        print("What do you want the lower end of your range to be?")
        randRangeBottom = int(input(""))
        levelData[0] = randRangeBottom
        print("What do you want the higher end of your range to be?")
        randRangeTop = int(input(""))
        levelData[1] = randRangeTop
        print("How many guesses do you want?")
        guesses = int(input(""))
        levelData[2] = guesses
        levelData[3] = 1
      elif level==1:
        levelData=[1,25,5,1]
      elif level==2:
        levelData=[50,200,8,1]
      elif level==3:
        levelData=[100,1000,15,1]
      elif level==4:
        levelData=[1,100,0,-1]
      elif level==5:
        levelData[1,1000,0,-1]
      elif level==6:
        levelData=[1,10000,0,-1]
      else:
        print("That is not a valid level. Please try again.")
        guesser()
      randomNumber = (random.randint(levelData[0], levelData[1]))
      print("Welcome to level",level,". Please input a guess from",levelData[0],"to",levelData[1],"You have",levelData[2],"guesses total.") if levelData[3]==1 else print("Welcome to level",level,". Please input a guess from",levelData[0],"to",levelData[1],"You have guessed",levelData[2],"times total.")
      while levelData[2] >= 0:
        levelData[2] -= levelData[3]
        numberOne = int(input(""))
        if numberOne>levelData[1] or numberOne<levelData[0]:
          print("Your number is out of the range. Please input another number.")
          levelData[2] += levelData[3]
        else:
          if numberOne==randomNumber:
            if levelData[3] == 1:
              print("Good Job! That's correct! You had",levelData[2],"guesses left.")
              level += 1
              guesser()
            else:
              print("Good Job. That took you",levelData[2],"guesses. Please input your name.")
              name = str(input(""))
              if level==4:
                fourHighscore.append(levelData[2])
                fourHighscore.sort()
                fourHighscoreDict.update({levelData[2]:name})
                print("Here are the highscores.")
                for l in fourHighscore:
                  m = fourHighscoreDict.get(l)
                  print(m,l)
              elif level==5:
                fiveHighscore.append(levelData[2])
                fiveHighscore.sort()
                fiveHighscoreDict.update({levelData[2]:name})
                print("Here are the highscores.")
                for l in fiveHighscore:
                  m = fiveHighscoreDict.get(l)
                  print(l)
              elif level==6:
                sixHighscore.append(levelData[2])
                sixHighscore.sort()
                sixHighscoreDict.update({levelData[2]:name})
                print("Here are the highscores.")
                for l in sixHighscore:
                  m = sixHighscoreDict.get(l)
                  print(l)
              guesser()
          elif numberOne>randomNumber:
            print("Your guess is too high. You have",levelData[2],"guesses remaining.") if levelData[3]==1 else print("Your guess is too high. You have taken",levelData[2],"guesses so far.")
          else:
            print("Your guess is too low. You have",levelData[2],"guesses remaining.")if levelData[3]==1 else print("Your guess is too low. You have taken",levelData[2],"guesses so far.")
        if levelData[2] == 0:
          print("You have ran out of Guesses, please try again.")
          guesser()
    guesser()
#one more line of code.
  elif a == "usernamepassword":
    userData = {
  "genericUser" : "15633uV^",
  "Joel" : "12345678",
  "Bobby" : "23124563",
  "Fred12345" : "iampassword",
    }
    websiterun = 1
    print("Welcome to website thingy.")
    while websiterun==1:
      print("Log in or create an account?")
      access = str(input(""))
      if access=="Log in" or access=="log in":
        print("Enter your username and password.")
        usernameInput = str(input("Username: "))
        passwordInput = str(input("Password: "))
        for userLoop in userData:
          if usernameInput==userLoop:
            if passwordInput==(userData[usernameInput]):
              print("Welcome",usernameInput,"to your account. Unfortunately, there are no features other than the login system, so you will be logged out. Logging out.")
            else:
              print("Your password is incorrect")
            break
      elif access=="create" or access=="create an account" or access=="Create an Account":
        print("Welcome to creating your account. Please enter a username and password for your account.")
        enoughCheck = 0
        while enoughCheck < 5:
          username = str(input("Username: "))
          password = str(input("Password: "))
          enoughCheck=0
          isupperCheck = 0
          isnumericCheck = 0
          islowerCheck = 0
          isspecialCheck = 0
          if len(password)>=8:
            enoughCheck+=1
          for check in password:
            if check.isupper() and isupperCheck==0:
              enoughCheck+=1
              isupperCheck = 1
            if check.isnumeric() and isnumericCheck==0:
              enoughCheck+=1
              isnumericCheck = 1
            if check.islower() and islowerCheck==0:
              enoughCheck+=1
              islowerCheck = 1
            if not(check.isalnum()) and isspecialCheck==0:
              enoughCheck+=1
              isspecialCheck = 1
          if enoughCheck==5:
            print("Your password is acceptable.")
            userData.update({username:password})
            print("Your account has been created, you may now go to login.")
          else:
            print("Your password is not strong enough. Make sure to include lowercase and uppercase letters, one special and one number, and is at least 8 characters long.")
      else:
        print("Please try again.")
  elif a == "tututu":
    import random
    terrariaList = ["t","e","r","r","a","r","i","a"]
    length = int(input("How many characters would you like to generate? "))
    countLength = 1
    concanted = terrariaList[random.randint(0, (len(terrariaList)-1))]
    while (length > countLength):
      concat = terrariaList[random.randint(0, (len(terrariaList)-1))]
      concanted = concat+concanted
      countLength+=1
    print(concanted)
    start()
  else:
      print("""You entered something that was not in this program. Please try again. 
Make sure your answer is in all lowercase and exactly as it is written.""")
      start()
start()