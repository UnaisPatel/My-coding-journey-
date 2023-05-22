# This program gives the user the ability to do simple maths calculations which are saved to a file and they can acess this file




def add (num1, num2) :   # declaring a function for each calculation
    return (num1 + num2)
def minus (num1, num2) :
    return (num1 - num2)
def multiply (num1, num2) :
    return (num1 * num2)
def divide (num1, num2) :
    if num2 == 0:
        print("Cannot divide by zero. Enter a valid number.")
        return None
    return num1 / num2
    
file_name = input("Enter the name of the file you want to create : \n> ").lower()



def calc():     # defining a function called calc
    
    with open(file_name, 'a') as file :    # opening a text file in write mode. 
        
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
    
    
    
# we are using if and elif statments here to make sure the user has entered a proper operator and doing the calculation. it will be written to a text file
            if is_valid and user_op == "+":
                result = (add(user_choice, user_num2))
                print(f"{user_choice} + {user_num2} = {result}")
                file.write(f"{user_choice} + {user_num2} = {result}\n")
            
            elif is_valid and user_op == "-" :
                result =(minus(user_choice, user_num2))
                print(f"{user_choice} - {user_num2} = {result}")
                file.write(f"{user_choice} - {user_num2} = {result}\n")
            
            elif is_valid and user_op == "*" :
                result =(multiply(user_choice, user_num2))
                print(f"{user_choice} * {user_num2} = {result}")
                file.write(f"{user_choice} * {user_num2} = {result}\n")
            elif is_valid and user_op == "/" :
                result = (divide(user_choice,user_num2))
                print(f"{user_choice} / {user_num2} = {result}")
                file.write(f"{user_choice} / {user_num2} = {result}\n")
                if result is not None:
                    print(result)
                    file.write(f"{user_choice} / {user_num2} = {result}\n")
                else:
                    continue
                
            else :
                print("Enter a valid operator.")
        file.close()

# defining a function called read so a user can access the calculator file

          
def read():
    open_file = input("Enter the name of the file you want to open: \n> ").lower()
    try:
        if open_file == file_name :
            with open(file_name, "r") as read_file:  #opening in read mode so the user can only read
                lines = read_file.readlines()
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
    print("3 - Exit the program")

    option = input()


    if option == '1':   #if they choose 1 the function of calc will execute
        calc()
    elif option == '2':  # if they choose 2 the function of read will execute
        read()
    elif option == '3':
        break
    else:
        print("Invalid option!")