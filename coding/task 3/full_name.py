full_name = input("please enter your full name :")
if len(full_name) == 0 : # len calculates how many characters have been entered. if it is 0 then this function will take place
    print ("you have not entered anything. Please enter your name")
elif len(full_name) < 4 : # more than sign is used here to make sure they enter more than 4 characters
    print("you have entered less than 4 characters. Please enter your first name and surname") 
elif len(full_name) > 25 : # less than sign is used to make sure it does not exceed 25 characters
    print("you have entered more than 25 characters. Please make sure you have only entered your full name")
else :
    print("thank you for entering your name ")