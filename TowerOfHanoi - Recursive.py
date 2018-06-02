import time
s = [5,4,3, 2, 1]
# Creates the list, which acts as the tower, which has all the disks on.
a = []
# Creates an empty list which acts as another tower.
d = []
# Creates an empty list which acts as another tower.
def toh(s,a,d):
    #Create the function to hold the program in celled 'toh'.
    end_state = [5,4,3, 2, 1]
    # This is what the end tower should end up as.
    time.sleep(2)
    # Delay the program by 2.
    if len(d) == 0:
        # If tower D is empty.
        disk = s.pop()
        # The variable disk is the variable that is removed from tower S.
        d.append(disk)
        # Add the value held in disk to tower A.
    elif len(s) == 0:
     # If tower S is empty.
        disk = d.pop()
     # The variable disk is the variable that is removed from tower D.
        s.append(disk)
     # Add the value held in disk to tower S.
    else:
    # Otherwise...
        if s[len(s) - 1] < d[len(d) - 1]:
        # If the end value in tower S is smaller then the end value in tower D.
            disk = s.pop()
            # The variable disk is the variable that is removed from tower S.
            d.append(disk)
            # Add the value held in disk to tower D.
        elif d[len(d) - 1] < s[len(s) - 1]:
        # If the end value of tower D is smaller than tower A...
            disk = d.pop()
            # The variable disk is the variable that is removed from tower D.
            s.append(disk)
            # Add the value held in disk to tower S.
    print(s, a, d)
    # Output the towers.
    time.sleep(1)
    #Delay the program by 1 second.
    if d == end_state:
    #If tower D is equal to the end state
        return (s, a, d)
        # Return the towers from the function.

    if len(a) == 0:
    # If tower D is equal to 0.
        disk = s.pop()
        # The variable disk is the variable that is removed from tower S.
        a.append(disk)
        # Add the value held in disk to tower A.
    elif len(s) == 0:
    # If tower S is empty...
        disk = a.pop()
        # The variable disk is the variable that is removed from tower D.
        s.append(disk)
        # Add the value held in disk to tower S.
    else:
    #Otherwise...
        if s[len(s) - 1] < a[len(a) - 1]:
        # If the end value of tower S is smaller than the end value of tower A.
            disk = s.pop()
            # The variable disk is the variable that is removed from tower S.
            d.append(disk)
            # Add the value held in disk to tower D.
        elif a[len(a) - 1] < s[len(s) - 1]:
        # If the end value of D is smaller than tower S.
            disk = a.pop()
            # The variable disk is the variable that is removed from tower A.
            s.append(disk)
            # Add the value held in disk to tower S.

    print(s, a, d)
    # Output the towers.
    time.sleep(1)
    # Delay the program by 1 second.

    if len(a) == 0:
    # If tower A is empty...
        disk = d.pop()
        # The variable disk is the variable that is removed from tower D.
        a.append(disk)
        # Add the value held in disk to tower A.
    elif len(d) == 0:
    # If tower D is empty.
        disk = a.pop()
        # The variable disk is the variable that is removed from tower A.
        d.append(disk)
        # Add the value held in disk to tower D.
    else:
    #Otherwise...
        if d[len(d) - 1] < a[len(a) - 1]:
        #If the final value in D is smaller than the final value in A...
            disk = d.pop()
            # The variable disk is the variable that is removed from tower D.
            a.append(disk)
            # Add the value held in disk to tower A.
        elif a[len(a) - 1] < d[len(d) - 1]:
        # If the final value in D is smaller than the final value in A...
            disk = a.pop()
            # The variable disk is the variable that is removed from tower A.
            d.append(disk)
            # Add the value held in disk to tower D.
    print(s, a, d)
    # Output the towers.
    time.sleep(1)
    #Delay the program by 1 second.
    toh(s, a, d)
    #Run the function.

toh(s,a,d)
#Run the function.