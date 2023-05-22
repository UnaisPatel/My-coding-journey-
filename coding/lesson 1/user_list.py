user_list = []
while True :
    num = input("Please enter a number : ")
    if num.lower() == "stop" :
        break
    try :
        num = int(num)
        user_list.append(num)
    except :
        print("Please enter only a number.")
print (user_list)
