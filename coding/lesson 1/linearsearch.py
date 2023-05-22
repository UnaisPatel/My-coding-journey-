array = ["1" , "2"]
def linear_search(array, item_to_collect) :
    for index in range(len(array)) :
        if array [index] == item_to_collect :
            return index
        return -1
print()