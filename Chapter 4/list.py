friends = ["apple","mango", 5, 33.3, "banana"]          # this is list of different type of items...... 'lists' are mutable
print(friends[0])                         # we can store any type of data in list
friends[0] = "grapes"           # here we changed item present at index 0
print(friends[0])

print(friends[1:4])             # we can do slicing in list as we can in strings



# METHODS OF LIST

friends.append("pravin")               # append is used to add element at last index of the list 
print(friends)


list = [1,4,5,2,44,555,4,40]
list.sort()            # it will sort the list 
print(list)

list.reverse()          # it will reverse the list
print(list)

list.insert(3,55)          # .insert is used to add element at any index 
print(list)

value = list.pop(3)      # this will remove value present at that index also return that value
print(value)
print(list)

list.remove(555)
print(list)

# there are lot of methods in list we can use in dsa
