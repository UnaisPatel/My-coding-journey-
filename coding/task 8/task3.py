#This program in comments asks a user to enter a number of rows.
num = int(input("Please enter the number of rows you would like :\n> ")) 
for i in range (1,(num + 1)) :  #for loop starts at 1 and ends at the number which the user has entered
    print("*" * i)  #the * is multiplied by i which increases from 1 to whatever the user enters


#for i in range (1,6) : # for loop starts at 1 and end at 5
    #print("*" * i) # multiplies the * by i which increases from 1 to 5