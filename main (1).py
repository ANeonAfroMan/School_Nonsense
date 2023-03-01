joeldata = {
  "Joel" : "12345678",
  "balance" : 9999999999,
}
userData = {
  "Joel" : joeldata,
}
import os
websiterun = 1
print("Welcome to the blackjack website.")
def webstart():
  while websiterun==1:
    print("Log in [1], create an account [2], or exit [3]?")
    access = str(input(""))
    if access=="Log in" or access=="log in" or access=="1":
      os.system('clear')
      print("Enter your username and password.")
      usernameInput = str(input("Username: "))
      global passwordInput
      passwordInput = str(input("Password: "))
      global incorrect
      incorrect = 0
      for userLoop in userData:
        if usernameInput==userLoop:
          incorrect += 1
          def password():
            global incorrect
            global passwordInput
            if passwordInput==(userData[usernameInput][usernameInput]):
              os.system('clear')
              print("Welcome",usernameInput,"to your blackjack account.")
              import random
              decklist = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10]
              gamerun = 1
              while gamerun == 1:
                print("Enter 1 to start blackjack or 2 to log out. You have $",userData[usernameInput]["balance"],"in your balance.")
                playloop = str(input(""))
                while playloop == "1":
                  if userData[usernameInput]["balance"] == 0:
                    print("You have no money, you cannot play.")
                    break
                  print("How much would you like to wager? Your balance is $",userData[usernameInput]["balance"],".")
                  try:
                    wager = int(input(""))
                  except:
                    print("Please enter a number.")
                  else:
                    if wager <= userData[usernameInput]["balance"] and wager > 0:
                      os.system('clear') 
                      print("You bet $",wager,".")
                      userData[usernameInput]["balance"] -= wager
                      print("Let's play!")
                      playloop = 2
                      activedecklist = decklist
                      cardTotal = 0
                      hitcheck = 1
                      while playloop <= 6:
                        if hitcheck == 1:
                          cardDraw = activedecklist.pop(random.randint(0,len(activedecklist))-1)
                          if cardDraw != 1: print("You just drew a",cardDraw,".")
                          cardTotal += cardDraw
                          if cardDraw == 1:
                            print("You just drew an ace. Do you want it to be worth 1 or 11. Anything entered other than an 11  is a 1.")
                            aceCheck = int(input(""))
                            if aceCheck == 11: cardTotal += 10
                          hitcheck = 0
                          if cardTotal > 21:
                            print("Your total is",cardTotal,", you have busted over 21, you lost your bet of $",wager,". Press enter to end the game.")
                            global slow
                            slow = input()
                            break
                        elif hitcheck == 2:
                          print("You stayed, now starting the dealer's turn.")
                          dealerCardTotal = 0
                          while dealerCardTotal < 16:
                            cardDraw = activedecklist.pop(random.randint(0,len(activedecklist))-1)
                            dealerCardTotal += cardDraw
                            print("The dealer just drew a",cardDraw,"and now has a total of",dealerCardTotal,"- Press enter to continue.")
                            slow = input()
                          print("The dealer stayed at",dealerCardTotal)
                          if dealerCardTotal > 21:
                            print("The dealer busted over 21 and loses. You win $",wager*2,"! Enter to finish.")
                            userData[usernameInput]["balance"] += wager*2
                            slow = input()
                            break
                          elif dealerCardTotal > cardTotal:
                            print("The dealer beat you. You lose your bet of $",wager,". Enter to finish.")
                            slow = input()
                            break
                          elif cardTotal > dealerCardTotal:
                            print("You beat the dealer, good job! You win $",wager*2,". Enter to finish.")
                            userData[usernameInput]["balance"] += wager*2
                            slow = input()
                            break
                          else:
                            print("You tied the dealer. Enter to finish.")
                            slow = input()
                            break
                        else:
                          print("That is not a valid input, please try again.")
                        if playloop <= 2:
                          hitcheck = 1
                          playloop += 1
                        else:
                          print("Your card total is",cardTotal,", do you want to hit [1] or stay [2]?")
                          hitcheck = int(input(""))
                        
                    else:
                      print("Please enter a valid wager. You cannot wager outside of your balance.")
                if playloop == "2": break
            else:
              incorrect += 1
              if incorrect == 6:
                print("You have guessed wrong too many times, logging you out.")
                webstart()
              print("Your password is incorrect. Please try your password again. You have",6-incorrect,"tries left")
              passwordInput = str(input("Password: "))
              password()
          password()
          break
      if (incorrect == 0): print("That username does not exist.")
    elif access=="create" or access=="create an account" or access=="Create an Account" or access=="2":
      os.system('clear')
      print("Welcome to creating your account. Please enter a username and password for your account.")
      enoughCheck = 0
      while enoughCheck < 5:
        username = str(input("Username: "))
        password = str(input("Password: "))
        if len(username)<6:
          print("Your username needs a minimum of 6 characters. Please try again.")
        else:
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
            userdict = {
              username : password,
              "balance" : 2000
            }
            userData.update({username:userdict})
            print("Your account has been created, you may now go to login. Enter to finish.")
            slow = input()
          else:
            print("Your password is not strong enough. Make sure to include lowercase and uppercase letters, one special and one number, and is at least 8 characters long.")
    elif access=="exit" or access=="3":
      os.system('clear')
      print("Exiting the website. Thank you for visiting.")
      print("Entering the website again.")
      webstart()
    else:
      print("Please try again.")
webstart()
if slow == "something":
  print("This is here just so replit doesn't yellow underline.")