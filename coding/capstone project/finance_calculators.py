import math

#This program calculates peoples investments or bonds depending on what they want to be calculated
investment = print ("investment - to calculate the amount of interest you'll earn on your investment. ")
bond = print("bond - to calculate the amount you'll have to pay on a home loan. ")

#While loop here to carry the program going on if something other than investment or bond is entered
#asking the user to choose bond or investments and calculating using the formula



while (True) :
    choice = input("Enter either Investment or Bond from the menu above to proceed :\n>  ").lower()

    if choice == "investment"  :
        
        deposit = float(input("how much money are you investing ?\n>"))
        interest_rate = float(input("what is the percentage of interest on your investment ?\n>"))
        num_of_years = float(input("How many years do you want to invest for?\n> "))
        r = interest_rate/100
        type_of_interest = input("What type of interest do you want to do ? Simple or compound ?\n>").lower()
        
        if type_of_interest == "simple" :
            print (f" You will make £{deposit*(1 + r*num_of_years)} off of your investment")
            break
        elif type_of_interest == "compound" :
            print (f" You will make £{deposit * math.pow((1 + r),num_of_years)} off of your investment")
            break
#break is used so the program stops once they have got their value 
    
    if choice == "bond" :
        house_value = float(input("what is the value of your house ?\n> "))
        interest_rate_2 = float(input("What is the interest rate ?\n> "))
        num_of_months = float(input("How many months do you plan on paying it off ?\n> "))
        monthly_interest_rate = (interest_rate_2/100)/12
        print (f" You will have to pay £{(monthly_interest_rate * house_value)/ (1 - (1 + monthly_interest_rate) ** (-num_of_months))} each month")
        break
    



