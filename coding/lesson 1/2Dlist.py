my_list = [[1, 2, 3] , [4, 5, 6] , [7, 8, 9]]
#print(my_list[0][0])
#print(len(my_list[2]))
my_list.append([7, 8, 9])
#print(my_list[-1][-2])
my_list.insert(2, [20, 21, 22])
my_list[0][2] = 11
my_list[2] = [15, 14, 13]

#for row in my_list: #row holds the value of the whole list
 #   for inside_list in row : #inside list holds the value of whatever is inside each list
  #      print(inside_list, end= ' ')
   # print()    

for num in range(len(my_list)):
    print(num)
    my_list[num].append(f"Row number {num + 1}")

for line in my_list :
    print (line)



