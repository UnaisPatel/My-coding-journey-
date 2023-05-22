#This program asks a user to enter a number and calculates the average of the numbers they have entered.
#This program ends when someone enters -1
number_list = []  #Declaring a list
num = 0
while num != -1 :  # while loop used so the program runs as long as num does not equal -1
    num = int(input("Enter a number if you want to stop enter -1 : \n> "))
    if num != -1 :
        number_list.append(num) # .append adds to the list

average = sum(number_list)/len(number_list) # calculates average 
print(average)

        

    

