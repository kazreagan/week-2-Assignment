#create an empty list
my_list = []

#appending/adding 10,20,30,40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# print(my_list)

#inserting the value 15 at the second position in the list
my_list.insert(1, 15)
# print(my_list)

#extending the list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
# print(my_list)

#removing the last element from the list
my_list.pop()
# print(my_list)

#sorting the list in ascending order
my_list.sort()
# print(my_list)

#finding an printing the index of the value 30 in the list
index_of_30 = my_list.index(30)
print(index_of_30)