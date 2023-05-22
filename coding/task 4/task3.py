#Asking for how long it took them in each activity
swimming = int(input("How many minutes did it take for you to complete the swimming? :"))
cycling = int(input("How many minutes did it take for you to complete the cycling? :"))
running = int(input("How many minutes did it take for you to complete the running? :"))
#Adding the time for each activity
Total = swimming + cycling + running
#using format method 
print (f"well done it took you : {Total} minutes")
#using if statement and greater than and equal to sign
if Total <= 100:
    print ("Well done you have achieved the Provincial colours!!")
#using elif statement to make sure it stays in the range of 100 and 105
elif Total < 105 and (Total) > 100 :
    print("Well done you have achieved the Provincial half colours!!")
#using it again to make sure it stays in the range of 105nand 110
elif Total < 110 and (Total) > 105 :
    print("Well done you have achieved the Provincial Scroll!!")
#stopping the loop with else
else : 
    print("Well done you have tried your best but due to you getting over 110 minutes you get no award")



