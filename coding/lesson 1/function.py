# This program gives the user the ability to do simple maths calculations which are saved to a file and they can acess this file

def calc():     # defining a function called calc
     
    with open('calculator.txt', 'w') as file :    # opening a text file in write mode. the with at the start automatically closes the file when you are finished
        
        while True:    # while loop to keep the programme running
            is_valid = False
            user_choice = input("Please enter a number (Enter stop to end ) : ") 
            if user_choice.lower() == "stop":
                break
            try :   # using a try block to make it robust if the user enters anything apart from an integer it will print the statement
                user_choice = int(user_choice)
                is_valid = True
            except:
                print("Enter a valid number")
                continue
            is_valid = False  # this is checking if the user entered a valid number or not
        

            user_op = input("Please enter an operator : ")
    
            user_num2 = input("Please enter another number : ")
            try:
                user_num2 = int(user_num2)
                is_valid = True
            except :
                print("Enter a valid number")
    
    
            def add (num1, num2) :   # declaring a function for each calculation
                return (num1 + num2)
            def minus (num1, num2) :
                return (num1 - num2)
            def multiply (num1, num2) :
                return (num1 * num2)
            
            

    
    
# we are using if and elif statments here to make sure the user has entered a proper operator and doing the calculation. it will be written to a text file
            if is_valid and user_op == "+":
                result = (add(user_choice, user_num2))
                print(result)
                file.write(f"{user_choice} + {user_num2} = {result}\n")
            
            elif is_valid and user_op == "-" :
                result =(minus(user_choice, user_num2))
                print(result)
                file.write(f"{user_choice} - {user_num2} = {result}\n")
            
            elif is_valid and user_op == "*" :
                result =(multiply(user_choice, user_num2))
                print(result)
                file.write(f"{user_choice} * {user_num2} = {result}\n")
            else :
                print("Enter a valid operator.")
    

# defining a function called read so a user can access the calculator file

          
def read():
    file_name = input("Enter the name of the file you want to open: ")
    try:
        if file_name == "calculator":
            with open("calculator.txt", "r") as file:  #opening in read mode so the user can only read
                lines = file.readlines()
                for line in lines:  # reads each line
                    print(line.strip()) #strips of any whitespaces
        else: 
            raise FileNotFoundError                
    except FileNotFoundError:  #if it is the wrong file entered by the user it will print invalid file
        print("Invalid file")    
        
#making the user choose what they want to do 
while True :
         
    print("Select an option:")
    print("1 - Enter two numbers and an operator")
    print("2 - Read equations from a file")

    option = input()


    if option == '1':   #if they choose 1 the function of calc will execute
        calc()
    elif option == '2':  # if they choose 2 the function of read will execute
        read()
    else:
        print("Invalid option!")
                
            
                   
        
        

            