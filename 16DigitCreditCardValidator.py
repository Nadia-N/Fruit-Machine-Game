ans = int(input("Enter Card Number: "))
#Asks for card number.
#4556737586899855
cardnum = list(str(ans))
#Turns the input into a list and splits the numbers up.
cardnum = [int(i) for i in cardnum]
#It then turns every value into an integer.

newnum = []
#Creates an empty list.
finnum = []
#Creates an empty list.
lastnum = []
#Creates an empty list.
total = 0
#Creates an empty value.

del cardnum[len(cardnum) - 1]
#Deletes the final number in the credit card number.

for i in range(len(cardnum)):
#For every element in the card number.
        newnum.insert(0, cardnum[i])
        #Insert the number to the start of the list.

for i in range(len(newnum)):
#For every element in the card number.
    if i%2 == 0:
        #If the modulus of the index is 0 (this checks if the position is odd.
        x = newnum[i] * 2
        #X equals the number held in the index multiplied by 2.
        finnum.append(x)
        #The value is then added into the list called 'finnum'.
    else:
        #Otherwise it just adds the normal value to the list 'finnum'.
        finnum.append(newnum[i])

for i in range(len(finnum)):
#For every element in the card number.
    if 9 < finnum[i]:
        #If the value held in the index is bigger than 9.
        x = finnum[i] - 9
        #X equals the value held in the index minus 9.
        lastnum.append(x)
        #The value is added to the list 'lastnum'.
    else:
        #Otherwise it just adds the normal value to the list 'lastnum'.
        lastnum.append(finnum[i])

for i in range(len(lastnum)):
#For every element in the card number
    total = total + lastnum[i]
    #Adds every element to the total.

total = total % 10
#The total equal the modulus of all the values added together.

if total == cardnum[len(cardnum) - 1]:
#If the total is equal to the final digit in the card number.
    print("valid")
    #Output valid.
else:
#Otherwise..
    print("Not Valid")
    #Output invalid.

print(cardnum)
print(newnum)
print(finnum)
print(lastnum)
