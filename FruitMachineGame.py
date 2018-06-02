#The random library needs to be imported in order to randomise what symbols come up.
import random
#This list are the possible symbols that can be used by the program
symbols = ["Cherry","Bell", "Lemon", "Orange", "Star", "Skull"]
#This condition is necessary for the while loop.
valid = False
#Credit starts at £1
credit = 1.00

#While the variable valid is true...
while valid == False:
#Try to...
  try:
    #Ask this question.
    question = input("Would you like to play? There is a 20p charge. Type Y or N.")
    #If user types "N"...
    if question == "N":
      #Print goodbye message.
      print("Goodbye!")
      #Stop program.
      break
    #If the user inputs "Y"
    if question == "Y":
      #Credit has 20p taken of of it as a play charge.
      credit = credit - 0.20
      #If the credit is less than 0...
      if credit <= 0:
        #Output 'You have no money left'...
        print("You have no money")
        #And end the program.
        break
      #Print the amount of money the user has.
      print("You have £",(str(round(credit,3)))+"0")
      #Get the index for the first symbol.
      symbol1 = random.randint(0,5)
      #Get the index for the second symbol.
      symbol2 = random.randint(0,5)
      #Get the index for the third symbol.
      symbol3 = random.randint(0,5)
      #This prints out the symbols.
      print(symbols[symbol1], symbols[symbol2], symbols[symbol3])

      #If all the symbols are the same...
      if symbol1 == symbol2 and symbol2 == symbol3:
        #If all the symbols are bells...
        if symbols[symbol1] == "Bell":
          #Add £5 to the credit.
          credit = credit + 5
          #Output to the user they won £5 and show them their current credit amount.
          print("You have won £5. You have £",(str(round(credit,3)))+"0",".")
        #If the symbols are all skulls...
        elif symbols[symbol1] == "Skull":
          #Output you have lost all your money.
          print("All your money has been lost.")
          #End the program.
          break
        #If they just have three of the other symbols...
        else:
          #Add £1 to their credit.
          credit = credit + 1
          #Output to the user telling them they won £1 and show them their current amount.
          print("You have won £1. You have £",(str(round(credit,3)))+"0","remaining")
      #If two of the symbols match...
      elif symbol1 == symbol2 or symbol1 == symbol3 or symbol2 == symbol3:
        #If the first and third symbols are the same...
        if (symbols[symbol1]=="Skull" and symbols[symbol2]=="Skull"):
          #Take £1 away from their credit...
          credit = credit - 1
          #Output to the user telling them they have lost £1 and tell the user their balance.
          print("You have lost £1.")
        #If the second and third symbols are the same...
        elif (symbols[symbol2]=="Skull" and symbols[symbol3]=="Skull"):
          #Take away £1 from their credit...
          credit = credit - 1
          #Output to the user telling them they have lost £1 and tell the user their balance.
          print("You have lost £1.")
        #If the first and third symbol are the same...
        elif symbols[symbol1]=="Skull" and symbols[symbol3]=="Skull":
          #Take away £1 from their credit...
          credit = credit - 1
          #Output to the user telling them they have lost £1.
          print("You have lost £1.")
          #If your credit is lower than 1...
          if credit <= 0:
            #Tell the user they have no money left
            print("You have no money left.")
            #End the program.
            break
        #Otherwise..
        else:
          #Add 50p to the users credit amount.
          credit = credit + 0.50
          #Tell them they won 50p and show their balance.
          print("You have won 50p. You have £",(str(round(credit,3)))+"0","remaining")
      #If credit is lower than 0...
      elif credit <= 0:
          #Tell the user they have no money left.
          print("You have no money left.")
          #End the program.
          break
      #Otherwise..
      else:
          #Tell the user nothing has happened. It then tells the user the credit amount.
          print("Nothing has happened. You have £",(str(round(credit,3)))+"0","remaining")
  #This bit doesn't work, I don't know why. It the user enters anything but "Y"...
  except ValueError:
    #Tell the user to try again.
      print("Please try again.")