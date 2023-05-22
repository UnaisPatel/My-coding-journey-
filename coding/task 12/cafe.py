# This program shows you the menu of a cafe and the total value of the items in the cafe 

menu = ["pizza" , "coffee", "tea", "bread"]          # creating a list of the menu items
stock = {"pizza" : 52, "coffee" : 72, "tea" : 65, "bread" : 60}          # creating a dictionary 
price = {"pizza" : 6.2, "coffee" : 2.5, "tea" : 3.4, "bread" : 1.5}
keys = {"pizza" : "A", "coffee" : "B", "tea" : "c", "bread": "d"}        # setting keys so it is easy to iterate


#creating a function to iterate through the list and dictionary

def total_stock_value():
    total_value = 0
    for i in menu:          # using a for loop to iterate through each item
        total_value += stock[i] * price[i]
    return (total_value)
value = total_stock_value() 
print(value)
